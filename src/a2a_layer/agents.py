import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from openai import OpenAI
from src.mcp_layer.context_adapter import TicketContextAdapter
from src.mcp_layer.query_builder import QueryBuilder
from src.data_layer.load_data import load_ticket_data
import os

client = OpenAI()

# ==========================================================
# ===============   CORE AGENTS (with MCP)   ===============
# ==========================================================

class DataAgent:
    """Fetches and filters ticket data using MCP (ContextAdapter + QueryBuilder)."""
    def __init__(self):
        filepath = os.path.join("data", "dummy_it_tickets.csv")
        self.df = load_ticket_data(filepath)

        # Initialize MCP layer
        self.context_adapter = TicketContextAdapter(self.df)
        self.query_builder = QueryBuilder(self.df)

    def handle_query(self, query: str):
        """Use MCP's QueryBuilder to filter based on user query."""
        filtered_df = self.query_builder.parse(query)
        return filtered_df

    def get_context_summary(self):
        """Provide context summary using MCP ContextAdapter."""
        return self.context_adapter.get_summary()


class AnalyticsAgent:
    """Performs basic descriptive analytics."""
    def summarize_data(self, df):
        if df.empty:
            return "No data found matching the query."
        total = len(df)
        by_status = df["status"].value_counts().to_dict()
        by_priority = df["priority"].value_counts().to_dict()
        return f"There are {total} tickets. Status breakdown: {by_status}. Priority breakdown: {by_priority}."


class ReportAgent:
    """Generates weekly reports."""
    def generate_report(self, df):
        if df.empty:
            return "No data available to generate a report."
        df["created_date"] = pd.to_datetime(df["created_date"])
        last_7 = df[df["created_date"] >= (df["created_date"].max() - pd.Timedelta(days=7))]
        total = len(last_7)
        by_priority = last_7["priority"].value_counts().to_dict()
        return f"In the past week, {total} tickets were created. Priority breakdown: {by_priority}."


class TrendAgent:
    """Analyzes ticket trends and generates visual graphs."""
    def analyze_trends(self, df):
        if df.empty:
            return {"summary": "No data available for trend analysis.", "image_base64": None}

        df["created_date"] = pd.to_datetime(df["created_date"])
        trend = df.groupby(df["created_date"].dt.date).size()

        # Plot line chart
        fig, ax = plt.subplots(figsize=(7, 4))
        trend.plot(kind="line", marker="o", ax=ax)
        ax.set_title("Ticket Trend Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Tickets Created")
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Convert to base64 image
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode("utf-8")
        plt.close(fig)

        max_date = trend.idxmax()
        max_val = trend.max()
        avg_val = round(trend.mean(), 2)
        summary = (
            f"Ticket trend shows an average of {avg_val} tickets per day. "
            f"The busiest day was {max_date} with {max_val} tickets created."
        )
        return {"summary": summary, "image_base64": image_base64}


class AssignmentAgent:
    """Summarizes workload distribution."""
    def summarize_assignments(self, df):
        if df.empty:
            return "No data available for assignment analysis."
        counts = df["assigned_to"].value_counts().head(5).to_dict()
        top_person = next(iter(counts))
        return f"{top_person} has the highest workload with {counts[top_person]} tickets. Top 5 workloads: {counts}"


class UserActivityAgent:
    """Summarizes user activity."""
    def summarize_users(self, df):
        if df.empty:
            return "No user data available."
        counts = df["created_by"].value_counts().head(5).to_dict()
        top_user = next(iter(counts))
        return f"{top_user} has created the most tickets ({counts[top_user]} total). Top 5 creators: {counts}"


# ==========================================================
# ===============   LLM AGENT (Human Output)  ===============
# ==========================================================

class LLMAgent:
    """Generates natural language summaries using OpenAI."""
    def generate_response(self, question: str, context: str):
        prompt = f"""
        You are an intelligent IT Helpdesk Assistant AI.
        Summarize the findings below in a clear, human-friendly way.
        Use short paragraphs, natural sentences, and small headings.
        Avoid repeating raw dictionaries or lists.
        Write as if presenting insights to a manager.

        Question: {question}
        Context: {context}
        """

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return completion.choices[0].message.content.strip()
