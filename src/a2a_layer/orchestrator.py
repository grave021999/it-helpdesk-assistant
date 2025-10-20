from src.a2a_layer.agents import (
    DataAgent, AnalyticsAgent, LLMAgent,
    ReportAgent, TrendAgent, AssignmentAgent,
    UserActivityAgent
)
from src.a2a_layer.intent_classifier import IntentClassifierAgent


class Orchestrator:
    def __init__(self):
        self.data_agent = DataAgent()
        self.analytics_agent = AnalyticsAgent()
        self.report_agent = ReportAgent()
        self.trend_agent = TrendAgent()
        self.assignment_agent = AssignmentAgent()
        self.user_activity_agent = UserActivityAgent()
        self.llm_agent = LLMAgent()
        self.intent_agent = IntentClassifierAgent(use_llm=False)
        self.last_trend_image = None

    def process_query(self, query: str):
        intents = self.intent_agent.classify_multi(query)
        df = self.data_agent.handle_query(query)
        context_sections = []

        if "analytics" in intents:
            analytics_output = self.analytics_agent.summarize_data(df)
            context_sections.append(("Analytics Summary", analytics_output))

        if "report" in intents:
            report_output = self.report_agent.generate_report(df)
            context_sections.append(("Report", report_output))

        if "trend" in intents:
            trend_output = self.trend_agent.analyze_trends(df)
            if isinstance(trend_output, dict):
                trend_text = trend_output["summary"]
                self.last_trend_image = trend_output["image_base64"]
                context_sections.append(("Trend Analysis", trend_text))
            else:
                context_sections.append(("Trend Analysis", trend_output))

        if "assignment" in intents:
            assign_output = self.assignment_agent.summarize_assignments(df)
            context_sections.append(("Workload Analysis", assign_output))

        if "user" in intents:
            user_output = self.user_activity_agent.summarize_users(df)
            context_sections.append(("User Activity", user_output))

        combined_context = "\n\n".join([f"{title}:\n{content}" for title, content in context_sections])
        answer = self.llm_agent.generate_response(query, combined_context)
        return f"{answer}"
