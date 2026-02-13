from tabulate import tabulate

def format_results(result):
    if "error" in result:
        return f" SQL Error: {result['error']}"

    rows = result["rows"]
    cols = result["columns"]

    if not rows:
        return "No results found."

    return tabulate(rows[:20], headers=cols, tablefmt="grid")
