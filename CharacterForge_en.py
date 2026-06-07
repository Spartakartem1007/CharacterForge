from tkinter import *
from tkinter import ttk
import random

male_names = [
    "Aragorn", "Geralt", "Kaladin", "Drogo", "Thorin", "Legolas", "Gimli", "Frodo",
    "Boromir", "Eddard", "Jon", "Tyrion", "Jaime", "Witcher", "Fist", "Richard",
    "Conan", "Arthur", "Merlin", "Orpheus", "Hades", "Valiant", "Sigurd", "Ragnar",
    "Bjorn", "Ivar", "Xerxes", "Hector", "Achilles", "Odysseus", "Perseus", "Theseus",
    "Hercules", "Zeus", "Apollo", "Poseidon", "Ares", "Hephaestus", "Hermes", "Dionysus",
    "Pluto", "Odin", "Thor", "Loki", "Balder", "Heimdall", "Tyr", "Vidar", "Magnus",
    "Kian", "Ronan", "Finn", "Lugh", "Nuada", "Lancelot", "Gawain", "Tristan", "Percival",
    "Mordred", "Escanor"
]

female_names = [
    "Artemisia", "Sylvanel", "Morrigan", "Luthen", "Eowyn", "Arwen", "Galadriel",
    "Celeborn", "Luthien", "Brienne", "Daenerys", "Cersei", "Melisandre", "Arya",
    "Sansa", "Catelyn", "Ygritte", "Spark", "Geraltina", "Ciri", "Vennegoer", "Triss",
    "Yennefer", "Sadko", "Vasilisa", "Marya", "Snow White", "Rapunzel", "Elsa", "Anna",
    "Moana", "Mulan", "Pocahontas", "Belle", "Jasmine", "Aurora", "Ariel", "Tiana",
    "Merida", "Hera", "Athena", "Aphrodite", "Artemis", "Demeter", "Persephone", "Hestia",
    "Iris", "Nike", "Helen", "Cassandra", "Andromeda", "Medea", "Circe", "Penelope",
    "Clytemnestra", "Electra", "Antigone", "Ismene", "Frigg", "Freya", "Idunn", "Sif",
    "Hel", "Nanna", "Skadi", "Gerda"
]

backgrounds = [
    "Found as a baby in the forest, raised by wild wolves",
    "Grew up in a circus, can juggle and read minds",
    "Escaped slavery after killing their cruel master",
    "Lost entire family in a fire, seeking revenge on the arsonists",
    "Served as a royal spy but betrayed the crown for love",
    "Cursed by a witch in childhood — turns into a beast during full moon",
    "Found an ancient artifact that grants power but slowly kills them",
    "Was resurrected by a necromancer, remembers only their name",
    "Born with silver eyes — everyone fears them as an omen of doom",
    "Has lived in a cemetery since childhood, talks to ghosts",
    "Was a knight but lost their honor due to false accusation",
    "Ran away from a mage's house because they couldn't endure the brutal training",
    "Found a talking raven who became their only friend",
    "Was a changeling raised by fairies, returned to the human world after 100 years",
    "Sold their soul to a demon to save a loved one",
    "Born on the day of a solar eclipse — considered the chosen one",
    "Has hidden their whole life that they are half-dragon",
    "Lost their memory after being struck by lightning, began seeing the dead",
    "Was a pirate captain, but the crew mutinied and stranded them on an island",
    "Made a deal with a witch — forgot their past in exchange for magic"
]

body_armor = ["Torn leather jacket", "Worn chainmail", "Dragon breastplate", "Wolf cloak", "Plate armor", "Cursed black cloak", "Quilted gambeson", "Druid's cloth robe", "Dark metal cuirass", "Magical robe with runes", "Holey tunic", "Light elven armor", "Bear hide", "Necromancer's robe", "Snakescale vest"]

legs_wear = ["Leather pants", "Torn wool breeches", "Kilt", "Heavy plate legguards", "Long fur skirt", "Linen loose harem pants", "Black tight leggings", "Rag loincloth", "No pants", "Leather fringe skirt", "Metal-plated greaves", "Fur pants", "Long dress", "Silk pants", "Torn riding breeches"]

footwear = ["Knee-high leather boots", "Bast sandals", "Forged iron boots", "Soft suede shoes", "Rough soldier's brogans", "Barefoot", "Light sandals", "Feathered speed boots", "Heavy armored jackboots", "Wolf fur boots", "Black leather half-boots", "Wooden clogs", "Dragon scale boots", "Torn rawhide shoes", "Boots with sharp curled toes"]

root = Tk()
root.title('CharacterForge')
root.geometry('500x400')
root.configure(bg='#ffda7d')

label = Label(root, text='Select your character\'s gender')
label.pack()
label.configure(bg='#ffda7d')

gender_var = StringVar(value="male")
rb_male = Radiobutton(root, text='Male', variable=gender_var, value='male')
rb_male.pack()
rb_male.configure(bg='#ffda7d')

rb_female = Radiobutton(root, text='Female', variable=gender_var, value='female')
rb_female.pack()
rb_female.configure(bg='#ffda7d')

label_name = Label(root, text="")
label_name.pack()
label_name.configure(bg='#ffda7d')

def generate():
    if gender_var.get() == "male":
        name_character = random.choice(male_names)
    else:
        name_character = random.choice(female_names)
    label_name.config(text=name_character)

Button(root, text="Generate name", bg='#58fc87', command=generate).pack()

label = Label(root, text='')
label.pack()
label.configure(bg='#ffda7d')

label = Label(root, text='Create a backstory')
label.pack()
label.configure(bg='#ffda7d')

def back():
    back_character = random.choice(backgrounds)
    label_back.config(text=back_character)

Button(root, text="Generate backstory", bg='#58fc87', command=back).pack()
label_back = Label(root, text="")
label_back.pack()
label_back.configure(bg='#ffda7d')

label = Label(root, text='')
label.pack()
label.configure(bg='#ffda7d')

label = Label(root, text='Create a random outfit')
label.pack()
label.configure(bg='#ffda7d')

def tip4():
    body = random.choice(body_armor)
    label_tip1.config(text=body)
    legs = random.choice(legs_wear)
    label_tip2.config(text=legs)
    foot = random.choice(footwear)
    label_tip3.config(text=foot)

Button(root, text="Generate outfit", bg='#58fc87', command=tip4).pack()
label_tip1 = Label(root, text="")
label_tip1.pack()
label_tip1.configure(bg='#ffda7d')
label_tip2 = Label(root, text="")
label_tip2.pack()
label_tip2.configure(bg='#ffda7d')
label_tip3 = Label(root, text="")
label_tip3.pack()
label_tip3.configure(bg='#ffda7d')

root.mainloop()

