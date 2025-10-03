import random

# Predefined rules with multiple possible responses
rules = {
    "hello": ["Hello! How can I assist you today?", "Hi there! How’s it going?", "Hey! Glad to see you."],
    "hi": ["Hi! What can I do for you?", "Hello! How’s your day?", "Hey there!"],
    "how are you": ["I'm doing great! How about you?", "All good here. How are you doing?", "I’m just a bot, but I feel awesome!"],
    "your name": ["I'm a rule-based chatbot created as part of an internship task.", "You can call me InternshipBot.", "My name doesn’t matter, I’m here to help you!"],
    "weather": ["I can’t check live weather, but I hope it’s sunny where you are.", "Not sure about the weather, but it’s always a good day to code.", "Weather data isn’t my thing, but I hope it’s pleasant!"],
    "bye": ["Goodbye! Have a wonderful day.", "See you later!", "Bye! Take care."],
    "help": ["Try commands like 'hello', 'how are you', 'weather', 'your name'.", "You can ask me things like greetings, weather, or about me.", "Need help? Try typing: hello, hi, your name, weather, bye."]
}


def chatbot_response(user_input: str) -> str:
    """
    Generates a chatbot response based on exact or partial matches.
    
    Parameters:
        user_input (str): The user's message.
    
    Returns:
        str: Chatbot's response.
    """
    user_input = user_input.lower().strip()

    # Exact match
    if user_input in rules:
        return random.choice(rules[user_input])

    # Partial match (keyword inside user input)
    for key in rules:
        if key in user_input:
            return random.choice(rules[key])

    # Default response if no rule matches
    return "I'm not sure I understand. Type 'help' to see what I can do."


def main():
    """
    Main loop to run the chatbot.
    """
    print("Internship Chatbot is ready! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        # Exit condition
        if user_input.lower().strip() == "bye":
            break


# Run the chatbot
if __name__ == "__main__":
    main()
