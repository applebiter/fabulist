import threading
from configparser import ConfigParser
from noveler.application import Noveler


def print_cube(num):
    print("Cube: {}".format(num * num * num))


def print_square(num):
    print("Square: {}".format(num * num))


"""Example database connection strings

noveler = Noveler("postgresql+psycopg://{dbuser}:{dbpassword}@{dbhost}:{dbport}/{dbname}", echo=False)
    Shown here using the psycopg driver, also known as psycopg3
noveler = Noveler("mysql+mysqlconnector://{dbuser}:{dbpassword}@{dbhost}:{dbport}/{dbname}", echo=False)
    Shown here using the mysql-connector-python driver
noveler = Noveler("sqlite:///{dbname}.db", echo=False)

You supply the connection string to the Noveler class, and it will automatically generate the database schema. Shown 
here using the sqlite3 driver, which is included in the Python standard library. The echo parameter is optional and
defaults to False. If set to True, it will print all SQL commands to the console. This is useful for debugging.
"""


config = ConfigParser()
config.read("config.cfg")
# db stuff
user = config.get("mysql", "user")
password = config.get("mysql", "password")
host = config.get("mysql", "host")
port = config.get("mysql", "port")
database = config.get("mysql", "database")
# noveler = Noveler(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")
noveler = Noveler(f"sqlite:///{database}.db")
# Export the existing story to JSON
if noveler("export").export_story_to_text(story_id=1):
    print("Exported story to file.")
else:
    print("Abject failure.")

# reach out to the ollama server for updates
# noveler("assistant").update_models()

