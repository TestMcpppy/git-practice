italian_food = ["Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagna"]
indian_food = ["Curry", "Chutney", "Samosa", "Naan"]


def find_meal(name, menu):
    if name in menu:
        return name
    else:
        return None


def select_meal(name, food_type):
    if food_type == "Italian":
        return find_meal(name, italian_food)
    elif food_type == "Indian":
        return find_meal(name, indian_food)
    else:
        return None


def display_available_meals(food_type):
    if food_type == "Italian":
        print("Available Italian Meals:")
        for food in italian_food:
            print(food)
    elif food_type == "Indian":
        print("Available Indian Meals:")
        for food in indian_food:
            print(food)
    else:
        print("Invalid food type")


def create_summary(name, amount, food_type):
    order = select_meal(name, food_type)
    if order == None:
        return "Meal not found"
    else:
        return f"{order} : {amount}"


print("Welcome to the Food Order System!")
type_input = input("Which kinds of food do you want to order?: ")
display_available_meals(type_input)

name_input = input("Meal Choice: ")
amount_input = input("Quantity: ")
result = create_summary(name_input, amount_input, type_input)
print(result)
