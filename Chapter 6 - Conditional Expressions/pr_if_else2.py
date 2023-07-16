# WAP to find out whether a student is pass or fail, if it requires total 40% & at least 33% in each subject to pass. Assume 3 subjects & take marks as an input from the user.
sub1=int(input("Enter the marks of first subject: "))
sub2=int(input("Enter the marks of second subject: "))
sub3=int(input("Enter the marks of third subject: "))
if (sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("You are fail because you have less than 33% marks in one of the subject.")
elif(sub1+sub2+sub3)/3 < 40:
    print("You are fail due to total percentage is less than 40%.")
else:
    print("Congratulations! You passed the exam.")