# Create a new story
# story = noveler("story").create_story(
#     title="Agent Ralph: The Peed St. Problem", description="Case number 1611-02"
# )
# # CHAPTER 1
# chapter1 = noveler("chapter").create_chapter(
#     story_id=story.id, title="Part I: The Interviews",
#     description=None
# )
# # SCENE 1
# scene1 = noveler("scene").create_scene(
#     story_id=story.id, chapter_id=chapter1.id,
#     title="November 23, 2016, 7:46 pm. Alley behind shops on Peed Street.",
#     description=None,
#     content="""Ralph didn't enjoy getting dirty on accident and certainly not on purpose; but here he lies in the shadows of The Stinky Possum Pub covered in dead leaves and old grass clippings. Waiting.
#
#
# Two days ago Flando the rat, Frances’ brother, came to him concerned for the alley cats that had disappeared and then returned later with terrible stories.
#
#
#
# “Family and friends reported they weren’t the same when they came back home. The cats don’t have an interest in the things they used to enjoy. Half the time they show no emotion, the other half they are angry and lash out at anyone who tries to help. Still, others never came back," said Flando.
#
#
# Ralph listened then said, “The ferals have taken a hard hit from illness this year. I’ve never seen it this widespread. And now this, this news truly troubling. How long has this been happening?”
#
#
# “Oh, I’d say about a month. It started after the big fall clean up the city does each year.”
#
#
#
# “How many food stations would you guess have been removed?” asked Ralph.
#
#
#
# “All the ones in the front of the Peed Street shops and in the city square. Raccoons now control the ones in the alleys and you know what trouble that can bring. Their leader, Jeff, rules with an iron paw. Cats must go further into the house areas to find food but the people are afraid their own cats  will get sick.”
#
#
#
# Replaying the conversation in his head over and over he tried to tease out more clues, Ralph had dozed off when someone triggered one of his crispy leaf alarms. With half-slit eyes, he watched as cat after cat entered a small alcove. After the eighth cat entered, he followed them where they sat  in a circle with their backs towards each other. Before he joined them a loud clang rang out as a gate crashed down behind him. Cats scattered to the shadows. Then another gate came down in front of him. They trapped him before he could run. He couldn’t see much through the metal grate, a tail here, an ear there. A pink nose owned by a cat with terrible breath, worse than mashed peas and garlic, blocked his view.
#
#
# “We don’t take kindly to strangers poking about,” said a raspy voice.
#
#
#
# “I bet he’s the one getting everybody snatched,” said another.
#
#
#
# “Or sick. I’ve seen his kind. Thinks he can slip in and weed out the weak ones, clean up the riffraff.” said a third.
#
#
#
# “Yeah!” said the cats.
#
#
#
# “What shall we do with him?” said the first.
#
#
#
# “Get him!” meowed a chorus cats with a few hisses.
#
# Agent Ralph did not understand what that meant but it couldn’t be good. These traumatized cats were out for blood. He hadn’t noticed the rat before but caught his shadow out of the corner of his eye. It sat up on whatever it perched on and addressed the group. The rat had a can lid in his hand which he banged with a spoon to bring the meeting to order. The cats didn’t pay attention and now they marched towards Ralph. As soon as he saw them back up towards him he pressed his large Maine Coon body up against the back gate and closed his eyes preparing for what was to come.
#
#
#
# The host said, “Good evening, everyone. My name is Flando and I’m glad you made it to this meeting. If this is your first time you don’t have to take part but I encourage you to get it off your chest.” The male cats took turns peeing on the closed gate. “What’s going on?” asked Flando.
#
#
#
# “We’ve caught a snooper!” yelled a cat.
#
#
#
# “Ooh, he’s a big one, too,” said another.
#
#
#
# “Stop, stop, stop!” shouted Flando as he banged on the lid again. The cats backed away. A tiny brown nose with long whiskers appeared in front of Ralph. “Are you all right, sir?”
#
#
#
# “I’ll survive,” said Ralph, “Fresh air would be nice.”
#
#
#
# Flando worked the latch and opened the gate. Ralph had no idea Frances’ brother was such a felinitarian. He’d have to congratulate him later for doing such a fine job and a much-needed service. These cats were a rough bunch and Ralph did not blame them for their anger.
#
#
#
# “Let’s try this again,” Flando said pinching his nose. Ralph stepped through the gate and sat next to Flando. “Allow me to introduce a special guest, Agent Ralph who is an important member of our community and as a Domesticated Investigation Bureau officer is investigating what is happening. Now, before you get upset I want you to know I invited him here. I asked him to join our group and listen to what has happened to you so he can solve this mystery. I understand that you may not wish to share but remember why he is here.”
#
#
#
# “Thank you so much for the wonderful introduction, Flando. It is true. I am investigating these occurrences and will do everything in my power to sort this out. I know you are upset and that these things that have happened are frightening. What I hear in this alcove, I promise you, won’t leave the alcove,” Ralph said. “It would be most helpful if you could tell me what happened to you.”
#
#
#
# Silence. No one came forward.
#
#
#
# Flando stood on his hind legs, “Come on now, are you so angry you can’t help those who are still missing? Ralph is our best chance of finding out who is doing this.”
#
#
#
# At last, an orange tabby stepped forward. “Thank you, Nacho,” said Flando.
#
#
#
# “I remember little of what led up to it. I saw a bright light getting closer and closer,” said Nacho.
#
#
#
# Then they took turns telling Ralph of their experience.
#
#
#
# “Mudd here. I have dreams of monsters. They wore space suits and had big round eyes. I thought I was gone for an hour or two,” said a tortoiseshell, “when I came back my brother Ollie was gone and is still missing.”
#
#
#
# The female calico next to him said, “My friends call me Zitzit cause I like to catch bugs that make that noise. Well, I used to. Now all the bugs remind me of the monsters. There were a bunch of us there together in the holding area. I was so scared I peed myself.”
#
#
#
# Mudd reached over and licked Zitzit’s face to soothe her.
#
#
#
# “Hi, my name is Checkers. I remember lights also. I was examined by the monsters in those suits,” he looked down at the ground, “sorry for peeing on you.” said one of the two black and white cats.
#
#
#
# The other said, “Yeah, sorry about that. I’m Chappy. It felt like a short time, but we had been missing three days. Now I have a lump on my shoulder.”
#
#
#
# “Me too. Everyone calls me Midnight.” said a female black cat.
#
#
#
# The orange and white cat next to Midnight said, “My name is Butterbean. When I came back, I saw my brother Nacho, who had been missing two days before they took me. They cut his ear, and he had a small scar on his stomach.”
#
#
#
# “When Butterbean came back her ear was also cut, and she had a much bigger scar. We noticed that we all have our left ears cut and a fresh scar on our lower stomach,” said Nacho.
#
#
#
# Last was a white cat, “We all have a green mark. I try to lick it off but it never goes away. All the other cats and animals here are afraid of us now. Oh, I’m Snowball.”
#
#
#
# Checkers said, “We all have the mark. We’re a bunch of misfits. I suppose that is why we were being mean. Those monsters hurt us and then our loved ones rejected us.”
#
#
#
# “Thank you for your time and patience. I know this has been very difficult,” said Ralph, “but I must take my leave to investigate further. I bid you a good evening. Please, ask any member of the 121st Street Clowder for help or if you’d like to offer further information. We’d be happy to help you in any way we can.”
#
#
#
# Ralph bowed then left. He believed they had experienced a horrible thing. Alien abduction. Their injuries followed a pattern, many of them still fresh. Ralph had to get abducted himself to know for sure.
#
#
#
# A voice from the shadows stopped him in his tracks. "Well, well, well. If it isn't a big, bad DIBs agent." Ralph turned just in time to see a group of raccoons attacks him placing a pillow case over his head and dragging him through the grass.
#     """
# )
# # SCENE 2
# scene2 = noveler("scene").create_scene(
#     story_id=story.id, chapter_id=chapter1.id,
#     title="November 23, 2016, 8:03 pm. 121st Clowder Headquarters.",
#     description=None,
#     content="""Meanwhile, Milton, Archie, and Frances were listening to the evening DIBs report, when a plaintive meowing broke their concentration. Archie was getting irritated but it didn’t take much to annoy him. “Milton, are you going to get that?”
#
#
#
# “Huh?” Milton asked.
#
#
#
# “Never mind, I'll do it myself," Archie said heading out the cat door.
#
#
# “Go ahead, Milton. I’ll catch you two up later.” Frances said waving off Milton.
#
#
#
# Milton found Archie sitting in the driveway. “Was that just my imagination?”
#
#
#
# “Would I be out here if it were your imagination?” Archie, the old Russian Blue, asked.
#
#
#
# "No," Milton said.
#
#
# “Please, come out. I won’t sit in the dark all night.” Archie said.
#
#
#
# “Excuse me, I don’t want to be a bother,” said a quiet voice coming from the privet.
#
#
#
# “Too late. Now, my dear how can I help you?” Archie asked.
#
#
#
# “You’re a DIBs agent, aren’t you? You can help me?” said a female black and white tuxedo cat.
#
#
#
# “Yes, I am an agent. I may help you but first, you need to tell me who you are and what is your matter."
#
#
# “My name is Tiff and my partner Ollie has gone missing," she said.
#
#
# “When and where did you last see him?”
#
#
#
# “It was two nights ago, and he headed towards the alley behind the shops on Peed Street.”
#
#
#
# “Can you tell us any more about what happened before he disappeared?" Milton asked. Frances came out and sat beside him.
#
#
#
# “I’ve been having trouble sleeping. He said he knew where he could get something to help. Ollie told me not to worry that Jeff could help.”
#
#
#
# “Who is Jeff?” asked Milton.
#
#
#
# “Jeff is a dumpster dealer her gang runs the alley behind The Stinky Possum Pub. Ollie doesn’t keep that sort of company and I’m afraid for him. I didn’t want him going there and end up getting sick. Things are so bad in the alleys. If cats aren’t getting sick, they’re disappearing. Only the kittens seem to be safe from kidnapping but many don’t get over the illness.”
#
#
#
# “I see,” said Archie.
#
#
#
# Frances went inside to fetch a few items and came back with cat food and two collars.
#
# “Ooh! Who are those for?” asked Milton.
#
#
#
# “You two," said Frances fastening them around Milton and Archie. Since she became a consultant for DIBs she was making many advances in her technical creations. "I've made upgrades. They now have a tracking device which monitors your location here and a proximity detector so you can find your way to each other. Located here is a small speaker. I didn't have time to add a switch to give you a microphone so you'll only be able to receive messages in Morris code."
#
#
# “Why is it making that noise?” asked Milton.
#
#
#
# “That is Ralph's signal. If you are within sniffing range there is no signal. If you change your direction the pitch will change. The collar will beep higher if you are heading towards each other and lower if you are going away. As you get closer the beeps get faster. I fit a motion detector on them but will only register clockwise and counter-clockwise movement. It is designed for answering questions with a yes or no reply in either direction. If you scratch the collar twice that means yes and three scratches means no. If you keep scratching you ask for backup. Everything clear?" Frances asked.
#
#
# Archie’s face beamed with pride, “Outstanding work, Frances.”
#
#
#
# “You guys are a high-tech operation aren't you?" asked Tiff.
#
#
# “You two go ahead, if anything comes up, I’ll contact you on your collar. Remember two scratches for yes and three for no.” Frances said. She’d ruin her street credibility if her contacts saw her in that alley with DIBs agents and she hated the stench of Peed Street.
#
#
#
# With their new collars on Milton and Archie headed toward the back yard.
#
#
#
# “You’re very polite for a street cat, how long have you been feral?” asked Frances.
#
#
#
# “Three years,” said Tiff. “It seem like only yesterday I had a warm lap to sit on, plenty of food, water, and sunshine patches to sleep in. Then my owners lost their house, and I was abandoned. If it hadn’t met Ollie, I might have starved.”
#
#
#
# Frances sighed, “I understand, if I hadn’t met these cats, I don’t know what I would do. I’m sure good will come out of this. DIBs agents are good cats. I thought you might be hungry, I brought you some food and there’s fresh water in that bowl over there.” she pointed with a little pink paw to a bowl near the steps leading into the kitchen.
#
#
#
# “Thank you so much for your kindness, Frances,” said Tiff. Frances acknowledged Tiff with a nod and thought of her brother who she always thought he was silly for the work he did helping stray animals. But now, she understood his wish to be a part of something bigger than just surviving.
#
#
#
# Frances watched Tiff eat and leave. Turning on the transmeowter she let Archie, Milton, and Ralph know there was a new agent in the vicinity.
#     """
# )
# # SCENE 3
# scene3 = noveler("scene").create_scene(
#     story_id=story.id, chapter_id=chapter1.id,
#     title="***",
#     description=None,
#     content="""Archie and Milton headed down the alley behind the house, cross over to the haunted house then take Peed Street to Ralph's location. They were almost at the haunted house when they saw a dark cat slink off towards Peed Street.
#
#
# They backed into the bushes when their collars buzzed with Morris code. The mystery cat looked in their direction but kept going. That was a close. Archie would have to talk to Frances about changing the volume.
#
#
#
#         “New agent in territory.”
#
#
# “That was close,” said Milton, “You think is the new agent?”
#
#
#
# “Let’s find out,” said Archie as he followed the silky brown cat. Milton ran a few paces to catch up to Archie. They’d only traveled a block before the new cat realized it was being tailed. It took another block for Archie and Milton to lose the cat. They dropped their gaze low to listen for any movement.
#
#
#
# “Did that cat just disappear?” asked Milton.
#
#
#
# “Not likely,” said Archie. “We have a job to do and should get on it.”
#
#
#
# “And stay out of my way,” said a deep female voice that was almost a growl.
#
#
#
# “You must be the new agent,” said Milton.
#
#
#
# “A real charmer,” said Archie, “I’d probably hide too if I was that grumpy.”
#
#
#
# “It takes lint to pick up lint.” she said.
#
#
#
# Milton blinked and tilted his head at the phrase trying to decipher it. This agent must have had very different training in codes.
#
#
#
# “I have important work to do,” she said.
#
#
#
# “Sure kid, don’t we all,” said Archie.
#
#
#
# “But, Archie,” said Milton, “you don’t hide.”
#
#
#
# “You’re not helping, Milton.” said Archie.
#
#
#
# Milton was still trying to figure out what she said. “Maybe she’s grumpy because she has a hairball from the lint, Archie.”
#
#
#
# "I don't have a hairball, and that is not what I meant," she said. "Seriously, cat's lives are at stake here."
#
#
# Archie’s and Milton’s collar chirped a series of three chirps and then a long drawn out chirp that sounded like a cricket. This differed from what Frances sent them previously. Ralph was sending a message via scratch cipher.
#
#
#
# The dark brown cat tilted her head, “What is that?”
#
# “Do you think you’re the only DIBs agent here?” he asked her, “Come on Milton, she is a distraction. We have to find Ollie,” said Archie.
#
#
#
# “She’s a pretty distraction,” Milton said.
#
#
#
# “She’s a Burmese; a brick wrapped in silk, Milt,” said Archie as he trotted off down Peed Street.
#
#
#
# “Well,” she said, “If you don’t like my notebook then don’t flip my pages.”
#
#
#
# Again, Milton tilted his head trying to work out her puzzling language. “I never got your name,” said Milton.
#
#
#
# “I never gave it,” said the chocolate brown cat.
#
#
#
# Milton shook his head then ran off to catch up to Archie. His ears focused behind him as he heard her say, “Minka! My name is Minka.” The Flame-point Siamese gave a twitch of his tail to signal that he heard her and slipped into the darkness.
#
#
#
# Minka trotted at an easy pace behind them and wondered what business they could have in the exact area where all of the sicknesses originated. The hair on the back of her ears prickled. Someone was watching her from above in the trees. She’d have to investigate later. Minka straightened her legs to pick up the pace, then she too disappeared into the shadows.
#     """
# )
# # CHAPTER 2
# chapter2 = noveler("chapter").create_chapter(
#     story_id=story.id, title="Part II: The Dealer",
#     description=None
# )
# # SCENE 4
# scene4 = noveler("scene").create_scene(
#     story_id=story.id, chapter_id=chapter2.id,
#     title=" ",
#     description=None,
#     content="""This was not what he had in mind.  “I don’t have time for this. Release me!” Ralph said trying to fight his way out of the bag. His collar buzzed with a message from Frances about a new agent. The rest of the team were listening to the evening DIBs report.
#
#
#
# “What is that noise?” One raccoon said.
#
#
#
# “Get the door would ya?” another voice said.
#
#
#
# There was a terrible scraping noise of a metal door opening and then closing behind him.
#
#
#
# “Welcome, Agent Ralph,” said a relaxed female voice.
#
#
#
# Ralph untangled himself from the pillow case. The bag had been dark his eyes adjusted to the low light in the shed. In front of him, he saw a raccoon swishing her paws in a pail of water. A small crate separated them. Pulling her paws out of the water, she had a small piece of metal in each one.  She placed an item on one plate, and the other item on another plate. While raccoons have an excellent sense of smell, the sensitivity of their hands increases five-fold when wet. "Fifteen for this one and 8 for that one," she told an old raccoon wearing an eye patch that came forward to take the plates. She sold kibble she had stolen from the neighborhood.
#
#
# Two raccoons guarded the door behind Ralph preventing his escape. The beep of his collar changed pitch signaling that Archie and Milton headed in his direction. Ralph had to warn them. He pretended to have fleas. First, he scratched a series of no replies. Then he bit his legs and scratched behind his ears. He scratched the collar requesting backup. He hoped it worked.
#
#
# “Tsk, tsk, tsk. You have been snooping around in places you shouldn’t,” said Jeff. “You picked up fleas and who knows what else. This has been a bad year for cats.”
#
#
#
# “Yes, Jeff, why don't you tell me about your collaboration with them," Ralph said looking up towards the sky.
#
#
# Jeff looked up then back at Ralph. “Apparently the fever has already claimed you. Lucky, raccoons are immune.”
#
#
#
# The two guards behind Ralph chuckled.
#
#
#
# "You know what I'm talking about. The disappearances. Tell me what you know and I'll make sure the authorities are lenient. I’ve got good information you’re helping the aliens abduct them.”  Ralph sneered.
#
#
# “Aliens… authorities?!” Jeff blurted out no longer able to contain her laughter. “I’m only offering what your aliens have left behind for them, without trapping them. See for yourself.”
#
#
#
# The old, one-eyed raccoon brought out a pellet and placed it on the crate that stood between Ralph and Jeff.
#
#
#
# “Look closer,” said Jeff stepping back.
#
#
#
# Ralph took a step closer and sniffed the pellet. It was chicken and catnip scented. There was something else there that he couldn’t place his paw on, something familiar. Satisfied, Ralph asked, “Where did you get this?”
#
#
#
# “Wouldn’t you like to know,” said one guard as both of them stepped closer.
#
#
#
# “Now, now. If I told you that would be bad for business. Ah! There is a way you can find out,” said Jeff waving a paw in the air in revelation.
#
#
#
# Ralph didn’t trust this raccoon. He trusted none of them, but especially not Jeff. “And how is that?” he asked.
#
#
#
# Jeff brought her paws down and placed them on the make-shift table, leaning forward. With a grimace on her face exposing her sharp teeth she growled, “Eat it.”
#
#
#
# The proximity detector on Ralph’s collar beeped faster and faster.
#
#
#
# “He sounds like he’s got a bomb,” said the guard.
#
#
#
# “He hasn’t got a bomb. Shut up and do your job!” snarled Jeff hurling a trinket at the creature.
#
#
#
# The guards pressed up against Ralph showing their long, sharpened claws.
#
#
#
# “Eat it!” Jeff pounded her fists on the table making the pellet bounce.
#
#
#
# They hemmed in Ralph. He didn’t want to endanger Archie and Milton so he ate the pellet. He realized the mystery ingredient was a sedative. It would take more than one pellet to knock out a cat of his size but it would still hinder his thinking. He wouldn’t be able to protect his partners from these bandits.
#
#
#
# Jeff was furious. Her teeth bared and waving her paws around, “Those vile creatures in their space suits come here every morning before sunrise with their beams of light shining everywhere. This place is lit up like daytime. They take the traps with the cats and raccoons. Oh yes, I bet you didn’t count on that one. But raccoons don’t come back like your cats do. I’m willing to bet those monsters will come for you too. The fewer cats the better, then the rest of us can get back to living our lives!”
#
#
#
# The noise of the collar increased in speed until it was just a single tone. He laid his ears back in response to the noise, it was really loud. And then it stopped. Ralph knew Milton and Archie were close by.
#
#
#
# A bell rang out. “Your aliens have arrived. Come on fellas, let’s beat feet!” said Jeff.
#
#
#
# Ralph watched them escape through a small hole. He knew raccoons could collapse their spines but had never seen it.
#     """
# )
# # SCENE 5
# scene5 = noveler("scene").create_scene(
#     story_id=story.id, chapter_id=chapter2.id,
#     title="November 23, 2016, 9:36 pm, Frances’ laboratory",
#     description=None,
#     content="""After sending the last message, Frances puzzled over how to listen to what was happening with the agents. The radio signal would only reach so far. On the transmeowter were lights, buttons, a small screen, and switches. A different light for each collar showed her if the agents were on the move. Frances could see how far away they were from 121st Street Clowder Headquarters on a digital map. Headquarters was anywhere on either Millie’s or Maggie’s property. They were such good friends they removed the fence between their yards.
#
#
# Frances, in the middle of experimenting with the transmeowter, thought she broke something as a series of chirps came from the little speaker. A series of 3 scratches and a very long chirp. The signal was coming from Ralph’s collar. Right now she could only send Morris code and receive scratch cipher. She needed to hear what was going on in the field. If she rerouted the send from the Morris code button to the microphone on the transmeowter she could reverse the polarity turning it into a speaker. But would it work? She had installed two-way devices on all of their collars but would have to signal the chip to listen instead of play. There was only one way to do that, bite-nary.
#
#
#
# Frances was just learning bite-nary. Grabbing a length of wire to suit her needs, she chewed some of the wrappings off exposing the metal. She attached one end to the send button. Pulling out her notes from communication class, Frances thought she'd better write out the signal so she would have a better chance of getting it right. If she didn't get it right, Jeff and her gang could hurt Ralph and the others. Electrocuting herself was also a possibility.
#
#
# The dumbo eared, brown and white rat grabbed the coated wire on each side of the bare metal, grounded her body, looked at her message and touched her tongue on the wire to interrupt the electricity. She had to send out a greeting message so the chip would be alert. Her ankles buzzed as the weak current flowed through her body. Next was the instructions to flip the poles so that the speakers would become microphones. She finished when she sneezed biting her tongue and breaking the wire. The electrical shock knocked her off her paws. What if it hadn’t worked?  Squeezing her eyes shut hard to stop the room spinning and to get rid of the stars that filled her sight. Her hearing became fuzzy with a crackling sound interrupted by whooshing.  Her head filled with static and popping noises followed by silence. This is terrible, she couldn’t go deaf. She thought about poor Ralph and the others mangled by who knows what or fallen down a storm drain or any other terrifying thing that could happen. Frances imagined Jeff arguing and her gang attacking the agents. Trying to get up again she knocked over her stool at the same time she heard voices. Great. Frances thought she’d caused serious brain damage. But one of them sounded like Ralph.
#
#
#
#  “I’m only offering what your aliens have left behind for them, without trapping them. See  for yourself.” said a female voice
#
#
#
#  “Where did you get this?” said Ralph
#
#
#
# The voices were interrupted by static, whistling and popping noises coming from the transmeowter’s speakers.
#
#
#
#  “He hasn’t got a bomb. Shut up and do your job!” said the female voice
#
#
#
#  “She’s a pretty distraction,” said Milton
#
#
#
#  “She’s a Burmese; a brick wrapped in silk, Milt,” said Archie.
#
#
#
#  “Eat it!” shouted the female voice
#
#
#
# Everything was a jumble. It dawned on Frances what she heard was coming from the agents’ collars. It worked and she wasn’t deaf! Frances jumped to her feet to look at the map. “No wonder it was confusing,” she said. Ralph  wasn’t with Archie and Milton, but they were moving towards him. Soon, they’d be in trouble too. She scurried out of her laboratory to tell Millie.
#     """
# )
# # SCENE 6
# scene6 = noveler("scene").create_scene(
#     story_id=story.id, chapter_id=chapter2.id,
#     title="November 23, 2016, 9:42 pm, Two blocks from The Stinky Possum Pub.",
#     description=None,
#     content="""“Her name is Minka,” said Milton as he caught up to Archie. He sat at the corner waiting to cross the street.
#
#
#
# “Her name oughta be trouble. Did you understand what she was saying?” asked Archie.
#
#
#
# “It was strange, but it’s cute. She is different from any other cat I’ve met.”
#
#
#
# Archie sighed and they both crossed the street. They didn’t speak the rest of the way. Their collars beeped faster as they approached the alley behind the Stinky Possum Pub where Tiff said Ollie was last seen. Ralph was nearby.
#
#
#
# “We must be near Ralph,” said Milton.
#
#
#
# “You don’t say,” said Archie.
#
#
#
# “Well, I don’t see him anywhere. Do you think he’s looking for Ollie, too?”
#
#
#
# “Perhaps, Milton. He had a tip from Frances’ brother. Ralph said he was going talk to some cats about disappearances of others in the area. Ollie was just one of many who has gone missing.”
#
#
#
# “It’s so scary and sad,” said Milton
#
#
#
# Archie’s put his nose to the ground. He picked up Ralph’s scent and followed it to a storage shed behind the pub. The shed stunk of raccoons. Milton and Archie could hear talking and leaned in closer.
#
#
#
#  “Your aliens have arrived. Come on fellas, let’s beat feet!”
#
#
#
# Alerted by scratching noises and footsteps, Milton and Archie saw four raccoons leave the shed.
#
#
#
# “Take care of your partner,” said a familiar female voice coming from the tall grass behind them. Minka continued, “Backup is here, I’ll catch up to you later.” She climbed up the tree the raccoons used to escape and followed their trail. Raccoons could do serious damage to a lone cat, she had to be careful.
#
#
#
# Milton and Archie stood up and pushed the shed door open. Sitting there in the dark with a stupid grin on his face was Ralph.
#
#
#
# “Whew!” said Archie blinking back tears, “You are ripe.”
#
#
#
# "Hey, guys!" slurred Ralph, happy to see them.
#
#
# The shed was lit up with beams of light. They weren’t fast enough to help Ralph escape.
#
#
# “It’s happening!” said Ralph, “I have to go with them.”
#
#
#
# “Are you crazy?” asked Milton
#
#
#
# “That’s debatable,” said Archie looking over his partner whose fur was matted, he covered with leaves, grass, and stunk of cat urine.
#
#
#
# “I’ll be okay,” said Ralph, “They will take me and I will find the others.”
#
#
#
# “Yep,” said Milton, “he’s crazy.”
#
#
#
# “That might work,” said Archie, “we’ll follow behind.”
#
#
#
# Archie and Milton turned toward the tall grass behind the shed, “Oh, Ralph? Look for a fella named Ollie. His partner Tiff sent us to find him. Remember, his name is Ollie.”
#
#
#
# Ralph nodded his head, his body swayed and he sang. “Olly, Olly, Oxen free!” He couldn’t remember where he heard it but it sounded funny.
#
#
#
# Silvery white beings with masks and goggles picked up Ralph. He was so relaxed they didn't even have to trap him but held him at arm's length and put him in a carrier of some sort.
#
#
# Ralph looked out from the carrier unaware he was being carried. The effect of the drug was in full force. He felt like he was floating or flying. They loaded him up into the vehicle he shared with two other cats who were asleep.
#
#
#
# “This must be their ship!” said Ralph, drooling a little as he settled down and fell asleep too.
#     """
# )
# # CHAPTER 3
# chapter3 = noveler("chapter").create_chapter(
#     story_id=story.id, title="Part III: Cell Block – C for cat",
#     description=None
# )
# # Scene 7
# scene7 = noveler("scene").create_scene(
#     story_id=story.id, chapter_id=chapter3.id,
#     title="November 24, 2016, 1:08 am, Mumford Avenue Veterinary Hospital",
#     description=None,
#     content="""Ralph woke up in a cage. He tried to stand up but the room spun, so he leaned to look out instead. He was in a small room full of these cell-like cages. Some had cats in them, some rabbits and some were empty.
#
#
#
# “Ollie?” he said, “Is Ollie here?”
#
#
#
# “Quiet down,” said an older female voice, “we’re tryin’ to sleep in here.”
#
#
#
# “Sorry, this is important,” said Ralph.
#
#
#
# No one heard Minka come into the holding area. Hoping to learn more about this agent and her case she sat down to listen below Ralph’s cell.
#
#
#
# “So is sleep!” said the same voice.
#
#
#
# “Excuse me,” said a quiet voice coming from the cell next to Ralph, “my name is Oliver. But some cats call me Ollie. Well, just one cat. Who are you?”
#
#
#
# “My name is Ralph and I am the lead investigator of the 121st Street Clowder of the Domesticated Investigation Bureau. Your partner Tiff came to us, told us you were missing. Are you all right?”
#
#
#
# Ollie wasn’t sure he should trust this Ralph cat. “Oh, my sweet Tiff. I knew it wasn’t a good thing to leave her there. I wanted her to rest,” said Ollie, “As for me, I’ll manage.”
#
#
#
# “You'll be with her soon. My team has been working very hard on these disappearances. Would you mind answering a few questions?" asked Ralph.
#
#
# “We don’t have anything better to do with our time,” said Ollie.
#
#
#
# “You could sleep!” said the female cat.
#
#
#
# Ralph waited for things to quiet down. He then rolled over onto his side so he could be closer to Ollie’s cell. Whispering he asked, “Can you tell me what happened? What led up to you being caught?”
#
#
#
# “Well, as much as I can remember. Tiff has been having such a hard time sleeping. All the sickness going around keeps her awake. She said she saw shadow monsters and then a few days later more cats would get sick. I thought she was imagining things. I couldn’t watch her waste away and she was so afraid. So, I went to the alley behind The Stinky Possum Pub. There were rumors a dumpster dealer there that had something that would help Tiff sleep.”
#
#
#
# “Jeff?” asked Ollie
#
#
#
# “Yes. What a nasty creature. I couldn’t afford her prices, I left and went searching on my own.”
#
#
#
# “Do you know where they got the pellets?”
#
#
#
# “Oh, yes. They were stealing from traps left out to capture us ferals. I don’t know how they got them without being trapped themselves, but they did. I followed a team after I left Jeff’s shed. They were almost done collecting them when the people arrived and scared them off. I took a chance and went for a pellet they’d missed but I was trapped. That’s the last thing I remember.”
#
#
#
# “Aren’t you a doll?” said a deep male voice. “Come here and let me sniff you.”
#
#
#
# Ralph looked to find a dark cat sitting on the floor just below him. She was outside of the cells. She turned and swatted at the cell she sat in front of striking a big rabbit’s cell door.
#
#
#
# “Ugh! Gross,” she said.
#
#
#
# “Are you spying on me?” asked Ralph
#
#
#
# Minka jumped on a stool in the center of the room. “I am on your side, Ralph. My name is Minka. As a DIBs agent, I have been investigating the spread of illness and disease among the cats, which has been faster than normal."
#
#
# Ralph asked, “What do you think causes this?”
#
#
#
# "Raccoons," said Minka, "they've been competing with cats for food and water. At first, they were upset that humans were taking more protective measures with their trash because it was attracting sick cats. But then they learned cats were dying and being removed from the area. So one raccoon decided it would be in the best interest of all the raccoons if they helped the cats get sick."
#
#
# “And they’re immune,” said Ralph his thinking becoming clearer.
#
#
#
# Then when the doctors trapped the cats to treat them and help them the raccoons became even bolder. The vets released the cats back into the alley after they healed. And that one raccoon made it her mission to stop cats being taken. So she stole pellets and infected them with what is making cats sick. She tells everyone what a hero she is for keeping cats from being abducted and they believe her.”
#
#
# “Let me guess, Jeff?” asked Ralph.
#
#
#
# “Oh, dear!” said Ollie, “I ate a pellet.”
#
#
#
# "Yes, but you ate one from a trap so you're safe and they gave you a shot to prevent you from getting sick while you were here," said Minka.
#
#
# “How do you know?” asked Ollie
#
#
#
# “My handler is a doctor and works here,” said Minka. “These abductions have been done to save the cats of Peed Street.”
#
#
#
# "Save them? They are scarred for life physically and mentally. Their ability to have a family has been taken from them without their permission. You’ve taken away any rights they have." said Ralph.
#
#
# “And they are alive. Spaying and neutering were the only ways I could get my handler to agree to help stop the spread of sickness,” said Minka, “the raccoons are trying to kill us, Ralph.”
#
#
#
# Ralph was about to argue but the door swung open and a human entered along with Millie.
#
#
#
# “There you are, Ralph! Thank goodness Frances told me you were in trouble. I picked up Archie and Milton on the way here, and Minka." said Millie who got a good look and whiff of Ralph. "Wow! You're one stinky kitty. You must be groomed before you can come home. I'll call Maggie to pick up Archie and Milton, in the meantime, you will get a good bath."
#
# Ralph cringed at the thought but he would rather smell like a baby human now than how Peed Street got its name.
#     """
# )
# # SCENE 8
# scene8 = noveler("scene").create_scene(
#     story_id=story.id, chapter_id=chapter3.id,
#     title="November 24, 2016, 7:50 pm, 121st Clowder Headquarters.",
#     description="",
#     content="""Later that evening, after being brushed and bathed and brushed again, Ralph felt more like himself. He was glad to be home again and gave Frances a good head bonk, knocking her off her feet. She climbed onto his back and they headed to join Milton and Archie at Maggie’s house.
#
#
#
# “Mr. Fancypants,” said Archie, “look at you!”
#
#
#
# “I thought you were more of a brown tabby but now you look more silver. You smell like a baby’s butt,” said Milton.
#
#
#
# “Good to see you two also," said Ralph. "Now, shall we have a meeting? Thanks to all our efforts, Ollie has been returned to Tiff safe and sound. I have referred him to Flando if he needs to talk to someone about what happened. Flando has been informed of the cause of the disappearances and has our full support in his efforts to help those who need it. In return, he is encouraging the cats to volunteer to be vaccinated and spayed or neutered."
#
#
# “Millie and Maggie have the details on that program and will speak to Minka’s former handler about changing procedures to make the experience less traumatic.” said Archie.
#
#
#
# “Former handler?” asked Ralph.
#
#
#
# “Yes," said Minka who had joined them, "I have my forever home with Archie and Milton which will take getting used to but I can handle it if I don't die from boredom first."
#
#
# “Maggie has placed her on temporary quarantine,” said Milton, “two weeks.”
#
#
#
# “Oh, dear,” giggled Frances.
#
#
#
# “Milton isn't so bad but Archie is staler than a used dryer sheet. I know how valuable they are to the team," said Minka, "they are very dedicated to the work. I admire that in a cat."
#
#
# Ralph was sure Archie stuck his tongue out at her. “That’s enough. I’ve received orders that Minka is to be a part of the 121st Street Clowder. She has done amazing work that needs to continue. We can pick up the slack while she is in quarantine.”
#
#
#
# Minka just nodded.
#
#
#
# “Good,” said Milton, “Let’s celebrate another job well done.”
#
#
#
# They all made their way inside to catch the evening DIBs report.
#
#
# “It's time to catch the news," said Ralph.
#     """
# )

