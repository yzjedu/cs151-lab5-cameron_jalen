balance = 1000

choice = 'g'
SENTINEL = 'e'

while choice != SENTINEL:
    choice = input("would you like to do: withdraw (w), deposit (d), view balance (v), or exit (e)").lower()
    if choice == "w":
        withdraw == int(input("how much would you like to withdraw: "))
        if amount < 0:
            print("you can't deposit a negative amount")
        balance -= withdraw
        if balance < 0:
            print("you will be charged 5% interest")
        print("\nyour current balance is", balance, "\n")
    if choice == "d":
        deposit == int(input("how much would you like to deposit: "))
        if deposit < 0:
            print("you can't withdraw a negative amount")
        balance += deposit
        print("\nyour current balance is", balance, "\n")
    if choice == "v":
        print("your balance is", balance, "\n")
if choice == SENTINEL:
    print("Thank you for using this ATM, \nhave a good day")