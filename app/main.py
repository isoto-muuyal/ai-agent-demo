from app.agent import create_agent

if __name__ == "__main__":
    agent = create_agent()
    result = agent.run("multiply 5 and 6")
    print(result)