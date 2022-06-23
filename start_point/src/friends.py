def get_name(person):
    return person["name"]

def get_favourite_tv_show(show):
    return show["favourites"]["tv_show"]

def likes_to_eat(person,food):
    like_food = False
    for snack in person["favourites"]["snacks"]:
        if snack == food:
            like_food = True
    return like_food
        

def add_friend(person, name):
    person["friends"].append(name)


def remove_friend(person, name):
    person["friends"].remove(name)

def total_money(list_of_people):
    sum = 0
    for person in list_of_people:
        sum+= person["monies"]
    return sum

def lend_money(person1, person2, money):
    person1["monies"] -= money
    person2["monies"] += money

def all_favourite_foods(list_of_people):
    fave_food = []
    for people in list_of_people:
        for food in people["favourites"]["snacks"]:
            fave_food.append(food)
    return fave_food

def find_no_friends(list_of_people):
    no_friends = []
    for people in list_of_people:
        if people["friends"] == []:
            no_friends.append(people)

    return no_friends
                
