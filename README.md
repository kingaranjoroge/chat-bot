# Enhanced Python Chatbot

A simple yet powerful chatbot built with Python using the ChatterBot library. This chatbot features context awareness, mathematical capabilities, and a user-friendly interface.

## Features

- 🤖 Natural language processing using ChatterBot
- 📝 Context awareness (remembers user's name and conversation state)
- 🔢 Mathematical evaluation capabilities
- 💬 Interactive command system
- ⚡ Error handling and graceful recovery
- 🎯 Simple and intuitive user interface

## Prerequisites

Before running the chatbot, make sure you have the following installed:

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the source code.

2. Install the required packages:
```bash
pip install chatterbot
pip install chatterbot-corpus
python -m spacy download en_core_web_sm
```

## Usage

1. Run the chatbot:
```bash
python chatbot.py
```

2. Available Commands:
- `help`: Display available commands
- `exit`: End the conversation
- `name: YourName`: Set your name for personalized responses

3. Example Interactions:
```
You: help
Bot: [Displays available commands]

You: name: John
Bot: Nice to meet you, John!

You: What is 2 + 2?
Bot: The answer is 4

You: Hello
Bot: Hello John! How can I help you today?
```

## Project Structure

- `chatbot.py`: Main chatbot implementation
- `database.db`: SQLite database for storing conversation data (created automatically)

## Features in Detail

### Context Awareness
- Remembers user's name throughout the conversation.
- Tracks greeting state.
- Maintains conversation context.

### Error Handling
- Graceful handling of invalid inputs.
- Recovery from unexpected errors.
- Keyboard interrupt handling (Ctrl+C).

### Mathematical Capabilities
- Basic arithmetic operations
- Mathematical expression evaluation

## Contributing

Feel free to contribute to this project by:
1. Forking the repository.
2. Creating a new branch.
3. Making your changes.
4. Submitting a pull request.
