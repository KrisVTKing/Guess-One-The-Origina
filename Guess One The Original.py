def get_guess():
    guess = input("Pick a number between 0 and 20: ")
    return guess
if get_guess() == "6":
    print("True")
else:
    print("False")
print(get_guess())

