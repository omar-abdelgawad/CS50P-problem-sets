s = input("Item: ").lower()
cal = {
    "apple":130,
    "avocado":50,
    "banana":110,
    "cantaloupe":50,
    "grapefruit":60,
    "grapes":90,
    "lemon":15,
    "orange":80,
    "peach":60,
    "plums":70,
    "strawberries":50,
    "watermelon":80,
    "kiwifruit":90,
    "pear":100,
    "sweet cherries":100,
}
if s in cal:
    print(f"Calories: {cal[s]}")