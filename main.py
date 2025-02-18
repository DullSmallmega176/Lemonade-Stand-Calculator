import re
print("Reminder\n100 cups\n50 lemons - 8 per jar\n56 sugar - 8 per jar\n1000 ice - 10 per cup\n")
def price():
    x = int(re.sub("[^0-9]", "", input("What is the temperature 'F': "))) - (5 if input("Is it an overcast? (yes/no): ").lower()[0] in ["y", "t", "1"] else 0)
    return 40 if x>=90 else 35 if x>=80 else 30 if x>=70 else 25 if x>=60 else 20
print(price())
