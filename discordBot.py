
from discord import Client 
from threading import Thread
from decouple import config
import asyncio


TOKEN= config('TOKEN')
ID_CHANNEL_PASSWORD=int(config('ID_CHANNEL_PASSWORD'))

class DiscordHost(Client):

    
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print('------')
      
        #await channel.send('The bot is online ')


    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

    async def sendMessage(self, msg: str):
        channel = self.get_channel(ID_CHANNEL_PASSWORD)
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

    async def sendMessage(self, msg: str):
        channel = self.discord_client.get_channel(ID_CHANNEL_PASSWORD)
        await channel.send(msg) 

    def run(self):
        self.setName('Discord.py')
        self.loop.create_task(self.starter())
        self.loop.run_forever()
    
    def stop(self):
        #self.discord_client.close()
        self.loop.stop()
