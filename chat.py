import random

# Define a dictionary with some basic responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I assist you?"],
    "how are you": ["I'm doing great, thanks for asking!", "I'm just a bot, but I'm doing fine!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm not sure how to respond to that.", "Can you please rephrase?", "I'm here to help, ask me something else!"]
}

def chatbot_response(user_input):
    # Convert input to lowercase for matching
    user_input = user_input.lower()

    # Check if the input matches any of the keys in the responses dictionary
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    # Return default response if no match
    return random.choice(responses["default"])

def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye!")
            break
        
        # Get chatbot's response
        response = chatbot_response(user_input)
        print("Chatbot:", response)

# Start chatting
if __name__ == "__main__":
    chat()
