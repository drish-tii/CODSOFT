# chatbot ai
def responses (ch):
    hi = {"hi", "hey","hello"}
    if ch.lower() in hi:
        print("Hello! How can I help you today?")
    elif ch.lower() == "how are you" or ch.lower() == "how are you?":
        print("I'm just a program, but I'm doing well. How can I help you?")
    elif ch.lower() == "what is your name" or ch.lower() == "what is your name?":
        print("I'm a chatbot created to assist you")
    elif ch.lower() == "help":
        print("Sure. Ask me anything!")
    else:
        print("Sorry I don't understand that")

print("Hii! Type bye to exit.")
while True:
    ch = input()
    if ch.lower()=="bye":
        print("GoodBye!")
        break
    else:
        responses(ch)
