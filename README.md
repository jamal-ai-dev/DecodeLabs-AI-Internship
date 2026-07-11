# AI Chatbot — Rule-Based Chatbot (Project 1)

## Description
A simple rule-based chatbot built in Python as part of the DecodeLabs AI Internship (Week 1, Project 1). The chatbot uses a dictionary-based knowledge base to match predefined user inputs and respond accordingly. It runs in a continuous loop, sanitizes user input (case-insensitive, whitespace-trimmed), provides a fallback response for unrecognized input, and exits cleanly on commands like `exit`, `quit`, or `bye`.

This project focuses on foundational programming concepts — control flow, decision-making logic, and dictionary lookups — as a precursor to more advanced AI systems.

## Features
- Handles greetings (`hello`, `hi`, `hey`)
- Answers simple predefined questions (name, purpose, help)
- Case-insensitive and whitespace-tolerant input handling
- Default fallback response for unrecognized input
- Clean exit via `exit`, `quit`, `bye`, or `goodbye`

## How to Run
1. Make sure Python 3 is installed:
   ```bash
   python --version
   ```
2. Clone or download this repository.
3. Navigate to the project folder:
   ```bash
   cd Project1-RuleBasedChatbot
   ```
4. Run the chatbot:
   ```bash
   python rule_based_chatbot.py
   ```
5. Start chatting! Try `hello`, `help`, `what is your name`, or `bye` to exit.

## Example
```
Bot: Hello! I'm DecodeBot. Type 'exit' or 'bye' anytime to leave.
You: hello
Bot: Hi there! How can I help you today?
You: what is your name
Bot: I'm DecodeBot, your rule-based assistant.
You: bye
Bot: Goodbye! 👋
```

## Tech Stack
- Python 3 (standard library only, no external dependencies)

## Author
DecodeLabs AI Internship — Batch 2026