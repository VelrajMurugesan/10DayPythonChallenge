# Grade Calculator
score = int(input("Enter a exam mark : "))

if score > 60:
    print("Pass")
    if score <= 100 and score >= 90:
        print("And Your Grade is : A")
    elif score < 90 and score >= 80:
        print("And Your Grade is : B")
    elif score < 80 and score >= 70:
        print("And Your Grade is : C")
    elif score < 70 and score >= 60:
        print("And Your Grade is : D")
    else:
        print("Invalid mark")
else:
    print("Fail")

 # Expression
 #
fName = "Velraj"
lName = "Murugesan"
fullname_old = fName + " " + lName
print(fullname_old)
# any expression can be used inside {} like 2 + 2, len(fName) and so on...
fullName = f"{fName} {lName}"
print(fullName)
