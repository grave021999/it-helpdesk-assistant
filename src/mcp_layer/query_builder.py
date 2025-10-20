import re
import pandas as pd
from datetime import datetime, timedelta

class QueryBuilder:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def parse(self, query: str) -> pd.DataFrame:
        query = query.lower()
        filtered = self.df.copy()

        if "open" in query:
            filtered = filtered[filtered["status"].str.lower() == "open"]
        elif "closed" in query:
            filtered = filtered[filtered["status"].str.lower() == "closed"]

        if "critical" in query:
            filtered = filtered[filtered["priority"].str.lower() == "critical"]
        elif "high" in query:
            filtered = filtered[filtered["priority"].str.lower() == "high"]
        elif "low" in query:
            filtered = filtered[filtered["priority"].str.lower() == "low"]

        if "last 7 days" in query or "past 7 days" in query or "in 7 days" in query:
            now = datetime.now()
            week_ago = now - timedelta(days=7)
            filtered = filtered[
                (filtered["created_date"] >= week_ago)
                & (filtered["created_date"] <= now)
            ]

        return filtered

    def summarize(self, query: str) -> str:
        result_df = self.parse(query)
        count = len(result_df)
        return f"There are {count} tickets matching your query."
