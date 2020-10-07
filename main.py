import random
from Crot import Crot

"""CREATE CROTS"""
my_mother = Crot("My mother, my mother, my \n My mother ate me up with love.", "my mother my mother yes she ate she ate she ate me up did she say how she said she ate me up with love")

a = Crot("Chocolate halls. Dripped ceilings. Sugar breath.", "the halls drip down saliva thick burns like oils under fingernails the ceilings press close get caught in your throat")
b = Crot("Tour guide. Clipped, shell-slicked hair. Skull doesn't crack. She built this place—it won't hurt her. (At least, not in a way you can understand).", "the girl the girl the woman with her hair pulled back her skull doesn't crack this place won't hurt won't hurt can't hurt her you don't see with your eye wide open the lids pulled back shore lines receding dry this place can't touch her no you can't see it touch her yes")
c = Crot("\"Welcome to my gallery,\" she says. \"Watch the steps. They're slick.\"", "the steps the steps they slide saliva sticky-slick-burns smells like sex she says to watch them watch watch watch with your eye open dried flowers blooming out from dead center")
d = Crot("Second floor. Flows downwards. Soft ceiling. Brutal railing. Cuts.\n\"Don't eat the artwork,\" she says. \"It bites back.\"", "the floor the floor the floor flows downwards pools into ceiling blood blood blood pools and dries grown brown grows flaky grows rose petals you got in the mail turned moldy like the sun the artwork tears the artwork chews the artwork has teeth, she says, teeth teeth teeth don't be afraid they'll cut you so quick you won't even feel pain")
e = Crot("(Even without you biting first.) The artwork gnaws. Brushstrokes like fur, hair caught in its throat.", "brushstrokes fur prickle down your throat slides down vomit the artwork has no manners the artwork touches you without permission")

text_1 = [a, b, c, d, e]

f_you = Crot("\"But not your mother, huh?\" Quirk. Carved into lip. Sharp tooth, gleaming smile. \"At one point in my life, that would have made me jealous. Not anymore.\"", "your mother your mother no she did not eat she did not eat she did not eat you she did not love you up with love")
f_mother = Crot("\"Your mother, too?\" Lips tighten. Old fruity skin. Bursting. \"A friend once told me all mothers are the same. I wonder how much that's true.\"", "all mothers all mothers the same with their hands linked in a circle spinning the ritual the moon wide and liquid not dry you can't understand you're not woman girl no not the way they are you should have empathy you should know this ritual changes them know no they are not the same they feel the same but only because the center whirlpools it pulls with their water up your throat you cannot see it see see see")

g = Crot("Ethan. Sugar-spun hair. Butterscotch curls. Candy-slick tongue between filmed teeth.", "the boy the boy blonde hair like an angel curled not subverted innocent pink teeth with slime the animal the creature no spine no nose no mouth no ears bumpy little eyes existed before us in the caves in the soft warm dark where it ate it crawled all mouth it sucked at the walls and drew trails of slime")
h = Crot("Drag eyes over him. No artist anymore. So be it: you're not sure she's your friend.", "the create ignores the creature keeps sucking keeps moving keeps its slime the artist the woman she left but she's no better you looked closer but the creature has no answer tells no secrets")
i = Crot("Ethan kicks at the wall. Spins. Whistles. \"Strange place, huh?\" he says. \"I never could make sense of this artsy-fartsy stuff. \'My mother ate me up with love.\' So what? It seems a bit thin for a whole gallery, doesn't it?\"", "the wall the wall the boy the creature ethan spins and whistles a top with no gravity what a strange place strange place he says, the mother ate ate ate so what? are you afraid of a little teeth little bite little acid tearing down your skin a bit thin for a gallery doesn't it the fear recedes it pulls back from the shore it goes to rot far in the center of the ocean but maybe not for you huh")
j = Crot("Doesn't wait. Turns again, hands buried behind head. Starts walking.", "the top spins further the gravity loosens its grip another ring out another planet far away the boy the create moving so far away spinning out from under you spinning out from your center")

text_2 = [g, h, i, j]

