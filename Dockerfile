FROM python:3.14.2

# WORKDIR /app

# # ENV PYTHONDONTWRITEBYTECODE=1
# # ENV PYTHONUNBUFFERED=1

# # COPY requirements.txt ./


# COPY . .
# RUN pip install --upgrade pip \
#     && pip install --no-cache-dir fastapi uvicorn requests groq \
#     && pip install --no-cache-dir archestra-ai

# # EXPOSE 8000

# CMD ["uvicorn", "mcp_server.main:app", "--host", "0.0.0.0", "--port", "8000"]

WORKDIR /app

COPY requirements.txt .

RUN  pip install --no-cache-dir -r requirements.txt 

COPY . .

CMD ["uvicorn", "mcp_server:app", "--reload", "--port", "8080"]
