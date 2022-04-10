from re import X
from PIL import Image 
from IPython.display import display 
import random
import json
import os

# Each sugar pretzel is made up of a pretzel, choclate coating ant toppings
#The weightings for each trait drive the rarity and add up to 100%

pretzel = ["Classic"]
pretzel_weights = [100]

salt = ["Classic Salt", "No Salt"]
salt_weights = [50, 50]

half_chocolate_coat = ["Half Brown", "Half White", "No Chocolate"]
half_chocolate_weights = [45, 45, 10]

full_chocolate_coat = ["Full Brown", "Full White", "No Chocolate"]
full_chocolate_weights = [45, 45, 10]

topping_half = ['Half Sprinkles Brown', 'Half Sprinkles White', 'Half Sprinkles Rainbow', 'Half Sprinkles PretzelDAO', 
    'Half Dots Brown', 
    'Half Dots White', 
    'Half Dots Rainbow', 
    'Half Dots PretzelDAO', 
    'Half Stripes Brown', 
    'Half Stripes White', 
    'Half Stripes Rainbow', 
    'Half Stripes PretzelDAO',
    'No Topping']
topping_half_weights = [9 , 9 , 6 , 3 ,9, 9, 6 ,3 ,9, 9 , 6 , 3, 19]

topping_full = ['Full Sprinkles Brown', 'Full Sprinkles White', 'Full Sprinkles Rainbow', 'Full Sprinkles PretzelDAO', 
    'Full Dots Brown', 
    'Full Dots White', 
    'Full Dots Rainbow', 
    'Full Dots PretzelDAO', 
    'Full Stripes Brown', 
    'Full Stripes White', 
    'Full Stripes Rainbow', 
    'Full Stripes PretzelDAO',
    'No Topping']
topping_full_weights = [9 , 9 , 6 , 3 ,9, 9, 6 ,3 ,9, 9 , 6 , 3, 19]

#Classify traits

pretzel_files = {
    "Classic": "classic"
}

salt_files = {
    "Classic Salt":"salt",
    "No Salt": "no_salt"
}

chocolate_coat_files = {
    "Half Brown": "half_brown",
    "Half White": "half_white",
    "Full Brown": "full_brown",
    "Full White": "full_white",
    "No Chocolate": "no_chocolate"
}


topping_files = {
    'Half Sprinkles Brown': "half_sprinkles_brown",
    'Half Sprinkles White': "half_sprinkles_white",
    'Half Sprinkles Rainbow': "half_sprinkles_rainbow",
    'Half Sprinkles PretzelDAO': "half_sprinkles_pretzelDAO",
    'Half Dots Brown': "half_brown",
    'Half Dots White': "half_dots_white",
    'Half Dots Rainbow': "half_dots_rainbow",
    'Half Dots PretzelDAO': "half_dots_prretzelDAO",
    'Half Stripes Brown': "half_stripes_brown",
    'Half Stripes White': "half_stripes_white",
    'Half Stripes Rainbow': "half_stripes_rainbow",
    'Half Stripes PretzelDAO': "half_stripes_pretzelDAO",
    'No Topping': "no_topping",
    'Full Sprinkles Brown': "full_sprinkles_brown",
    'Full Sprinkles White': "full_sprinkles_white",
    'Full Sprinkles Rainbow': "full_sprinkles_rainbow",
    'Full Sprinkles PretzelDAO': "full_sprinkles_pretzelDAO",
    'Full Dots Brown': "full_dots_brown",
    'Full Dots White': "full_dots_white",
    'Full Dots Rainbow': "full_dots_rainbow",
    'Full Dots PretzelDAO': "full_dots_pretzelDAO",
    'Full Stripes Brown': "full_dark_stripes",
    'Full Stripes White': "full_stripes_white",
    'Full Stripes Rainbow': "full_stripes_rainbow",
    'Full Stripes PretzelDAO': "full_stripes_pretzelDAO",
}


## Gernerate Sugar Pretzel

def create_pretzle():

    new_pretzle = {}
    

    new_pretzle ["Pretzel"] = "Classic"
    new_pretzle ["Salt"] = random.choices(salt, salt_weights)[0]
    if new_pretzle["Salt"] == "No Salt" :
        new_pretzle ["Chocolate_Coat"] = random.choices(full_chocolate_coat, full_chocolate_weights)[0]
        if new_pretzle["Chocolate_Coat"] == "No Chocolate" :
            new_pretzle ["Topping"] = "No Topping"

        else:
            new_pretzle ["Topping"] = random.choices(topping_full, topping_full_weights)[0]
        
    else :
        new_pretzle ["Chocolate_Coat"] = random.choices(half_chocolate_coat, half_chocolate_weights)[0]
        if new_pretzle["Chocolate_Coat"] == "No Chocolate" :
            new_pretzle ["Topping"] = "No Topping"
        else :
            new_pretzle ["Topping"] = random.choices(topping_half, topping_half_weights)[0]
    
    return new_pretzle
    


