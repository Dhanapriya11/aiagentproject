from agents import sql_agent

print("Text-to-SQL Agent")
print("Type 'exit' to stop.\n")

while True:
    question = input("Questions: ")

    if question.lower() == "exit":
        print("THANKS FOR THIS IS AGENT")
        break

    answer = sql_agent(question)
    print("\n" + answer + "\n")
