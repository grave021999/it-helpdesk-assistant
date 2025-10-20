import pandas as pd
import os

def load_ticket_data(filepath: str):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    df = pd.read_csv(filepath)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    if "created_date" in df.columns:
        df["created_date"] = pd.to_datetime(df["created_date"], errors="coerce")
    
    return df

if __name__ == "__main__":
    data_path = "data/dummy_it_tickets.csv"
    df = load_ticket_data(data_path)
    print("✅ Dataset loaded successfully!")
    print(df.head())