## Generate Sugar Pretzle Banners

TOTAL_BANNERS = 1 # Number of random unique images we want to generate
PRETZELS_PER_BANNER = 35 #Number of Pretzels in Picture


all_banners = [] 

# A recursive function to generate unique banner combinations
def create_new_banner():
    
    new_banner = [] #

    # For each position in banner create Pretzel
    i=0
    while i < PRETZELS_PER_BANNER:
        new_banner.append(create_pretzle())
        i=i+1

    if new_banner in all_banners:
        return create_new_banner()
    else:
        return new_banner
    
    
# Generate the unique combinations based on trait weightings
for i in range(TOTAL_BANNERS): 
    
    new_sugar_pretzle_banner = create_new_banner()
    
    all_banners.append(new_sugar_pretzle_banner)


# Returns true if all images are unique
def all_banners_unique(all_banners):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_banners)

print("Are all banners unique?", all_banners_unique(all_banners))


# Add token Id to each banner
i = 0
for item in all_banners:
    item[i]["tokenId"] = i
    i = i + 1
   
# Get Trait Counts

pretzle_count = {}
for item in pretzel:
    pretzle_count[item] = 0
    
salt_count = {}
for item in salt:
    salt_count[item] = 0

chocolate_coat_count = {}
for item in half_chocolate_coat:
    chocolate_coat_count[item] = 0
for item in full_chocolate_coat:
    chocolate_coat_count[item] = 0
    
topping_count = {}
for item in topping_half:
    topping_count[item] = 0
for item in topping_full:
    topping_count[item] = 0
    

for banner in all_banners:
    for pretzel in banner:
        pretzle_count[pretzel["Pretzel"]] += 1
        salt_count[pretzel["Salt"]] += 1
        chocolate_coat_count[pretzel["Chocolate_Coat"]] += 1
        topping_count[pretzel["Topping"]] += 1
    
#print(pretzle_count)
#print(salt_count)
#print(chocolate_coat_count)
#print(topping_count)


#### Generate Pretzels

#os.mkdir(f'./images')

places_for_pretzels =[
    [0, -150], [500, -150], [1000, -150], [1500, -150], [2000,-150], [2500, -150], [3000,-150],
    [-250, 100], [250, 100], [750, 100], [1250, 100], [1750,100], [2250, 100], [2750,100],
    [0, 350], [500, 350], [1000, 350], [1500, 350], [2000,350], [2500, 350], [3000,350],
    [-250, 600], [250, 600], [750, 600], [1250, 600], [1750,600], [2250, 600], [2750,600],
    [0, 850], [500, 850], [1000, 850], [1500, 850], [2000,850], [2500, 850], [3000,850]
]

for banner in all_banners:

    pretzel_compositions = []
    size = 350, 350
    banner_background = Image.open(f'banner.png')
    banner_composition = banner_background.copy()

    k = 0

    for pretzel in banner:

        
        p1 = Image.open(f'./pretzel_parts/{pretzel_files[pretzel["Pretzel"]]}.png')
        p2 = Image.open(f'./pretzel_parts/{salt_files[pretzel["Salt"]]}.png')
        p3 = Image.open(f'./pretzel_parts/{chocolate_coat_files[pretzel["Chocolate_Coat"]]}.png')
        p4 = Image.open(f'./pretzel_parts/{topping_files[pretzel["Topping"]]}.png')


        #Create each composite
        com1 = Image.alpha_composite(p1, p2)
        com2 = Image.alpha_composite(com1, p3)
        com3 = Image.alpha_composite(com2, p4)
        
        com3 = com3.rotate(40)
        com3 = com3.resize(size)

        com3.save("./images/" + str(k) + "test.png")

        



        places_for_pretzels[k]
    
        #compose banner
        banner_composition.alpha_composite(com3, (places_for_pretzels[k][0],places_for_pretzels[k][1]))
        k += 1




    #Convert to RGB
    file_name = str(banner[0]["tokenId"]) + ".png"
    banner_composition.save("./images/" + file_name)