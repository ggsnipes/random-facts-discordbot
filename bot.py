import discord
    
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'logged on as {self.user}')


    async def on_message(self, message):
        pring(f'message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))
