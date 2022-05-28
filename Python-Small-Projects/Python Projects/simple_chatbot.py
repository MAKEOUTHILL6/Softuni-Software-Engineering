from colorama import Fore, Back
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello, %2, how are you today?"]
    ],

    [
        r"(.*)what is my location?",
        ["your location is: Sofia, Bulgaria"]
    ],
    [
        r"(.*)what is python?",
        ["Python is an interpreted, object-oriented, high-level programming language with dynamic semantics"]
    ],
    [
        r"(iam|im|i'm) (.*)",
        ["Glad to hear that! How can I help you today?"]
    ],
    [
        r"(hi|hey|hello) (.*)",
        ["Hey", "Hello"]
    ],
    [
        r"quit",
        ["Bye for now see ya later! :)"]
    ],
    [
        r"(.*)",
        ["I am sorry, I don't think I understand your question, could you please try again?"]
    ]
]


print(Fore.RED + "")
print(f"Please type in lowercase English language to start a conversation with me! "
      f"Type quit to leave.")
print()
print("\033[0mHi, I am a chatbot created by Martin Atanasov! \nDo you mind telling me your name?")
chat = Chat(pairs, reflections)
chat.converse()