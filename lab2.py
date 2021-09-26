print("-----------------------------------------------------------------------------")
print("EMERGING TECHNOLOGIES - LABORATORY ACTIVITY 2")
print("-----------------------------------------------------------------------------")
print("")
prelims = float(input("Input your prelim grades: "))
midterm = float(input("Input your midterm grades: "))
semi = float(input("Input your semi-final grades: "))
final = float(input("Input your final grades: "))
avg = (prelims + midterm + semi + final) / 4
print(" ")
if avg >= 99 and avg <= 100:
    print("Your total average is {}" .format(avg) + ". \nYour grade is A. \nCongratulations, you passed!")
elif avg >= 90 and avg <= 98:
    print("Your total average is {}" .format(avg) + ". \nYour grade is B. \nCongratulations, you passed!")
elif avg >= 80 and avg <= 89:
    print("Your total average is {}" .format(avg) + ". \nYour grade is C. \nCongratulations, you passed!")
elif avg >= 75 and avg <= 79:
    print("Your total average is {}" .format(avg) + ". \nYour grade is D. \nCongratulations, you passed!")
elif avg >= 70 and avg <= 74:
    print("Your total average is {}" .format(avg) + ". \nYour grade is D. \nUnfortunately, you failed.")
elif avg >= 61 and avg <= 69:
    print("Your total average is {}" .format(avg) + ". \nYour grade is E. \nUnfortunately, you failed.")
elif avg < 60:
    print("Your total average is {}" .format(avg) + ". \nYour grade is F. \nUnfortunately, you failed.")
else:
    print("You have entered an invalid input!")

