from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
import sys

class EnhancedChatBot:
    def __init__(self):
        try:
            # Create a new chatbot with a custom name
            self.chatbot = ChatBot(
                'MyBot',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                logic_adapters=[
                    'chatterbot.logic.BestMatch',
                    'chatterbot.logic.MathematicalEvaluation'
                ],
                database_uri='sqlite:///database.db'
            )
            
            # Create a new trainer for the chatbot
            self.trainer = ChatterBotCorpusTrainer(self.chatbot)
            
            # Train the chatbot on the English corpus
            print("Training the chatbot... This may take a few minutes.")
            self.trainer.train("chatterbot.corpus.english")
            print("Training completed!")
            
            # Initialize conversation context
            self.context = {
                'last_topic': None,
                'user_name': None,
                'greeting_done': False
            }
            
        except Exception as e:
            print(f"Error initializing chatbot: {str(e)}")
            sys.exit(1)

    def get_response(self, user_input):
        try:
            # Handle special commands
            if user_input.lower() == 'exit':
                return "Goodbye! Have a great day!"
            elif user_input.lower() == 'help':
                return self.get_help_message()
            elif user_input.lower().startswith('name:'):
                self.context['user_name'] = user_input[5:].strip()
                return f"Nice to meet you, {self.context['user_name']}!"
            
            # Get response from chatbot
            response = self.chatbot.get_response(user_input)
            
            # Add context awareness
            if not self.context['greeting_done'] and any(greeting in user_input.lower() for greeting in ['hi', 'hello', 'hey']):
                self.context['greeting_done'] = True
                if self.context['user_name']:
                    return f"Hello {self.context['user_name']}! How can I help you today?"
                return "Hello! I'm your friendly chatbot. What's your name? (Type 'name: YourName')"
            
            return str(response)
            
        except Exception as e:
            return f"I'm having trouble processing that. Could you rephrase? (Error: {str(e)})"

    def get_help_message(self):
        return """
Available commands:
- help: Show this help message
- exit: End the conversation
- name: YourName: Tell me your name
- You can also just chat normally with me!
        """

def main():
    print("Initializing the chatbot...")
    bot = EnhancedChatBot()
    
    print("\nWelcome to the Enhanced Chatbot!")
    print("Type 'help' to see available commands or 'exit' to quit.")
    print("----------------------------------------")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                print("Bot: I didn't catch that. Could you please say something?")
                continue
                
            response = bot.get_response(user_input)
            print("Bot:", response)
            
            if user_input.lower() == 'exit':
                break
                
        except KeyboardInterrupt:
            print("\nBot: Goodbye! Thanks for chatting!")
            break
        except Exception as e:
            print(f"Bot: Oops! Something went wrong: {str(e)}")
            print("Bot: Let's continue our conversation!")

if __name__ == "__main__":
    main()