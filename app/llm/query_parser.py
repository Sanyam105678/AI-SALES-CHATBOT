import json
from typing import Dict


def parse_query_with_llm(user_query: str) -> Dict:
    """
    Parse natural language query into structured intent
    (LLM placeholder – rule-based + prompt-ready)
    """

    query = user_query.lower()

    intent = {
        "metric": None,
        "group_by": None,
        "year": None,
        "month": None,
        "brand": None,
        "chart": False
    }

    # Metric detection
    if "sale" in query:
        intent["metric"] = "sales"

    if "store" in query:
        intent["metric"] = "active_stores"

    # Chart detection
    if any(word in query for word in ["show", "chart", "graph", "plot", "trend"]):
        intent["chart"] = True

    # Group by detection
    if "month" in query:
        intent["group_by"] = "Month"
    elif "year" in query:
        intent["group_by"] = "Year"
    elif "region" in query:
        intent["group_by"] = "Region"
    elif "brand" in query:
        intent["group_by"] = "Brand"

    # Year detection (simple)
    for y in range(2020, 2031):
        if str(y) in query:
            intent["year"] = y
            break

    # Month detection
    month_map = {
        "january": 1, "february": 2, "march": 3, "april": 4,
        "may": 5, "june": 6, "july": 7, "august": 8,
        "september": 9, "october": 10, "november": 11, "december": 12
    }

    for name, num in month_map.items():
        if name in query:
            intent["month"] = num
            break

    # Brand detection (simple placeholder)
    # Later this will come from dynamic brand list
    if "neo" in query:
        intent["brand"] = "Neo"
    print("#################intent",intent)
    return intent
