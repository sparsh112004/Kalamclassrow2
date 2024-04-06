
c=input("Course lead name:")
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

c=input("Contact No:")
s=input("Semester:")
cn=input("Course Name")

i=input("Would you like to have any another course with same course lead")
h=input("Overall rating of the course")
g=input("We would like to hear if you have any comments/suggestions about the course and class.")
response = input("Does the instructor come punctually on time? (always/mostly/rarely/never): ")
punctuality_level = response.lower()
print("Punctuality level of the instructor:", punctuality_level)
DT = input ("Enter the course :")
POE = input ("Enter the course :")
FOP = input ("Enter the course :")
ITC = input ("Enter the course :")
if(DT=="design thinking"):
    elif(POE=="principal of engireeing"):
        elif(FOP=="fandamentel of programing"):
            elif(ITC=="introduction to computing"):
                else:
pace=int(input("The pace at which material was covered was:\nEnter '5' if too fast\nEnter '4' if slightly fast\nEnter '3' if about right\nEnter '2' if lightly slow\nEnter '1' if too slow\n Your choice : "))
material=int(input("The course materials helped me understand the subject matter:\nEnter '5' if you strongly agree\nEnter '4' if you agree\nEnter '3' if neutral\nEnter '2' if disagree\nEnter '1' if strongly disagree\n Your choice : "))
skills=int(input("In this course, I learned skills or content that I consider valuable:\nEnter '5' if strongly agree\nEnter '4' if agree\nEnter '3' if neutral\nEnter '2' if disagree\nEnter '1' if strongly disagree\n Your choice : "))
knowledge=int(input("What would you say about the knowledge of the course lead:\nEnter '5' if excellent\nEnter '4' if good\nEnter '3' if average\nEnter '2' if bad\nEnter '1' if very bad\n Your choice : "))
overall=pace+material+skills+knowledge  


course_lead_feedback = input("In addition to the subject knowledge, did you gain anything useful from the Course lead? (yes/no): ")

# Check if the input is either 'yes' or 'no'
if course_lead_feedback.lower() == 'yes' or course_lead_feedback.lower() == 'no':
    print("Thank you for your feedback!")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")

# You can now use the variable 'course_lead_feedback' to store the user's response

