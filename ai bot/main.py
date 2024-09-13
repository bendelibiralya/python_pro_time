import discord
from discord.ext import commands
from bot_token import token
from detect_class import detect_hp


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def image(ctx):
    if ctx.message.attachments:
        await ctx.send(f'ok im detecting!')
        for attachement in ctx.message.attachments:
            file_name = attachement.filename
            file_path = f"images/{file_name}"
            await attachement.save(file_path)
            await ctx.send("done!!")
            name, score = detect_hp("converted_keras/keras_model.h5", "converted_keras/labels.txt", file_path)
            #name, score = ("Buckbeak",99)
            await ctx.send(f"Bu {name.strip()}, bundan %{int(score*100)} eminim.")
            if name.strip() == "Buckbeak":
                await ctx.send("""Buckbeak is a male hippogriff. He lived with Hagrid during Harry's third year. He was later sentenced to death when he attacked Draco Malfoy after being taunted and provoked. With the help of Harry, Hermione and her Time-Turner he escaped execution and became under the care of Sirius Black.
★ Buckbeak is very loyal and protective of those who treat him with kindness and respect.
★ After Sirius's death Buckbeak came to be owned by Harry and he showed great affection and loyalty toward Harry, defending him whenever he was in danger.""")
            elif name.strip() == "Basiliks":
                await ctx.send("""The Basilisk was a giant serpent magical beast, also known as the King of Serpents. Looking a Basilisk directly in the eye caused instant death, but an indirect look would merely render the victim petrified. 
★ Basilisk is the mortal enemy of spiders. Spiders refused to speak of the Basilisk, could intuitively sense their presence, and would flee whenever they sensed them.
★ It also is a known wizard-killer that couldn't be domesticated due to its immense powers. However, since the Basilisk was still a serpent, a Parselmouth might communicate with it and potentially place the creature under their influence. 
★ The basilisk we saw in the Chamber of Secrets was The Serpent of Slytherin. She was placed in the Chamber of Secrets by Salazar Slytherin and could only be controlled by the Heir of Slytherin, Tom Riddle.""")
            elif name.strip() == "Dementor":
                await ctx.send("""Dementors are dark creatures that fed on human happines and so any person close to them will generate feelings of despair and depresion. They can also consume a persons soul by sucking it out of the victims body and turning them into an "empty-shell". That's why they are also reffered to as "soul-sucking fiends".
★ The dementors can not be killed but they can be driven away with The Patronus Charm that is summoned by good will and happines.
★ For anyone who had been overcome in the presence of Dementors, the best antidote was chocolate with it's mood-enhancing properties. However, it could only be a short-term cure. """)
            elif name.strip() == "Dobby":
                await ctx.send("""Dobby was a house-elf who used to serve the Malfoy family where he was treated cruelly. His master was Lucius Malfoy until Harry Potter tricked Malfoy into freeing dobby with a sock. That's how the iconic line "Master has given Dobby a sock. Master has presented Dobby with clothes. Dobby is… free." was born.
★ Later on, Dobby died saving Harry Potter and his friends in the Malfoy Manor. To not forget, he died as a free elf as said on his grave "HERE LIES DOBBY, A FREE ELF".
★ Another iconic line of Dobby that he said moment before his death was "Dobby never meant to kill! He only meant to maim, or seriously injure." """)
            elif name.strip() == "Hedwig":
                await ctx.send("""Hedwig is Harry Potter's pet snowy owl. She was a gift from Hagrid to Harry on his 11th birthday. She was Harry's closest friend and remained one until her deah during the Battle of the Seven Potters.  
★ Hedwig was an intelligent owl and she died after she was struck by a killing curse aimed at Harry or Hagrid, maybe saving them with her death. """)
            elif name.strip() == "Niffler":
                await ctx.send("""Nifflers are magical beasts that are attracted to shiny things, which made them wonderful for locating treasure, but that also meant that they could destroy belongings looking for sparkly objects if kept indoors.
★ They were seen in Fantastic Beasts movies with their pouches on their bellies.""")
            elif name.strip() == "Sorting hat":
                await ctx.send("""The Sorting Hat is a magical hat that was used to determine which school house was the best fit for the new student. These school houses are Gryffindor, Hufflepuff, Slytherin and Ravenclaw. The Sorting Hat originally belonged to Godric Gryffindor, one of the four founders of Hogwarts.
★ There are times when the Hat struggles to determine which house is the best fit for a student. In rare cases like this the student is calleda “Hatstall”. The most known Hatstalls are Minerva McGonagall, Peter Pettigrew, Filius Flitwick, Hermione Granger and Harry Potter.
★ For all this talk of Hatstalls, it’s important to remember that most students are sorted relatively quickly. Like this one student who was placed in their house almost immediately: Tom Riddle, known as Lord Voldemort.""")
            elif name.strip() == "Thestral":
                await ctx.send("""The thestrals are a breed of winged horse with a skeletal body. They were very rare, and were considered dangerous by the British Ministry of Magic. 
★ Thestrals were, undeservedly, known as omens of misfortune and aggression by many wizards because they were visible only to those who had witnessed death at least once.
★ The most known characters that could see Thestrals were Luna Lovegood and Harry Potter (after Cedric Diggory's death).""")

    else:
        await ctx.send("add an image pls!")

bot.run(token)