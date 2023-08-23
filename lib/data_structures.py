spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    got_foods = []

    for food in spicy_foods:
        got_foods.append(food["name"])
    
    return got_foods


def get_spiciest_foods(spicy_foods):
   return [food for food in spicy_foods if (food["heat_level"] > 5)] 

def print_spicy_foods(spicy_foods):
    return [print(f'{f["name"]} ({f["cuisine"]}) | Heat Level: {"🌶" * f["heat_level"]}') for f in spicy_foods]
    
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    foods = get_spiciest_foods(spicy_foods)
    return print_spicy_foods(foods)
    
def get_average_heat_level(spicy_foods):
    total_heat = 0
    num_food = len(spicy_foods)

    if num_food == 0:
        return 0
    
    for food in spicy_foods:
        total_heat += food["heat_level"]

    avg_heat_level = total_heat / num_food
    return int(avg_heat_level)  



def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
