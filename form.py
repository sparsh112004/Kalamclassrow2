fn=input("Frist Name:")
ln=input("Last Name:")
ip=input("issue and problems :")
pbl=input("project based problem:")
e=input("Email:")
c=input("contact:")
s=input("semester:")
cn=input("course name")
cc=input("course code:")
cln=input("Course lead name:")

# Ask the user about the instructor's punctuality
response = input("Does the instructor come punctually on time? (always/mostly/rarely/never): ")

# Save the user input to a variable
punctuality_level = response.lower()

# Print the user input
print("Punctuality level of the instructor:", punctuality_level)
