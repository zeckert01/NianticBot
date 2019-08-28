import discord
from discord.ext import commands
from datetime import datetime
from lib.common import make_selection
from lib.ocr import getTeam
import urllib

class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel = 488153124633182219

    @commands.Cog.listener()
    async def on_message(self, message):
        if(message.author.id != self.bot.user.id and message.channel.id  == self.channel):
            if(len(message.attachments) > 0):
                for i in message.attachments:
                    await i.save("temp.png")
                try:
                    res = getTeam("temp.png")

                    POSSIBLE = [488146122091528194, 488146121886138369, 488146121613508608, 519304919631527956]

                    for j in message.author.roles:
                        if j.id in POSSIBLE:
                            await message.channel.send("You've been assigned already.\nTalk to a mod about getting your role changed...")
                            return

                    newRole = None
                    if res == 'instinct':
                        newRole = 488146122091528194
                    elif res == 'valor':
                        newRole = 488146121886138369
                    elif res == 'mystic':
                        newRole = 488146121613508608
                    else:
                        await message.channel.send("I'm sorry... couldn't determine your team")

                    rol = message.guild.get_role(newRole)
                    await message.author.add_roles(rol)
                    await message.channel.send("Welcome {} to team {}!".format(message.author.mention, res))
                    await message.delete()
                except Exception as e:
                    print(e)
                    mod = message.guild.get_role(488160235085889537)
                    await message.channel.send("Sorry... I had some issues")
                    await message.channel.send("Could a {} please help me out?".format(mod.mention))

        elif(self.bot.user.mentioned_in(message) and message.author != self.bot.user and not message.mention_everyone):
            await message.channel.send('¯\_(ツ)_/¯')
def setup(bot):
    bot.add_cog(Verification(bot))
