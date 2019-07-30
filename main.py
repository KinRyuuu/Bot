import discord
from datetime import date
import spoilerminesweeper

MIN_YEAR = 2010
MAX_YEAR = date.today().year+1

messages = {
    'welcome':'Welcome to the official Discord server for computing at the University of Glasgow! Before you can start chatting, please reply to this message with your starting year.',
    'invalid':f"Invalid year, please make sure that your starting year is between {MIN_YEAR} and {MAX_YEAR}. If you're having any issues, please DM a member of staff in the Discord server.",
    'role':'You already have a role.',
    'success':'You have been given the role `{0}`. Please read #welcome and #rules before you start chatting!'
}

class MyClient(discord.Client):
    async def on_member_join(self, member):
        await member.send(messages['welcome'])

    async def on_message(self, message):
        if message.channel.type == discord.ChannelType.private and message.author != self.user:
            try:
                year = int(message.content)
                if year < MIN_YEAR or year > MAX_YEAR:
                    await message.channel.send(messages['invalid'])
                else:
                    guild = self.get_guild(553638026618601488)
                    member = guild.get_member(message.author.id)
                    for role in guild.roles:
                        if role.name == str(year):
                            if len(member.roles) == 1:
                                student_role = guild.get_role(602573138475220996)
                                await member.add_roles(student_role)
                                await member.add_roles(role)
                                await message.channel.send(messages['success'].format(year))
                            else:
                                await message.channel.send(messages['role'])
            except Exception:
                await message.channel.send(messages['invalid'])

        if "minesweeper" in message:
            await message.channel.send(spoilerminesweeper.getBoard(10, 5))
client = MyClient()
client.run('token here')
