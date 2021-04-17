import conf
import discord
from discord.ext import commands
import os
import img_handler as imhl
from discord.ext import commands
# intense = discord.Intents.default()
# intense.members = True

# client = discord.Client(intents = intense)

# @client.event
# async def on_message(message):
# # <Message 
# # id=825338226058461184 
# # channel=<TextChannel id=822806350886207542 name='флудильня' position=0 nsfw=False news=False category_id=822806350886207539>
# # type=<MessageType.default: 0>
# # author=<Member id=459312368321691660 name='Twinkle | J4F' discriminator='2408' bot=False nick=None guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=29>>
# # flags=<MessageFlags value=0>>

#     if message.author == client.user:
#         return

#     #Проверка на дурака №2 - Отправитель чужой бот

#     if message.author.bot:
#         return

#     #Задаем каналы для бота
#     if message.channel.id == 825339462707052554:
#         #Ответ пользователю в формате "Hello, {user.name} - your message {user.content}"
#         msg = None

#     # 'Hello, {message.author.name}! - your message {message.content}'
#     #     await message.channel.send(msg)

#         ctx = message.content.split(" ", maxsplit=1)

#         if message.content == "/hello":
#             msg = f"Hello, {message.author.name}. I am {client.user.name}"
        
#         elif message.content == "/about_me":
#             msg = f"Your name is {message.author.name}, your id is {message.author.id}"
#             if message.author.nick:
#                 msg = "and your nickname is {author.user.nick}"
        
#         elif ctx[0] == "/repeat":
#             msg = ctx[1]    
        
#         elif message.content == "/get_members":
#             msg = ""
#             if message.author.guild.name == "Bots":
#                 for idx, member in list(enumerate(message.author.guild.members)):
#                     msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else "" } - {member.id}\n' 
        
#         elif message.content == "/get_member" and ({client.user.name} or {client.user.id}):
#             msg = f'User's name is {client.user.name}'  
#         if message.author.nick:
#             msg = f'and Users's nick is {client.user.id}'
#         elif message.content == "/get_member" and " ":
#             msg = f'Enter User's name is {client.user.name}'

#         elif message.content == "/get_channels":
#             msg = ""
        



# # Отправляем сообщение если оно есть
#         if msg != None:
#             await message.channel.send(msg)

# client.run(conf.bot_token)
intense = discord.Intents.default()
intense.members = True

bot = commands.Bot(command_prefix="!", intents = intense)

channel = 825339462707052554

@bot.command(name = "get_member")
async def get_member(ctx, member:discord.Member = None):
    msg = None
    global channel
    if ctx.channel.id == channel:
       
        if member:
            msg = f'Member {member.name}{"({member.nick})" if member.nick else " "} - {member.id}'

        if msg == None:
            msg = "error"
            
            
        await ctx.channel.send(msg)

@bot.command(name = "mk")
async def mk(ctx, f1:discord.Member = None, f2:discord.Member = bot.user):
    msg = None
    global channel
    if ctx.channel.id == channel:
        if f1 and f2:
            await imhl.vs_create(f1.avatar_url, f2.avatar_url)
            await ctx.channel.send(file =discord.File(os.path.join("./img/result.png")))

bot.run(conf.bot_token)