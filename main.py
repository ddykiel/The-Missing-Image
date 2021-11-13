import random
from Crot import Crot
import replit

"""CREATE CROTS"""

title = Crot("the missing image", "The missing image")

my_mother = Crot("My mother, my mother, my \n My mother ate me up with love.", "my mother my mother yes she ate she ate she ate me up did she say how she said she ate me up with love")

a = Crot("The dark hall.", "the halls saliva drip down thick burns under fingernails")
b = Crot("The tour guide with her clipped hair. She built this place. It won't hurt her. At least, not in a way you can understand.", "the girl the girl with her hair pulled back her skull doesn't crack this place won't hurt can't hurt her this place can't touch her no you can't see it touch her yes")
c = Crot("\"Welcome to my gallery,\" she says. \"Watch the steps. They're slick.\"", "the steps they slide sticky-slick-sex-burns she says to watch watch watch dried flowers blooming out from dead center")
d = Crot("You step down to the second floor.\n\"Don't eat the artwork,\" she says. \"It bites back.\"", "the floor the floor flows downwards pools into ceiling pools and dries grown brown flaky turned moldy like the sun the artwork tears the artwork has teeth she says teeth teeth teeth don’t be afraid, they'll cut you so quick you won't even feel pain")
e = Crot("The artwork gnaws. Even without you biting first. Brushstrokes like fur, hair caught in its throat.", "brushstrokes fur prickle down your throat the artwork has no manners the artwork touches you without permission")

text_1 = [a, b, c, d, e]

f_you = Crot("\"But not your mother, huh?\" A smile carves her face. \"At one point in my life, you would have made me jealous. Not anymore.\"", "your mother your mother no she did not eat she did not eat she did not she did not eat you she did not love you up with love")
f_mother = Crot("\"Your mother, too?\" Her lips tighten, old fruit bursting. \"A friend once told me all mothers are the same.\"", "all mothers all mothers the same with their hands linked in a circle spinning the ritual night wide and liquid")

g = Crot("Ethan with his sugar-spun hair, candy-slick tongue.", "the boy the boy blonde hair like an angel curled not subverted the animal the creature no spine no nose no mouth no bumpy little eyes existed before us all in caves of soft warm dark where it ate and drew across the walls trails of slime")
h = Crot("Your eyes drag over him. The artist is gone. So be it: you’re not sure she’s your friend.", "the creature ignores the creature keeps its slime the artist the woman she’s no better the creature has no answer tells no secrets")
i = Crot("Ethan kicks at the wall. Whistles. \"Strange place, huh?\" he says. \"I never could make sense of this artsy-fartsy stuff. \'My mother ate me up with love.\' So what? It seems a bit thin for a whole gallery, doesn't it?\"", "the wall the boy the creature ethan spins and whistles with no gravity what a strange place he says, the mother ate ate ate so what? are you afraid of a little teeth little bite little acid tearing down your skin? the fear pulls back it pulls from the shore it goes to rot far in the center of the ocean but maybe not for you huh")
j = Crot("He turns again, hands buried in his hair. Starts walking.", "the gravity loosens another ring out the boy the spinning out from under you spinning away from your center")

text_2 = [g, h, i, j]

artistDangerWithEthan = Crot("Ethan curses. Wrenches his shoulders against wall. Crack.\n \"Fuck!\" he says. Crumbles inside himself. Then turns. \"What the fuck did you say to her? What the ever-loving fuck did you say to her?\"", "the boy the boy the creature falls back into himself spins spits firesparks you stupid bastard what the fuck did you say to her what did i say what")
artistDangerWithoutEthan = Crot("You spiral, fall. Or rise. \n Your head pounds. When you swallow, there's a taste of metal in your throat.", "the stairs the stairs you fall you spiral up drip-drop drip you conglomerate you smell you rot")
artistNoDangerWithEthan = Crot("Ethan swivels away. Still whistling. His face a stone house, unreachable through deep-set windows.", "the boy the boy turns turns away the creature the creature keeps sucking the wall pays you no mind")
artistNoDangerWithoutEthan = Crot("You fall down the slick-wet stairs, stumble with your breath caught. \nThe artist with her long dark dress, her small sharp teeth. Tools held still in luminous hands. \"You came here with a friend, didn't you? You should keep better track of them.\"", "spiral drip-drop drip you conglomerate you smell you rot you contract you expand breath shudders out of you bones elasticize the woman the girl the artist arrowheads in her teeth nighttime falling against her skin pale pale hands uncooked sinewed nothing nothing to see she says nothing.")

k = Crot("Your friend. She may have looked just like you.","the grasping shadow the fleeting face your friend you when you were children you talked of killing each other in your sleep")

l = Crot("The walls of the gallery crumble, flesh-warm in your hands.","your friend the burr she held you she held your clothes your hair your skin now ethan she holds and follows")

m = Crot("You may still catch her if you run fast.","your friend the burr she held you she held your clothes your hair your skin now ethan she holds and follows")

