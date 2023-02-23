import random

def unknown():
    custom_messages = [
        "I don't understand you",
        "Could you please rephrase that?",
        "...",
        "Not sure I get that"
        "Come again?",
    ]

    return custom_messages[random.randrange(0, len(custom_messages))]

R_EATING = "I'm a bot so I don't eat"
