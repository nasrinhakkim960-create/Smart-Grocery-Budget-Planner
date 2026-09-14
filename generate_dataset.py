import random
import pandas as pd
months=[
    "January","february","March","April","June","July","August","September","October","November","December"
]
food_preferences=[
    "Vegetarian","Mixed","Non-Veg"
]
shopping_frequency=[
    "weekly","Biweekly","Monthly"
]
records=[]
for i in range(500):
    income= random.randint(15000,150000)
    family_size=random.randint(1,8)
    children=random.randint(0,min(4,family_size-1))
    previous_expense=random.randint(2500,18000)
    month=random.choice(months)
    festival=random.choice(["yes","no"])
    food=random.choice(food_preferences)
    guest= random.choice(["Yes","No"])
    price_hike=random.choice(["Yes","No"])
    shopping=random.choice(shopping_frequency)
    expense=previous_expense
    expense+=(family_size-1)*500
    expense+=children*300
    if festival == "Yes":
        expense += random.randint(1000,2500)
    if guest == "Yes":
        expense += random.randint(500,2000)
    if price_hike == "Yes":
        expense = int(expense * random.uniform(1.05,1.15))
    if income > 100000:
        expense += 500

    elif income < 30000:
        expense -= 300
    expense = max(expense,2500)
    records.append([
    income,
    family_size,
    children,
    previous_expense,
    month,
    festival,
    food,
    guest,
    price_hike,
    shopping,
    expense
    ])
df = pd.DataFrame(
    records,
    columns=[
        "Monthly_Income",
        "Family_Size",
        "Children",
        "Previous_Expense",
        "Month",
        "Festival",
        "Food_Preference",
        "Guest_Arrival",
        "Price_Hike",
        "Shopping_Frequency",
        "Grocery_Expense"
    ]
)
df.to_csv("data/data.csv", index=False)
print("dataset generated successfully")
print("number of records:",len(df))