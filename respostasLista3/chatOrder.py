quantidade = int(input())
chats = {}

for _ in range(quantidade):
    chat = input()
    if chat in chats:
        del chats[chat]
    chats[chat] = None

for chat in reversed(chats):
    print(chat)