n = Crot("She holds out a hand with no face. \"Trust me,\" she says, her voice barely a whisper: as if she has already left. \"I may still catch him if I run fast.\"","the warm wind around your shoulders thin thin her thin neck become voice i can find him if you let me trust if you trust me if you trust him not if you trust us trust")

text_3 = [k, l, m, n]

trustDanger = Crot("She left the gallery and the next morning she was missing.","no spikes no spines no legs to run after to find her did you ever find her did she ever leave leave our gallery did you ever see her leave")
trustNoDanger = Crot("She left the gallery and bludgeoned his face against the steering wheel. The next morning he was missing.","into the lake with no shorelines receding like the wind like her hand waving thin and luminous he watched her hand from his rearview window shining like the moon")
noTrustDanger = Crot("She stays in the gallery. One day you find Ethan too. A formless insect, dead within the walls.","she stays and when the cold in the winter strikes you think of making a fire you think of smoking up the bones")
noTrustNoDanger = Crot("She stays in the gallery with you","she stays she stays she gains a set of scratching gums a new set of teeth i could have torn him and you stopped me why for what why you stopped these hollow teeth and us three in the gallery forever")

ending_1 = Crot("Start with the glint of metal, iron oxide in your toffee. A head ballooning up and down, ballooning inside itself. A stone house, unreachable through deep- set windows.\n Haven't you heard this story before?","start with glint-metal the iron oxide in his sugar-spun hair a balloon without a body floating up and down haven’t you heard, haven’t you heard this story before?")

ending_2 = Crot("Ethan stands, a rhythm of metal against his palm. \"I never could make sense of this artsy-fartsy stuff,\" he says. Her life glitters in his eyes. \"\'My mother ate me up with love.\' It seems a bit thin for a whole gallery, doesn't it?\"","your gold tooth your silver foil caught between his gums a rhythm of metal between his palms swinging down the metal the metal against his knees haven’t you heard haven’t you heard was it was it ever was she ever")

"""STORY"""

endlessLoop = bool(True)

while endlessLoop:

  choices = [0, 1]

  #Booleans that determine the state of the story
  #Randomly generated
  artistSameAffinity = bool(random.choice(choices))
  trustFriend = bool(random.choice(choices))

  def continue_on(): #Function to allow reader to continue
    print ('\n')
    input("\nPRESS ENTER  ")
    replit.clear()
    repetition = random.randint(0, 9) #Randomly select a number between 0-9 to determine if the motif will randomly repeat. It repeats if the number is 0; i.e., there's a 1/10 chance it repeats. // Test different frequencies
    if (repetition == 0):
      print(my_mother.returnRandom())
      print ('\n')
      input("\nPRESS ENTER  ")
      replit.clear()

  print("________________________________________")

  print(title.returnRandom() + '\n')
  continue_on()

  for x in range (len(text_1)):
    print(text_1[x].returnRandom())
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

  replit.clear() #Clear screen after answering question

  if (choice_1 == "you"):
    print(f_you.returnRandom())

  if (choice_1 == "mother"):
    print(f_mother.returnRandom())

  continue_on()

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

  if (choice_2_input in choice_2_follow_list):
    choice_2 = "follow"
  if (choice_2_input in choice_2_back_list):
    choice_2 = "back"

  replit.clear() #Clear screen after answering question

  if (artistDanger):
    if (choice_2 == "follow"):
      print(artistDangerWithEthan.returnRandom())
    if (choice_2 != "follow"):
      print(artistDangerWithoutEthan.returnRandom())

  if (not artistDanger):
    if (choice_2 == "follow"):
      print(artistNoDangerWithEthan.returnRandom())
    if (choice_2 != "follow"):
      print(artistNoDangerWithoutEthan.returnRandom())

  continue_on()

  for x in range (len(text_3)):
    print(text_3[x].returnRandom())
    continue_on()

  choice_3_trust_list = ["trust", "Trust", "\"trust\"", "\"Trust\""]
  choice_3_distrust_list = ["distrust", "Distrust", "\"distrust\"", "\"Distrust\""]
  choice_3_list = choice_3_trust_list + choice_3_distrust_list

  print("Do you trust or distrust your friend?")
  choice_3_input = input ("TYPE \"trust\" OR \"distrust\" ")

  while (choice_3_input not in choice_3_list):
    choice_3_input = input ("PLEASE TYPE \"trust\" or \"distrust\". THEN HIT ENTER. ")

  if (choice_3_input in choice_3_trust_list):
    choice_3 = "trust"
  else:
    choice_3 = "distrust"

  replit.clear() #Clear screen after answering question

  #Choice logic for choice 3
  if (trustFriend):
    if (choice_3 == "trust"):
      print(trustNoDanger.returnRandom())
    if (choice_3 != "trust"):
      print(noTrustNoDanger.returnRandom())

  if (not trustFriend):
    if (choice_3 == "trust"):
      print(trustDanger.returnRandom())
    if (choice_3 != "trust"):
      print(noTrustDanger.returnRandom())

  continue_on()

  firstEnding = bool(random.choice(choices))

  if (firstEnding):
    print(ending_1.returnRandom())

  if (not firstEnding):
    print(ending_2.returnRandom())

  continue_on() #Clear screen after iteration
