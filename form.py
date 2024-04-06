name= input("Enter your Name: ")
E_id= input("Enter your Enrollment ID: ")
email= input("Enter your email ID: ")
contact=int(input("Enter your contact number:" ))
school=input("Enter your school in the University: ")
C_name=input("Enter the course name: ")
C_code=input("Enter the course code: ")
C_lead=input("Enter your course lead: ")
rate=int(input("Rate your couse lead from 1 to 10"))
if rate<=5:
    print("Poor")
else:
    print("Good")
rate_=int(input("Rate your couse lead according to his delivering content"))
if rate_<=5:
    print("poor")
else:
    print("Good")
add_=input("Add some instruction you want to add")
punch=int(input("Rate their punchuality in the class"))
if punch <=7:
    print("poor")
else:
    print("Good")
overall=((rate+rate_+punch)//3)*100
if overall >=50:
    print("Your feedback is positive to the course lead")
else:
    print("Oh! You are not satisfied with the course")
print("Thank you for the feedback")

