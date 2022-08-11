
from discord import Client 
from threading import Thread
from decouple import config
import asyncio


TOKEN= config('TOKEN')
ID_CHANNEL_PASSPORD=int(config('ID_CHANNEL_PASSPORD'))

class DiscordHost(Client):

    
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        channel  = self.get_channel(ID_CHANNEL_PASSPORD)
        #await channel.send('The bot is online ')


    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

    async def sendMessage(self, msg):
        channel = self.get_channel(ID_CHANNEL_PASSPORD)
        await channel.send(msg)

class ThreaderBot(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.loop = asyncio.get_event_loop()
        self.discord_client : DiscordHost 
        self.start()

    async def starter(self):
        print("starter")
        self.discord_client = DiscordHost()
        await self.discord_client.start(TOKEN)     

    async def sendMessaged(self, msg):
        channel = self.discord_client.get_channel(ID_CHANNEL_PASSPORD)
        await channel.send(msg) 

    def run(self):
        self.setName('Discord.py')
        self.loop.create_task(self.starter())
        self.loop.run_forever()
