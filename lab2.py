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
print("Your total average is {}" .format (avg))
if avg >= 75:
  print("PASSED")
else:
  print("FAILED")
