fn=input("First Name:")
ln=input("Last Name:")
ip=input("Issue and Problems :")
pbl=input("Project based problem:")
e=input("Email:")

c=input("contact:")
s=input("semester:")
cn=input("course name")
cc=input("course code:")
cln=input("Course lead name:")

i=input("Would you like to have any another course with same course lead")
h=input("Overall rating of the course")
g=input("We would like to hear if you have any comments/suggestions about the course and class.")
response = input("Does the instructor come punctually on time? (always/mostly/rarely/never): ")
punctuality_level = response.lower()
pace=int(input("The pace at which material was covered was:\n '5' if too fast\n '4' if slightly fast\n '3' if about right\n '2' if lightly slow\n '1' if too slow\n Your choice : "))
material=int(input("The course materials helped me understand the subject matter:\n '5' if you strongly agree\n '4' if you agree\n '3' if neutral\n '2' if disagree\n '1' if strongly disagree\n Your choice : "))
skills=int(input("In this course, I learned skills or content that I consider valuable:\n '5' if strongly agree\n '4' if agree\n '3' if neutral\n '2' if disagree\n '1' if strongly disagree\n Your choice : "))
knowledge=int(input("What would you say about the knowledge of the course lead:\n '5' if excellent\n '4' if good\n '3' if average\n '2' if bad\n '1' if very bad\n Your choice : "))
overall=pace+material+skills+knowledge               
overall=9
overall_score = (overall/20)*10
if (0<=overall_score<2):
    print("Your overall satisfaction score is : ",overall_score)
    print("We are sorry for your extremely bad experience ",fn," we will consider your feedback in ",cn," course and try making possible improvements.\nTHANKYOU")
if (2<=overall_score<4):
    print("Your overall satisfaction score is : ",overall_score)
    print("We are sorry for your bad experience ",fn," we will consider your feedback in ",cn," course and try making possible improvements.\nTHANKYOU")
if (4<=overall_score<6):
    print("Your overall satisfaction score is : ",overall_score)
    print(fn,", your experience was average we will consider your feedbackk in ",cn," course and try making it better.\nTHANKYOU")
if (6<=overall_score<8):
    print("Your overall satisfaction score is : ",overall_score)
    print("So your overall experience was good ",fn,", we thank you for your positive feedback in ",cn," course. We will try making it even better.\nTHANKYOU")
if (8<=overall_score<10):
    print("Your overall satisfaction score is : ",overall_score)
    print("So your overall experience was excellent ",fn,", we thank you for your extremely positive feedback in ",cn," course. We will keep introducing more such cources.\nTHANKYOU")
  
