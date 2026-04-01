print("Hello! I am your AI Assistant. Type 'exit' to quit.")

while True:
    user = input("You: ").lower()

    if user == "okey bye":
        print("Bot: Goodbye!")
        break

    elif "hello" in user:
        print("Bot: Hello! How can I help you?")

    elif "ai" in user:
        print("Bot: AI stands for Artificial Intelligence.")

    elif "course" in user:
        print("Bot: This course is about Programming for AI.")

    elif "help me" in user:
        print("Bot: I can answer questions about AI or your course.")


    elif"what is AI in simple terms" in user:
        print("Bot: AI is like teaching a computer to think and learn like a human.")
    elif"what are the branches of AI"in user:
        print("Bot: The branches of AI include Machine Learning, Natural Language Processing, Computer Vision, and Robotics.")
    elif "whats the difference between AI and machine learning" in user:
        print("Bot: AI is the broader concept of machines being able to carry out tasks in a way that we would consider smart, while Machine Learning is a specific subset of AI that involves training algorithms to learn from data.")

    elif "thank you" in user:
        print("Bot: You're welcome! If you have any more questions, feel free to ask.")

    else:
        print("Bot: I'm sorry, I don't understand that. Can you please rephrase?")