import os
import json
from openai import OpenAI
from dotenv import load_dotenv
# Load variables from .env file
load_dotenv()

client = OpenAI()

models = client.models.list()
for m in models.data:
    print(m.id)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT_TEMPLATE = """
You are a project generator agent.
The user will provide a paragraph describing a project idea.
Your task is to:
1. Extract key requirements and goals.
2. Identify the most suitable tech stack (frontend, backend, database, APIs).
3. Suggest an architecture (monolith, microservices, serverless, etc.).
4. Generate a project scaffold with folder structure and starter code snippets.
5. Provide setup instructions (dependencies, environment variables, build/run commands).

Output ONLY valid JSON with the following keys:
{
  "requirements": [...],
  "tech_stack": {...},
  "architecture": "...",
  "scaffold": {...},
  "setup_instructions": [...]
}
"""

def generate_project_spec(user_input: str) -> dict:
    response = client.chat.completions.create(
        model="gpt-5.1-codex-max",
        messages=[
            {"role": "system", "content": PROMPT_TEMPLATE},
            {"role": "user", "content": user_input}
        ],
        temperature=0
    )
    content = response.choices[0].message.content
    return json.loads(content)

