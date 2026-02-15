def get_gfg_link(query: str):
    q = query.lower()

    if "java tutorial" in q:
        return "https://www.geeksforgeeks.org/java/java/"

    if "java interview" in q:
        return "https://www.geeksforgeeks.org/java/java-interview-questions/"

    if "python tutorial" in q:
        return "https://www.geeksforgeeks.org/python/python-programming-language-tutorial/"

    if "python interview" in q:
        return "https://www.geeksforgeeks.org/python/python-interview-questions/"

    if "gfg" in q or "geeksforgeeks" in q:
        return "https://www.geeksforgeeks.org/"

    return "No GFG link found"
