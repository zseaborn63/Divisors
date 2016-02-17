print("Welcome to Number Construction Extractor!")
user_num = int(input("What is your number?\n"))

divisors = []
for x in range(1, user_num):
    if user_num % x == 0:
        divisors.append(x)

print(divisors)
