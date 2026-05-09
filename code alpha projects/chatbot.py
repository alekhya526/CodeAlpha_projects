import random
import datetime

def get_response(user_input, memory):
    user_input = user_input.lower()

    # Greeting
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return random.choice([
            "Hey there! 😊",
            "Hello! How can I help you?",
            "Hi! Nice to talk to you!"
        ])

    # Ask name
    elif "my name is" in user_input:
        name = user_input.split("my name is")[-1].strip().title()
        memory["name"] = name
        return f"Nice to meet you, {name}! 💙"

    elif "what is my name" in user_input:
        return f"Your name is {memory.get('name', 'unknown 😅')}"

    # How are you
    elif "how are you" in user_input:
        return random.choice([
            "I'm doing great! 🤖",
            "All good here! Thanks for asking 😊",
            "Feeling smart today 😎"
        ])

    # Time
    elif "time" in user_input:
        return "Current time is: " + datetime.datetime.now().strftime("%H:%M:%S")

    # Date
    elif "date" in user_input:
        return "Today's date is: " + datetime.datetime.now().strftime("%Y-%m-%d")

    # Simple math
    elif "calculate" in user_input:
        try:
            expression = user_input.replace("calculate", "")
            result = eval(expression)
            return f"Result: {result}"
        except:
            return "Sorry, I couldn't calculate that 😅"

    # Joke
    elif "joke" in user_input:
        return random.choice([
            "Why did Python go to school? To become smarter! 😂",
            "I told my computer I needed a break… it said no problem – it froze 😆",
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"
        ])

    # Help
    elif "help" in user_input:
        return (
            "I can help with:\n"
            "- Greetings\n"
            "- Tell time/date\n"
            "- Simple calculations (type: calculate 2+2)\n"
            "- Tell jokes\n"
            "- Remember your name"
        )

    # Exit
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day 👋"

    else:
        return "Hmm... I didn't understand that. Try 'help' 😊"


def chatbot():
    print("🤖 Advanced Chatbot Started!")
    print("Type 'help' to see what I can do.\n")

    memory = {}

    while True:
        user_input = input("You: ")
        response = get_response(user_input, memory)
        print("Bot:", response)

        if user_input.lower() in ["bye", "exit", "quit"]:
            break


chatbot()