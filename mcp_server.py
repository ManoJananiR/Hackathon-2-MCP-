from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tools.gfg_tool import get_gfg_links

app = FastAPI(title="Dynamic MCP Agent")

class MCPQuery(BaseModel):
    topic: str

@app.post("/mcp_query")
def mcp_query(query: MCPQuery):
    topic = query.topic.strip()
    if not topic:
        raise HTTPException(status_code=400, detail="Topic required")

    # Dynamically fetch GFG links
    links = get_gfg_links(topic)
    
    return {"topic": topic, "links": links}

@app.get("/")
def root():
    return {"status": "MCP running"}