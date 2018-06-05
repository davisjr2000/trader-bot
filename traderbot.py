import discord
import random
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Trader is ready!")
    await client.change_presence(game=discord.Game(name="Flappy Catito"))
  
    
@client.event
async def on_message(message):
    userID = message.author.id
    if message.content.upper() == "ALE":
        await client.send_message(message.channel, "esse é niilista")
    if message.content.upper() =="ALE É MÓ...":
        await client.send_message(message.channel, "...niilista")
    if message.content =="ale e mo...":
        await client.send_message(message.channel, "...niilista")
    if message.content =="ale é mo...":
        await client.send_message(message.channel, "...niilista")
    if message.content =="ale eh mó...":
        await client.send_message(message.channel, "...niilista")
    if message.content =="ale eh moh...":
        await client.send_message(message.channel, "...niilista")
    if message.content =="ale eh mo...":
        await client.send_message(message.channel, "...niilista")
    if message.content =="qual o melhor jogo do mundo":
        await client.send_message(message.channel, "flappy catito")
    if message.content.upper() =="MDS":
        await client.send_message(message.channel, "<@%s> chamou?" % (userID))
    if message.content.upper() =="VLW":
        await client.send_message(message.channel, "rlx qqlr coisa to aqui")
    if message.content =="cade seu filho?":
        await client.send_message(message.channel, "ta batendo punheta la em cima")
    if message.content.upper() =="CADE LR?":
        await client.send_message(message.channel, "pergunta pra porra do guincho")
    if message.content.upper() =="Q":
        await client.send_message(message.channel, "q oq caralho")
    if message.content.upper() =="KK":
        await client.send_message(message.channel, "obrigado por rir")
    if message.content.upper() =="CUCK":
        await client.send_message(message.channel, "ó o ale ai")
    if message.content.upper() =="KCT":
        await client.send_message(message.channel, "no seu cu arrombado")
    if message.content.upper().startswith =="ahn":
        await client.send_message(message.channel, "para c essa bosta de 'ahn'")
    if message.content.upper() =="GRR":
        await client.send_message(message.channel, "miau")
    if message.content.upper() =="PERAE":
        await client.send_message(message.channel, "to perando kk")
    if message.content.upper() =="EAE":
        await client.send_message(message.channel, "<@%s> eae bro" % (userID))
    if message.content =="catito":
        await client.send_message(message.channel, "ah n")
    if message.content =="trader":
        await client.send_message(message.channel, "fala")
    if message.content.upper() =="PO":
        await client.send_message(message.channel, "adoro kung fu panda")
    if message.content =="porra":
        await client.send_message(message.channel, "tudo isso")
    if message.content =="porr":
        await client.send_message(message.channel, "tudo isso")
    if message.content =="davis":
        await client.send_message(message.channel, "meu criador")
    if message.content =="gru":
        await client.send_message(message.channel, "gru dudu e seu cu")
    if message.content =="vini":
        await client.send_message(message.channel, "outro niilista")
    if message.content =="dominions 4":
        await client.send_message(message.channel, "meu filho n para de falar dessa bosta")
    if message.content =="equador":
        await client.send_message(message.channel, "nem foi tao bom assim")
    if message.content =="sdds da morena?":
        await client.send_message(message.channel, "demais")
    if message.content =="o creme e de la quem?":
        await client.send_message(message.channel, "do ale porra")
    if message.content =="miguelvin ou melguel?":
        await client.send_message(message.channel, "<@%s> precisa de alguém rápido ou forte?" % (userID))
    if message.content =="forte":
        await client.send_message(message.channel, "melguel")
    if message.content =="rápido":
        await client.send_message(message.channel, "miguelvin")
    if message.content =="rapido":
        await client.send_message(message.channel, "miguelvin")
    if message.content =="sente sdds do catito?":
        await client.send_message(message.channel, "o do arqui ou o flappy?")
    if message.content =="arqui":
        await client.send_message(message.channel, "espero q morra")
    if message.content =="flappy":
        await client.send_message(message.channel, "esse sim, jogo do ano")
    if message.content.upper() =="UE":
        await client.send_message(message.channel, "ue oq? quer que eu desenhe pra vc?")
    if message.content =="@everyone":
        await client.send_message(message.channel, "geral cola aqui")
    if message.content =="tetinhas":
        await client.send_message(message.channel, "esse é o amigo bundudo do ale ne")
    if message.content =="esquilo":
        await client.send_message(message.channel, "esse menino é aquela lenda urbana de guarulhos ne filhao?")
    if message.content =="andre":
        await client.send_message(message.channel, "esse que gosta de pewdiepie ne ale")
    if message.content =="luan":
        await client.send_message(message.channel, "adoro a série desse menino")
    if message.content =="fortnite":
        await client.send_message(message.channel, "ainda bem que o ale n joga isso")
    if message.content =="flavio":
        await client.send_message(message.channel, "pernambucano do inferno") 
    if message.content =="guincho":
        await client.send_message(message.channel, "esse devia ta fznd LR mas fica o dia inteiro coçando o saco")
    if message.content =="ricardo":
        await client.send_message(message.channel, "faz uma webnamorada no python p mim pfvr")
    if message.content =="bolinho tetinhas":
        await client.send_message(message.channel, "esse foi feito na unha")
    if message.content =="péter":
        await client.send_message(message.channel, ":moyai:")
    if message.content =="peter":
        await client.send_message(message.channel, ":moyai:")
    if message.content =="=m p toto africa":
        await client.send_message(message.channel, "nossa toto africa mto bom")
    if message.content.upper() =="RIP":
        await client.send_message(message.channel, "=f pipi") 
    if message.content.upper() =="EU SOQUEI UM HATER NO SHOPPING":
        await client.send_message(message.channel, "QUE FALOU BOSTA") 
    if message.content.upper() =="ÓCULOS DO KURT COBAIN":
        await client.send_message(message.channel, "Double cup, Sprite, Codein")
    if message.content.upper() =="PQP":
        await client.send_message(message.channel, "Language.")
    if message.content.upper() =="RAFFA MOREIRA":
        number=random.randint(0,9)
        lista=[0,1,2]
        lista2=[3,4,5]
        lista3=[6,7]
        lista4=[8,9]
        if number in lista:
            await client.send_message(message.channel, "MIXTAPE MANO")
        if number in lista2:
            await client.send_message(message.channel, "BRO FAZ SOL")
        if number in lista3:
            await client.send_message(message.channel, "gang gang")
        if number in lista3:
            await client.send_message(message.channel, "vc e branco bro")
    if message.content =="=m s":
        number=random.randint(0,9)
        lista=[1,2,3]
        if number in lista:
           await client.send_message(message.channel, "nao porra mo foda a musica")
    if message.content.upper() =="VSF":
        await client.send_message(message.channel, "<@%s> vai vc" % (userID))
    if message.content.upper() =="MAS LITTLE.":
        await client.send_message(message.channel, "Mas <@%s>." % (userID))
    if message.author.id =="143607024087859200":
        number=random.randint(0,9)
        lista=[1,2]
        if number in lista:
           await client.send_message(message.channel, "para de falar merda catito")
    if message.author.id =="307282841501171712":
        number=random.randint(0,9)
        lista=[1,2,3]
        if number in lista:
           await client.send_message(message.channel, "mas little.")
    if message.author.id =="216660094048403457":
        number=random.randint(0,9)
        lista=[1,2]
        if number in lista:
           await client.send_message(message.channel, "caralho esse pernumbucano branco é uma máquina de fala merda")
    if message.author.id =="294968198535577600":
        number=random.randint(0,9)
        lista=[1,2]
        if number in lista:
           await client.send_message(message.channel, "harhar")
    if message.author.id =="325407029382348801":
        number=random.randint(0,99)
        lista=[24]
        lista2=[1,2,3,4,5]
        if number in lista:
           await client.send_message(message.channel, "Testando o ovo do Ale.")
        elif number in lista2:
           await client.send_message(message.channel, "Nada importa msm")
    if message.content.upper().startswith('!TRADER SAY'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[2:])))
    if message.content.upper().startswith('QUAL O FRENE?'):
        memes = message.content.split(" ")
        if 'Catito' in memes or 'catito' in memes or 'CATITO' in memes:
            await client.send_message(message.channel, "Catito")
        else:
            size=len(memes)
            frene1=random.randint(3,size)
            await client.send_message(message.channel, "%s" % ("".join(memes[frene1])))
       
                
                


client.run("NDMxOTk5NjMxMTIwMTM4MjQw.DasiAw.0hlUP5MbyeuWE_WuF6dVY0xjHa4")
client.login(process.env.BOT_TOKEN)
