favorite_restaurants = ["Popeyes", "In-N-Out", "Wonder Burgers", "McDonalds"]
print("favorite_restaurants")
new_restaurant = input("What other restaurant do you like?")
favorite_restaurants.append(new_restaurant)
#Question = int(input("Rank your restaurant list by number from least to most favorite."))
#Answer = int(input())
str = "Do you like ", new_restaurant, " more than ", favorite_restaurants[0], " Y/N"
rank = input(str)

print("Here is your restaurnt rankings", )
