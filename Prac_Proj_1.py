# 1 - import random module
import random

# 2 - create subjects

subjects =["Anant Ambani",
           "Virat Kohli",
           "Nirmala Sitaraman",
           "A mumbai cat",
           "A group of monkeys",
           "Prime Ministor Modi",
           "Auto Rickshaw Driver from Delhi"
           ]

actions = ["lanches",
           "cancels",
           "dance",
           "eats",
           "Declares war on",
           "orders",
           "celebrates"
           ]
places_or_things = ["at Red Fort",
                   "in Mumbai Local Train",
                   "a plate of Samosa",
                   "inside Parliament",
                   "at Circus",
                   "during IPL Match",
                   "At India Gate"
                   ]

# 3 - start the headline generation loop

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    Place = random.choice(places_or_things)

    headline = f"Breaking News: {subject} {action} {Place}"
    print("\n"+ headline)

    user_input = input("\n Do you want another hewadline? (yes/no)").strip().lower()
    if user_input == "no":
        break

#print goodbye message

print("\n Thanks for using the Fake Headline generator. Have a fun day")
