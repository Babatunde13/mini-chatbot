import os, re, long_responses as lr

def get_user_name():
    name = input("Welcome 👋, to get started let me know what is your name is: ")
    return name

def get_user_input(name):
    user_input = input(f"{name}: ")
    return user_input

def isQuitInput(user_input):
    if user_input.lower() == "quit" or user_input.lower() == "exit" or user_input.lower() == "q":
        return True
    return False

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_word = True
    
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1
    
    probability = float(message_certainty) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_word = False
            break
    
    if has_required_word or single_response:
            return int(probability * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_map = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_map
        highest_prob_map[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    
    response("Hello, how are you?", ["hello", "hi", "hey", "What's up"], single_response=True)
    response("I am good, how are you?", ["how", "are", "you"], required_words=["how", "are", "you"])
    response("Bye, Thank you!", ["thank", "thanks", "bye"], single_response=True, required_words=["thank"])
    response(lr.R_EATING, ["eat", "food", "hungry"], single_response=True, required_words=["eat", "you"])

    highest_prob = max(highest_prob_map, key=highest_prob_map.get)

    return lr.unknown() if highest_prob_map[highest_prob] < 1 else highest_prob
        

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    return check_all_messages(split_message)

def main():
    name = get_user_name()
    print("Enter any message to start the chat, or enter 'quit' to exit the chat")
    while True:
        user_input = get_user_input(name)
        if isQuitInput(user_input):
            print("Bot: bye 👋")
            break
        print(f"Bot: {get_response(user_input)}")

if __name__ == "__main__":
    main()
