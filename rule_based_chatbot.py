"""
DecodeLabs AI Internship - Project 1
Rule-Based AI Chatbot

Goal: A simple chatbot that responds to predefined user inputs using
a dictionary-based knowledge base (instead of a long if-elif ladder),
runs in a continuous loop, and exits cleanly on command.
"""

# -----------------------------
# 1. KNOWLEDGE BASE
# -----------------------------
# Dictionary = O(1) lookup instead of O(n) if-elif chain.
# Add as many intents as you like -- this is your "vocabulary".
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "hey": "Hey! Good to see you.",
    "how are you": "I'm just code, but I'm running smoothly!",
    "what is your name": "I'm DecodeBot, your rule-based assistant.",
    "who made you": "I was built during the DecodeLabs AI internship.",
    "help": "I can respond to greetings and a few simple questions. Try 'hello', 'help', or 'what is your name'.",
    "thanks": "You're welcome!",
    "thank you": "Anytime!",
}

# Words that will end the conversation
EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye"}


def get_response(user_input: str) -> str:
    """
    Look up a cleaned user input in the knowledge base.
    Falls back to a default message if no match is found.
    """
    return responses.get(user_input, "I do not understand that yet. Try typing 'help'.")


def sanitize(raw_text: str) -> str:
    """
    Normalize user input: lowercase + strip leading/trailing whitespace.
    This ensures 'Hello', 'hello ', and 'HELLO' all match the same key.
    """
    return raw_text.lower().strip()


def run_chatbot():
    print("Bot: Hello! I'm DecodeBot. Type 'exit' or 'bye' anytime to leave.")

    # 2. THE INFINITE LOOP (the "heartbeat")
    while True:
        raw_input_text = input("You: ")
        clean_input = sanitize(raw_input_text)

        # 3. EXIT STRATEGY
        if clean_input in EXIT_COMMANDS:
            print("Bot: Goodbye! 👋")
            break

        # Skip empty input instead of showing "I don't understand"
        if clean_input == "":
            continue

        # 4. RESPONSE LOOKUP + FALLBACK
        reply = get_response(clean_input)
        print(f"Bot: {reply}")


if __name__ == "__main__":
    run_chatbot()