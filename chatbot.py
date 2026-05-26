def chatbot():
    print("===================================")
    print("      Welcome to Smart ChatBot")
    print("===================================")
    print("Type 'exit' anytime to stop chatting.\n")
    while True:
        user_input = input("You: ").lower()
        if user_input == "hello":
            print("Bot: Hey there! Nice to meet you.")
        elif user_input == "how are you":
            print("Bot: I'm doing great! Hope you're doing well too.")
        elif user_input == "what is your name":
            print("Bot: My name is SmartBot.")
        elif user_input == "bye":
            print("Bot: Goodbye! Have a wonderful day.")
            break
        elif user_input == "exit":
            print("Bot: Chat ended successfully.")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")
# Run chatbot
chatbot()