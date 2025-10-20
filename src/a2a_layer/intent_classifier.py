from openai import OpenAI

client = OpenAI()

class IntentClassifierAgent:
    def __init__(self, use_llm=False):
        self.use_llm = use_llm

    def classify_multi(self, query: str):
        query_lower = query.lower()
        intents = set()

        if "report" in query_lower:
            intents.add("report")
        if "trend" in query_lower:
            intents.add("trend")
        if "assign" in query_lower or "workload" in query_lower:
            intents.add("assignment")
        if "user" in query_lower or "created" in query_lower:
            intents.add("user")
        if "summary" in query_lower or "count" in query_lower or "how many" in query_lower:
            intents.add("analytics")

        if not intents:
            intents.add("analytics")

        return list(intents)

    def classify(self, query: str):
        return self.classify_multi(query)[0]
