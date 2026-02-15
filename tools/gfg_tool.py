# tools/gfg_tools.py
import requests
from bs4 import BeautifulSoup

GFG_SEARCH_URL = "https://www.geeksforgeeks.org/?s={query}"

def get_gfg_links(topic: str):
    topic = topic.lower()
    search_url = GFG_SEARCH_URL.format(query=topic)
    resp = requests.get(search_url)
    if resp.status_code != 200:
        return {"tutorial": None, "interview": None, "roadmap": None}

    soup = BeautifulSoup(resp.text, "html.parser")
    links = soup.find_all("a", href=True)

    result = {"tutorial": None, "interview": None, "roadmap": None}

    for link in links:
        href = link["href"]
        text = link.get_text().lower()
        if topic in href or topic in text:
            if "tutorial" in href or "tutorial" in text:
                if not result["tutorial"]:
                    result["tutorial"] = href
            elif "interview" in href or "interview" in text:
                if not result["interview"]:
                    result["interview"] = href
            elif "roadmap" in href or "roadmap" in text:
                if not result["roadmap"]:
                    result["roadmap"] = href
    return result