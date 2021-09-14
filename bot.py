import discord, sys

def load(file):
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read()
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
              file=sys.stderr)
        sys.exit(1)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if (message.author.name == 'Czechbox'):
            await message.channel.send("cringe")

client = MyClient()
client.run(load('token.txt'))