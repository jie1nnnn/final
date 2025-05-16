from one import books
a = books()
v = ""
print(a.title)

while v !="no":

    v = input("would you like to add a book(yes or no)?")
    if v == "yes":
        c = a.Add()
    elif v == "no":
        c = a.Muins()
    elif v == "y":
        e = a.showbook()
    elif v == "show":
        b = a.save()
    else:
        print("please enter 'yes' or 'no'.")