def chat(prompt):
    """Example of how to use the chat method of the ChatController class.

    response = noveler("assistant").chat('Why is the sky blue?')

    The method is a wrapper around the chat method of the Ollama Client class. It takes a list of messages as input and
    returns a list of responses. The messages are dictionaries with two keys: role and content. The role key is a string
    that can be either 'user' or 'assistant'. The content key is a string that contains the message history of the chat
    session. The ollama system allows keeping models in memory for an arbitrary duration, but my concept for this app is
    that it could share an ollama server on a local network, and that means freeing up resources and making all
    interactions "one shot" interactions. This is why the keep_alive parameter is set to 0. There is overhead incurred
    loading the model with each call, but chat models are relatively small and load quickly.

    THAT BEING SAID - there's no way to integrate the ollama system with your own application without the use of either
    asynchronous programming or threading. No one is going to want to stop work altogether to wait for every response
    from the ollama models, as that would only magnify the latency inherent in running models on end-user hardware.
    """

    response = noveler("assistant").chat(prompt=prompt, temperature=1.0)

    print(response)


# t_chat = threading.Thread(target=chat, args=("Give me five good reasons to legalize marijuana.",))
# t_cube = threading.Thread(target=print_cube, args=(10,))
# t_square = threading.Thread(target=print_square, args=(10,))
#
# t_chat.start()
# print("Made remote call to ollama...")
# t_cube.start()
# print("Ran the cube function...")
# t_square.start()
# print("\nRan the square function...")
# print("Probably still waiting on that chat response...")
#
# t_chat.join()
# t_cube.join()
# t_square.join()
#
# print("Now all threads are done.")
