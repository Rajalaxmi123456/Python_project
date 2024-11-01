def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm doing well! How about you?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "name" in user_input:
        return "I'm your friendly chatbot!"
    else:
        return "I'm sorry, I didn't understand that. Could you rephrase?"

def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot:", chatbot_response(user_input))

if __name__ == "__main__":
    chat()