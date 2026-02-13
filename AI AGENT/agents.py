from openai import OpenAI
from tools.get_schema import get_schema
from tools.execute_sql import execute_sql
from tools.validate_sql import validate_sql
from tools.format_sql import format_results

OpenAI(api_key="AIzaSyBKVQeXfyzZ6hWwkshJuLuvSkO9jJWq9gE")

def sql_agent(question: str):
    schema = get_schema()

    prompt = f"""
You are an expert SQLite SQL assistant.

Database schema:
{schema}
Task:
Convert the user question into a valid SQL query.
Rules:
- Use only tables and columns from schema.
- Only generate SELECT queries.
- Do not explain anything.
- Output ONLY SQL query.
User Question:
{question}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    sql_query = response.choices[0].message.content.strip()

    valid, msg = validate_sql(sql_query)
    if not valid:
        return f"Invalid SQL generated.\nReason: {msg}\n\nSQL:\n{sql_query}"

    result = execute_sql(sql_query)
    formatted_result = format_results(result)

    return f"SQL Query:\n{sql_query}\n\n Result:\n{formatted_result}"
