def validate_sql(query: str):
    blocked = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER"]
    upper_query = query.upper()

    for word in blocked:
        if word in upper_query:
            return False, f"Blocked keyword found: {word}"

    if "SELECT" not in upper_query:
        return False, "Only SELECT queries are allowed"

    return True, "Valid SQL"
