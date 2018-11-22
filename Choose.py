async def choose(a):
    b,c,d=a.split(" ")
        choices = [c,d]
        e = random.choice(choices)
        await garith.send_message(message.channel,'I choose *%s* ' % e)

