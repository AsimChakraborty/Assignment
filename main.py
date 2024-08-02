from autogen_agent import fetch_wikipedia_content, QnAAgent

def main():
    url = "https://en.wikipedia.org/wiki/Bangladesh"
    content = fetch_wikipedia_content(url)
    
    # Initialize QnA agent with the content
    agent = QnAAgent(content)
    
    # Sample questions
    questions = [
        "What is the capital of Bangladesh?",
        "What is the population of Bangladesh?",
        "Describe the culture of Bangladesh.",
        "What is the official name of Bangladesh?.",
        "What are the official and widely used languages in Bangladesh?",
        "Which countries share land borders with Bangladesh?"
    ]
    
    # Answer the questions
    for question in questions:
        answer = agent.answer_question(question)
        print(f"Q: {question}")
        print(f"A: {answer}\n")

if __name__ == "__main__":
    main()

#using spacy

# from autogen_agent import fetch_wikipedia_content, QnAAgent

# def main():
#     url = "https://en.wikipedia.org/wiki/Bangladesh"
#     content = fetch_wikipedia_content(url)
    
#     # Initialize QnA agent with the content
#     agent = QnAAgent(content)
    
#     # Sample questions
#     questions = [
#         "What is the capital of Bangladesh?",
#         "What is the population of Bangladesh?",
#         "Describe the culture of Bangladesh.",
#         "What is the official name of Bangladesh?",
#         "What are the official and widely used languages in Bangladesh?",
#         "Which countries share land borders with Bangladesh?"
#     ]
    
#     # Answer the questions
#     for question in questions:
#         answer = agent.answer_question(question)
#         print(f"Q: {question}")
#         print(f"A: {answer}\n")

# if __name__ == "__main__":
#     main()
