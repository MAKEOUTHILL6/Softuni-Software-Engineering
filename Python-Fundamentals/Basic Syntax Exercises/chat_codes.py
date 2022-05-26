def chat(chats):
    for i in range(chats):
        numbers = int(input())
        if numbers == 88:
            print("Hello")
        elif numbers == 86:
            print("How are you?")
        elif numbers != 86 and numbers != 88 and numbers < 88:
            print("GREAT!")
        else:
            print("Bye.")


chats = int(input())
chat(chats)