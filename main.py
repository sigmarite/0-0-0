from discord.ext.commands import Bot
from secrets import TOKEN

client = Bot(command_prefix="!")


@client.event
async def on_ready():
    print('Up and running')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f'Received from {message.author.name}: {message.content}')
    channel = message.channel

    await channel.send('Col cazzo, sacco di carne')

client.run(TOKEN)
