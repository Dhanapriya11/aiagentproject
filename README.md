SQL Music Store Agent Challenge: Project Requirement Document

Problem Statement
Natural language interfaces to databases are becoming increasingly important as organizations want to democratize data access. In this project, your task is to build an AI agent that can answer natural language questions about a music store database by generating and executing SQL queries.
This is a Text-to-SQL agent challenge where you will build an intelligent system that understands database schema, generates appropriate queries, and presents results in a human-readable format.
Your goal is to: - Build an AI agent that converts natural language to SQL - Execute queries against a SQLite database - Demonstrate understanding of agent architecture, tool use, and prompt engineering
Dataset Information:   Chinook Sqlite dataset:
 This project is an AI-based Text-to-SQL agent using the Chinook SQLite music store database. The user gives a question in normal English, like “List all albums by AC/DC”. The agent reads the database schema to understand the tables and columns, then uses an OpenAI LLM (gpt-4o-mini) to convert the question into an SQL query. After generating the SQL, the agent validates it to make sure it is safe and correct, then executes it on the SQLite database. Finally, the output is formatted into a readable table and the agent returns the answer to the user in a simple format.

