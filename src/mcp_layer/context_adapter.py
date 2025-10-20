import pandas as pd

class TicketContextAdapter:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def get_schema(self):
        return list(self.df.columns)

    def get_summary(self):
        return {
            "total_tickets": len(self.df),
            "status_counts": self.df["status"].value_counts().to_dict(),
            "priority_counts": self.df["priority"].value_counts().to_dict(),
            "categories": self.df["category"].unique().tolist(),
        }

    def filter_tickets(self, **filters):
        temp = self.df.copy()
        for key, value in filters.items():
            if key in temp.columns:
                temp = temp[temp[key].str.lower() == value.lower()]
        return temp
