from src.data_layer.load_data import load_ticket_data
from src.mcp_layer.context_adapter import TicketContextAdapter
from src.mcp_layer.query_builder import QueryBuilder

data_path = "data/dummy_it_tickets.csv"
df = load_ticket_data(data_path)

context = TicketContextAdapter(df)
builder = QueryBuilder(df)

print("Schema:", context.get_schema())
print("Summary:", context.get_summary())

queries = [
    "how many open tickets are there?",
    "how many critical tickets in last 7 days?",
    "show high priority tickets"
]

for q in queries:
    print(f"\n🔹 Query: {q}")
    print(builder.summarize(q))
