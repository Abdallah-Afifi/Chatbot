import random

def simple_chatbot(user_input):
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey!"],
        "how are you": ["I'm doing well, thank you!", "I'm fine, how about you?", "All good!"],
        "bye": ["Goodbye!", "See you later!", "Bye!"],
        "default": ["I'm not sure how to respond to that.", "Could you please rephrase?", "I didn't understand that."]
    }

    user_input_lower = user_input.lower()

    for pattern, response_list in responses.items():
        if pattern in user_input_lower:
            return random.choice(response_list)

    return random.choice(responses["default"])

def main():
    print("Welcome to the Simple Chatbot!")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye! Exiting the chatbot.")
            break

        bot_response = simple_chatbot(user_input)
        print("Chatbot:", bot_response)

if __name__ == "__main__":
    main()
