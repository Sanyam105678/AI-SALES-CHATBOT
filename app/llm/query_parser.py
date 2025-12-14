import json
from typing import Dict


def parse_query_with_llm(user_query: str) -> Dict:
    """
    Parse natural language query into structured intent
    (LLM placeholder – rule-based + prompt-ready)
    """
    brand_list = ["delphy", "neo", "rasbury", "silk", "solerone","su ruc"]
    query = user_query.lower()
    # print("############query",query)
    intent = {
        "metric": None,
        "group_by": None,
        "year": None,
        "month": None,
        "brand": None,
        "product": None,
        "chart": False,
        "compare": False
    }


    # Metric detection
    if any(word in query for word in ["active store", "active stores", "unique store", "unique stores"]):
        intent["metric"] = "active_stores"
    elif "sale" in query:
        intent["metric"] = "sales"

    # Comparison detection
    if any(word in query for word in ["compare", "vs", "versus", "between", "difference"]):
        intent["compare"] = True

    
   
    # Chart detection
    if any(word in query for word in ["show", "chart", "graph", "plot", "trend"]):
        intent["chart"] = True

    for brand in brand_list:
        if brand in query:
            # print("###################br",brand)
        
            intent["brand"] = brand

    # Group by detection
    # Group by detection
    if intent["compare"]:
        intent["group_by"] = "Year"
    elif any(word in query for word in ["by month", "monthly"]):
        intent["group_by"] = "Month"
    elif any(word in query for word in ["by year", "yearly"]):
        intent["group_by"] = "Year"
    elif "by brand" in query:
        intent["group_by"] = "Brand"
    elif "by product" in query:
        intent["group_by"] = "Product"
    elif "by region" in query:
        intent["group_by"] = "Region"
    else:
        intent["group_by"] = None



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
    # if "neo" in query:
    #     intent["brand"] = "Neo"
    # print("#################intent",intent)
    return intent