artistDangerWithEthan = Crot("Ethan curses. Broad shoulders against wall. Crack. Crumble him inside himself. \n \"Fuck!\" he says. Then turns. Dull, blinded. Sharp knives less dangerous. \"What the fuck did you say to her?\" Blunt force. Head spins. \"What the ever-locking fuck did you say to her?\"", "the boy the boy the creature crumbles falls back into himself spins faster spins a black hole yells screams spits shooting stars firesparks you stupid bastard what the fuck did you say to her what did i say what")
artistDangerWithoutEthan = Crot("Standing in stairs. Spiral, fall. Or rise. Or stand still. \n Your head pounds. When you swallow, there's a taste of metal in your throat.", "the stairs the stairs you fall you spiral down drip-drop drip you conglomerate you smell you rot")
artistNoDangerWithEthan = Crot("Ethan glances. Swivels his head. Still whistling. Then side-eye. Face stone house, windows closed. Movement secret, sacred. Unreachable through deep-set windows. \nSmiles broadly. Teeth dull. Wish you could read him.", "the boy the boy turns turns away the creature the creature keeps sucking the wall pays you no mind draws out the color the light the flesh turns pale the blood the blood the blood is gone the ritual the ritual what ritual lives inside the spiral the spiral the spiral of his stomach his putty intestines his pre-historic body")
artistNoDangerWithoutEthan = Crot("Fall down stairs. Slick, almost wet. Stumble breath caught in throat. \nArtist with long dark dress, small sharp teeth. Tools held loosely in luminous hands. Silken scars knot. \"Nothing to see here,\" says she. Eyes narrow, make you small. Pointed tongue through still lips. \"You came here with a friend, didn't you? You should keep better track of them.\"", "the stairs the stairs you spiral drip-drop drip you conglomerate you smell you rot you contract you expand breath shudders out of you bones rattle bones decompose bones elasticize the woman the woman the girl the artist arrowheads in her teeth nighttime falling against her skin pale pale pale moon hands cratered veined uncooked sinewed nothing nothing to see she says why don't you believe her why does she lie when you can see her her shadow her eyes her shadow behind the moon you turn you turn you turn your face away no shadow no more your friend your friend you came here with them you held their hand your friend your friend may have fallen down with you your friend your fried clumped hair beneath your nail a morsel between your teeth your friend your friend where did they go?")

room = Crot("Dark room. Vibrations. You came here with your best friend and now you miss them. Walls squelch, suction. Get closer. \nPress against you. Wet soft warm. You sink through. Start to decompose.","Dark room. Vibrations. You came here with your best friend and now you miss them. Walls squelch, suction. Get closer. \nPress against you. Wet soft warm. You sink through. Start to decompose.")
title = Crot("the missing image", "The missing image")

"""STORY"""

choices = [0, 1]
story_id =[] #ID that keeps track of story state and player choices

#Booleans that determine the state of the story
#Randomly generated
artistSameAffinity = bool(random.choice(choices))

story_id.append(artistSameAffinity)

def continue_on(): #Function to allow reader to continue
  input("\nPRESS ENTER  ")
  print ('\n')
 
print("Content warnings: abuse of parental authority, graphic body descriptions, body horror, trauma, sense of unreality, strong language, sexual assault\n")

print("________________________________________")

print(title.returnRandom() + '\n')
print(my_mother.returnRandom())
continue_on()

for x in range (len(text_1)):
  print(text_1[x].returnRandom())
  if (x==4):
    print('\n')
    print(my_mother.returnRandom()) #Print text where needed--repeated throughout piece
  continue_on()

choice_1_you_list = ["you", "You", "\"you\"", "\"You\""]
choice_1_mother_list = ["your mother", "Your mother", "mother", "Mother", "\"your mother\"", "\"Your mother\"", "\"mother\"", "\"Mother\""]
choice_1_list = choice_1_you_list + choice_1_mother_list

print("The artwork is")
choice_1_input = input ("TYPE \"you\" OR \"your mother\" ")

while (choice_1_input not in choice_1_list):
  choice_1_input = input ("PLEASE TYPE \"you\" or \"your mother\". THEN HIT ENTER. ")

if (choice_1_input in choice_1_you_list):
  choice_1 = "you"
else:
  choice_1 = "mother"

print('\n')

if (choice_1 == "you"):
  print(f_you.returnRandom())

if (choice_1 == "mother"):
  print(f_mother.returnRandom())

#Choice logic for choice 1
if (artistSameAffinity):
  if (choice_1 == "you"):
    artistDanger = True
  else:
    artistDanger = False

if (not artistSameAffinity):
   if (choice_1 == "you"):
    artistDanger = False
   else:
    artistDanger = True
  
continue_on()

for x in range (len(text_2)):
  print(text_2[x].returnRandom())
  continue_on()

choice_2_follow_list = ["follow", "Follow", "\"follow\"", "\"Follow\""]
choice_2_back_list = ["Go back", "go back", "back", "Back", "\"Go back\"", "\"go back\"", "\"back\"", "\"Back\""]
choice_2_list = choice_2_follow_list + choice_2_back_list

print("Do you follow Ethan or go back to the artist?")
choice_2_input = input ("TYPE \"follow\" OR \"go back\" ")

while (choice_2_input not in choice_2_list):
  choice_2_input = input ("PLEASE TYPE \"follow\" or \"go back\". THEN HIT ENTER.")

print('\n') 
print (my_mother.returnRandom(), '\n')

if (choice_2_input in choice_2_follow_list):
  choice_2 = "follow"
if (choice_2_input in choice_2_back_list):
  choice_2 = "back"

if (artistDanger):
  if (choice_2 == "follow"):
    print(room.returnRandom(), '\n')
    continue_on()
    print(artistDangerWithEthan.returnRandom())
  if (choice_2 != "follow"):
    print(room.returnRandom(), '\n')
    continue_on()
    print(artistDangerWithoutEthan.returnRandom())

if (not artistDanger):
  if (choice_2 == "follow"):
    print(artistNoDangerWithEthan.returnRandom())
  if (choice_2 != "follow"):
    print(artistNoDangerWithoutEthan.returnRandom())

print('\n')
continue_on()
print("This is how you remember it. Would you like to remember again?")