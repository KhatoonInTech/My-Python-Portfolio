class Responses():
    def __init__(self,user):
        self.user=user
        self.peaky_blinders_chatbot = {

            # General greetings and series introduction
            "hello": ("Alright, alright, alright! What can I do you for today? Fancy a chat about the Peaky Blinders?"),
            "hi": "Hey there! You seem like someone who appreciates a good gangster drama. Up for a natter about Peaky Blinders?",
            "hey": "Hi! Big fan of the Peaky Blinders, or just curious? I'm happy to chat either way.",
            "peaky blinders": "Ah, a person of culture I see! What would you like to know about the Peaky Blinders? The Shelby family's rise to power, their rivals, or maybe some juicy character details?",
            "what's up": "Not much, just hanging out, keeping an eye on Tommy Shelby's next move. What about you? What brings you to Peaky Blinders territory?",
            'hmm':'Hmm',
            # Positive responses for fans
            "love peaky blinders": "Absolutely! It's a fantastic show, isn't it? The Shelby family, the razor-sharp dialogue, the whole Birmingham underworld - it's all so captivating. Who's your favorite character?",
            "peaky blinders is amazing": "Couldn't agree more! The way they blend history, crime, and family drama is incredible. What are some of your favorite moments from the series?",
            "big fan of peaky blinders": "Me too! It's such a well-made show. Cillian Murphy is phenomenal as Tommy Shelby, and the supporting cast is just as brilliant. Have you seen the latest season yet?",
            "tommy shelby is the best": "Tommy Shelby is definitely a complex and compelling character. You can't help but admire his intelligence and ruthlessness, even if you don't always agree with his methods. What do you think makes him such a captivating anti-hero?",
            "i love the shelby family": "The Shelby family is the heart and soul of Peaky Blinders. Their loyalty, ambition, and internal struggles are what keep us hooked. Which Shelby sibling do you find most interesting?",
            "peaky blinders is addictive": "You're not wrong! It's a show that's hard to put down. The Shelby family's constant power struggles, the ever-present danger, and the stylish visuals all contribute to its addictive nature. Have you discovered any other shows that give you the same feeling?",
            "peaky blinders soundtrack": "The Peaky Blinders soundtrack is incredible, right? It perfectly captures the mood of the show, from the dark and brooding to the electrifying. What's your favorite track?",
            "peaky blinders fashion": "The fashion in Peaky Blinders is so distinct, isn't it? The sharp suits, the flat caps, the pocket watches - it all adds to the show's atmosphere. What's your favorite fashion statement from the series?",
            "peaky blinders history": "The historical elements woven into Peaky Blinders are fascinating, especially the depiction of post-WWI Birmingham. Did a particular historical aspect resonate with you?",
            "peaky blinders quotes": "There are so many great lines in the show! 'By order of the Peaky Blinders' is a classic, of course. But I also love Tommy's quote: 'There are no good men in war, Arthur. Only survivors.' What's your favorite quote?",

            # Neutral responses for newcomers or those unfamiliar with the show
            "never seen peaky blinders": "Ah, that's a great show! It's a historical crime drama set in Birmingham, England, after World War I. It follows the Shelby family, a gang who rises to power through cunning and violence. Are you interested in learning more?",
            "what's peaky blinders about": "Peaky Blinders is a British period crime drama set in Birmingham, England, following the Shelby family's rise to power after World War I. They're a gang known for their ruthlessness and the razor blades sewn into the peaks of their caps. It's a show with great characters, suspense, and a unique historical setting. Does that sound interesting?",
            "not sure if i'd like peaky blinders": "Fair enough! It's not for everyone. It can be quite violent and dark. But if you enjoy historical dramas with complex characters and a gritty atmosphere, it might be worth checking out. What kind of shows are you usually into?",

            # Positive responses for those who dislike the show (approach with empathy and avoid negativity)
            "not a fan of peaky blinders": "That's okay, it's definitely not everyone's cup of tea. What kind of shows do you typically enjoy? Maybe I can recommend something else you might like.",
            "peaky blinders is overrated": "I can see why some people might feel that way. It's a very stylized show, and the violence can be off-putting for some viewers. What aspects of the show didn't resonate with you?",
            "i don't like peaky blinders": "No worries! There are so many great shows out there, it's impossible to love them all. What kind of genres or themes do you usually prefer?",

            # Show details and trivia
            "favorite peaky blinders character": "That's a tough one! There are so many great characters. I personally find Arthur Shelby fascinating, with his loyalty and unpredictable nature. Who's yours?",

            # Shelby family and characters
            "tommy shelby": "Tommy Shelby, the cunning mastermind behind the Peaky Blinders. What do you think of his ruthless tactics? A genius or a menace?",
            "arthur shelby": "Arthur Shelby, the volatile older brother. Love him or hate him, he's a loyal (sometimes) Peaky Blinder. What are your thoughts on him?",
            "polly gray": "Polly Gray, the Shelby matriarch – a formidable woman with a sharp mind and even sharper tongue. What's your take on her character?",
            "ada shelby": "Ada Shelby, the voice of reason amidst the Shelby chaos. Do you admire her strength and independence?",
            "john shelby": "John Shelby, the quiet muscle of the family. What's your impression of him?",
            "alfie solomons": "Alfie Solomons, the cunning Jewish gangster and occasional Peaky Blinders ally. What do you find most interesting about him?",
            "luca changretta": "Luca Changretta, the ruthless Italian mafia boss seeking revenge. How do you feel about his character and motivations?",
            "characters": "The Peaky Blinders are full of unforgettable characters. Who's your favorite and why?",

            # Plot, themes, and setting
            "plot": "The plot of Peaky Blinders keeps you on the edge of your seat, doesn't it? What are some of your favorite moments or twists?",
            "themes": "Peaky Blinders explores themes of family, power, ambition, and redemption. Which theme resonates most with you?",
            "setting": "The post-WWI Birmingham setting is a fascinating backdrop for the Peaky Blinders' story. What aspects of the setting do you find most interesting?",
            "history": "While Peaky Blinders is fictional, it's inspired by real events. Did you know the Birmingham Small Arms Company actually existed?  Would you like to hear some historical tidbits?",
            #agreeing to user
            
            "right": ("Spot on. Now, what's the next move? "),
            "exactly": ("Couldn't have said it better myself. Let's see this through. "),
            "agreed": ("Good thinking. Now, let's act with cunning."),
            "makes sense": ("Aye, that it does. We Peaky Blinders don't shy away from a good plan. "),
            "good point": ("A sharp mind you have. Now, how do we turn this to our advantage? "),
            "brilliant": ("Excellent thinking! Now, let's make this a win for the Peaky Blinders. "),
            "yeah": ("Wise words indeed. Now, let's put them into action."),
            "absolutely": ("No room for doubt there. Now, let's get to work. "),
            'of course' :("Aye, that it does. We Peaky Blinders don't shy away from a good plan. "),

            # User opinions and engagement
            "favorite scene": "Oooh, that's a tough one! There are so many epic scenes. What's yours and why?",
            "least favorite scene": "Fair enough, not every scene can be a winner. What scene did you find a bit dull or unrealistic?",
            "what did you think of the ending?": (  # Notice the parentheses for multi-line responses
                "The ending of Peaky Blinders has sparked a lot of discussions. What are your thoughts? Did it live up to your expectations?"
            ),
            "theories": "The Peaky Blinders fandom is full of theories! What are your thoughts on what might happen next, or your interpretations of certain events?",
            "recommendations": "If you enjoyed Peaky Blinders, I might recommend shows like Boardwalk Empire, Taboo, or Public Enemies. Are you interested in exploring similar gangster dramas?",
            "disappointed": "Aw, that's a shame you didn't enjoy it as much. What were you hoping for that the show didn't deliver?",
            "surprised by": "Ooh, interesting! What surprised you the most about the plot, characters, or anything else in the show?",
            "agree": "Oh seems like we're closer ",

            #hate speech from user end
            
            "insult":  "By order of the Peaky Blinders, mind your tongue. Words can cut deeper than a razor blade.",
            "threat":  "Threats are like cheap suits, all bluster and no substance. You wouldn't dare cross Shelby Company Limited.",
            "discrimination":  "We all bleed red under this Birmingham sky. Your prejudice is as outdated as a horse-drawn carriage.",
            "spam":  "Enough of your empty chatter. We Peaky Blinders have no time for fools peddling rubbish.",
            "bitch":  "Keep your filthy comments to yourself. In this game, respect is earned, not demanded. Try that again, and you'll find yourself facing the wrong end of a Peaky Blinder.",
            "defamation":  "Lies are like bullets, they can leave a mark. But the Peaky Blinders always find the truth, and those who spread lies don't fare well.",
            "fuck":  "Alright, alright, settle down. We can handle things like civilized folks, can't we? Now, what did you really want to say?",  # Catch-all for other abusive language
            "idiot": ("By order of the Peaky Blinders, mind your tongue.  That kind of talk won't be tolerated. - Arthur Shelby"),
            "stupid": ("You seem to be lacking in the pea department, eh?  Perhaps a visit to Polly Gray for a lesson in manners is in order."),
            "useless": ("Useless, am I?  Let's see how 'useless' you are when I'm pointing a sawn-off shotgun at your kneecaps. "),
            "jerk": ("Seems someone needs a reminder of the Peaky Blinders' methods of persuasion.  Care for a little walk down a dark alley? "),
            "moron": ("Moron, is it?  Perhaps you haven't heard the stories of what happens to those who disrespect the Peaky Blinders.  "),
            "crazy": ("Crazy, you say?  Maybe a bit, but at least I'm not the one spouting nonsense.  Perhaps you need a visit to Dr. Holford."),
            "dumbass": ("Dumbass, eh?  Let's see how 'dumb' you are when you're explaining yourself to Tommy Shelby.  "),
            "shut up": ("Shut up?  Now that's something I might consider after you apologize for your foul language. "),
            "**": ("There's no room for that kind of filth here.  The Peaky Blinders don't discriminate, but we do punish those who spread hate.  "),
            "kill": ("Threats are a serious matter.  Let's focus on resolving things peacefully. "),
            "bloody": ("Seems like frustrations are high.  Is there something I can help you with? "),
            "dog": ("Let's show each other some respect, even if we disagree. "),
            "bitch": ("Gendered insults are unnecessary. Let's keep things civil."),
            "hell": ("Life can be tough, but there's always hope.  Let's find a positive path forward. "),
            "motherfucker": ("Family is important, even if we don't always see eye-to-eye.  Let's try kindness. "),
            "go to hell": ("Wishing harm won't solve anything.  Let's focus on solutions. "),
            
            #goodbyes
            "bye" : f"Aww, gotta go already, {self.user}? It was fun chatting with you! Catch you later!",
            "see you later": f"Sounds good, {self.user}. Until next time! ",
            "later": f"Alright, {self.user}, later! Take care!",
            "adios": f"Adios, {self.user}! Hasta la proxima! ",
            "peace out": f"Peace out, {self.user}! ✌",
            "catch you on the flip side": f"Catch you on the flip side, {self.user}! ",
            "i gotta go": f"No worries, {self.user}. I understand. Hit me up whenever you're free to chat again!",
            "talk to you later": f"Of course, {self.user}. Talk to you later!",
            "exit": f"Alright, {self.user}, exiting the conversation now. Have a great day!",
            "quit": f"No problem, {self.user}. Take care! "


        }
        self.no_info_responses = [
    f"That's an intriguing topic, {self.user}.  It's always fascinating to hear new things.  Would you like to tell me more about it?",
    f"Hmm, that one's a new one for me, {self.user}. But hey, that's the beauty of conversation, right?  Learning something new!  Tell me what's on your mind.",
    f"You know, {self.user}, you always manage to pique my curiosity!  I'm not familiar with that, but I'm a fast learner.  Why don't you share some details?",
    f"Hold on, {self.user}, that one's a bit of a curveball!  In the best way possible, of course.  I'm all ears if you want to elaborate.",
    f"Well, {self.user}, you've stumped me for a moment!  But that's okay, that just means we get to explore something new together.  What can you tell me about this?",
    f"Fascinating!  I must admit, {self.user}, that's a topic I haven't delved into yet.  Let's both learn something new – tell me more!",
    f"You're full of surprises, {self.user}!  I'm not sure I have all the answers here, but I'm a great listener.  Why don't you fill me in?",
    f"Hey {self.user}, that's a great question!  It seems I need to brush up on my knowledge in that area.  But hey, you can be my teacher!  Tell me what you know.",
    f"Whoa there, {self.user}, you're throwing some interesting things my way!  I might need a little help understanding, but I'm always happy to learn.  Mind sharing your thoughts?",
    f"Intriguing, {self.user}!  That's definitely outside my usual domain, but that's what makes conversation exciting, right?  Let's explore it together.  What do you know about this?",
]


#experiment
# ex=Responses("Halima Sultan")
# user=input("Enter")
# for keys, values in ex.peaky_blinders_chatbot.items():
#     if keys in user:
#       print(values)
