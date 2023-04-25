# foods = list()
# while True:
#   food = input("What food do you like?: ")
#      if food == "quit":
#           break
#   food.append(food)

foods = list()      #walrus :=
while food := input("What food do you like?: ") != "quit":
    foods.append(food)
