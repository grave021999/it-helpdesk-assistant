import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.a2a_layer.orchestrator import Orchestrator

if __name__ == "__main__":
    orchestrator = Orchestrator()

    queries = [
        "generate a weekly report for tickets",
        "show me the trend of tickets over time",
        "who has the most workload right now",
        "which user created the most tickets",
        "send an alert for open critical tickets",
        "how many open tickets are there"
    ]

    for q in queries:
        print(f"\nQuery: {q}")
        print(orchestrator.process_query(q))
