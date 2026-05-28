# chatbot.py

print("🤖 AI Chatbot for FAQs (Type 'exit' to stop)\n")

faq = {
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is python": "Python is a programming language.",
    "what is ml": "ML stands for Machine Learning.",
    "hello": "Hi! How can I help you?",
    "how are you": "I'm just a program, but I'm doing great!"
}

while True:
    user = input("You: ").lower().strip()

    if user == "exit":
        print("Bot: Goodbye!")
        break

    answer = faq.get(user, "Sorry, I don't know the answer to that.")
    print("Bot:", answer)