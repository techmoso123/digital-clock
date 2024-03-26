from nltk.chat.util import Chat, reflections

pairs =[
    [
      r"hello|hi|Hello|Hi",
        ["hey! how are you","Hi","Good day"]
      
    ],
    [
        "Am fine, you?|Good , how are you too|How are you|how was your day",
        ["Doing well", "Am fine","Great"]

    ]
]

chatbot = Chat(pairs, reflections)

def myChatbot  ():
    userName=input("what is your name: ")
    print(f"welcome {userName}")

    while True:
         userInput = input(F"{userName}:")

         response = chatbot.respond(userInput)
         print(f"mona: {response}")
    
    if userInput=="ok, bye" or "bye" or"Bye":
        print(f"Bot: Goodbye{userName}")
        exit()
if "__main__"==__name__:
    myChatbot()   