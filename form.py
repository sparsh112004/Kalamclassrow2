print("Login page :")
user_name=input("Enter your username : ")
password=input("Enter your password : ")
if(user_name==xyz and password==12345):
    print("FEEDBACK FORM")
    print("\nPersonal details\n")
    name=input("First Name:")
    last_name=input("Last Name:")
    email=input("Email:")
    contact=input("Contact:")
    semester=input("Semester:")
    course_name=input("Course name:")
    course_code=input("Course code:")
    course_lead=input("Course lead name:")
    i=input("Would you like to have any another course with same course lead:\nEnter '1' if yes\nEnter '2' if no\n")
    punctuality_level = response.lower()
    print("Punctuality level of the instructor:", punctuality_level)
    com=int(input("communication skills of the couse lead: \nEnter '5' if too fast\nEnter '4' if slightly fast\nEnter '3' if about right\nEnter '2' if lightly slow\nEnter '1' if too slow\n Your choice : "))
    pace=int(input("The pace at which material was covered was:\nEnter '5' if too fast\nEnter '4' if slightly fast\nEnter '3' if about right\nEnter '2' if lightly slow\nEnter '1' if too slow\n Your choice : "))
    material=int(input("The course materials helped me understand the subject matter:\nEnter '5' if you strongly agree\nEnter '4' if you agree\nEnter '3' if neutral\nEnter '2' if disagree\nEnter '1' if strongly disagree\n Your choice : "))
    skills=int(input("In this course, I learned skills or content that I consider valuable:\nEnter '5' if strongly agree\nEnter '4' if agree\nEnter '3' if neutral\nEnter '2' if disagree\nEnter '1' if strongly disagree\n Your choice : "))
    knowledge=int(input("What would you say about the knowledge of the course lead:\nEnter '5' if excellent\nEnter '4' if good\nEnter '3' if average\nEnter '2' if bad\nEnter '1' if very bad\n Your choice : "))
    overall=com+pace+material+skills+knowledge  
    g=input("We would like to hear if you have any comments/suggestions about the course and class.")
    overall_score = (overall/20)*10
    if (0<=overall_score<2):
        print("Your overall satisfaction score is : ",overall_score)
        print("We are sorry for your extremely bad experience ",name," we will consider your feedback in ",course_name," course and try making possible improvements.\nTHANKYOU")
    if (2<=overall_score<4): 
        print("Your overall satisfaction score is : ",overall_score)
        print("We are sorry for your bad experience ",name," we will consider your feedback in ",course_name," course and try making possible improvements.\nTHANKYOU")
    if (4<=overall_score<6):
        print("Your overall satisfaction score is : ",overall_score)
        print(fn,", your experience was average we will consider your feedbackk in ",course_name," course and try making it better.\nTHANKYOU")
    if (6<=overall_score<8):
        print("Your overall satisfaction score is : ",overall_score)
        print("So your overall experience was good ",name,", we thank you for your positive feedback in ",couse_name," course. We will try making it even better.\nTHANKYOU")
    if (8<=overall_score<10):
        print("Your overall satisfaction score is : ",overall_score)
        print("So your overall experience was excellent ",name,", we thank you for your extremely positive feedback in ",course_name," course. We will keep introducing more such cources.\nTHANKYOU")
else :xyz
  print("Wrong username or password")