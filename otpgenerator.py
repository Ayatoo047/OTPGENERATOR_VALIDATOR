import random

email = input("input your email: ")
confirmation_test = False

while confirmation_test is False:
    otp = []
    for numbers in range(6):
        otp.append(random.randint(0, 9))
    join = "".join([str(i) for i in otp])
    print(join)
    confirmation = input("input otp: ")
    if confirmation != join:
        print("wrong otp")
    elif confirmation == join:
        confirmation_test = True
        print("welcome", email)