a=input("Frist Name:")
b=input("Last Name:")
c=input("Course lead name:")

























print("Feedback Questions")
pace=int(input("The pace at which material was covered was:\nEnter '5' if too fast\nEnter '4' if slightly fast\nEnter '3' if about right\nEnter '2' if lightly slow\nEnter '1' if too slow\n Your choice : "))
material=int(input("The course materials helped me understand the subject matter:\nEnter '5' if you strongly agree\nEnter '4' if you agree\nEnter '3' if neutral\nEnter '2' if disagree\nEnter '1' if strongly disagree\n Your choice : "))
skills=int(input("In this course, I learned skills or content that I consider valuable:\nEnter '5' if strongly agree\nEnter '4' if agree\nEnter '3' if neutral\nEnter '2' if disagree\nEnter '1' if strongly disagree\n Your choice : "))
knowledge=int(input("What would you say about the knowledge of the course lead:\nEnter '5' if excellent\nEnter '4' if good\nEnter '3' if average\nEnter '2' if bad\nEnter '1' if very bad\n Your choice : "))
overall=pace+material+skills+knowledge
