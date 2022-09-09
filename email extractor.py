import re, os

# Array to store emails
emails = []

# Array to store second type string
emailsArr = []

# Take filename from user input and find it
filename = input("Enter file name: ")

if os.name == 'nt':
    path = 'C:\\'
elif os.name == 'posix':
    path = '/'
    
for root, dirs, files in os.walk(path):
    if filename in files:
        filename = os.path.join(root, filename)
        break
        
print('File found: ' + filename)

# Read the file and store it in a variable
with open(filename, encoding = 'unicode_escape') as file:
    fileContent = file.read()

# Basic email regex -> john@doe.com
emailRegex = re.compile(r'[\w\._%\-]+@[\w\-]+\.[a-zA-Z]{2,4}')
emails += emailRegex.findall(fileContent)
print('-------------------Basic emails fetched-------------------')
print(str(len(emails)) + ' fetched till now')

# Email regex type 2 ->
# {john, samantha.philip, henry}@caltech.com
# {robert.schoene | thomas.ilsche | mario.bielert | andreas.gocht | daniel.hackenberg}@tu-dresden.de
#emailRegex2 = re.compile(r'({([\w\._%\-]+(,\s)?)+}@[\w\-]+\.[a-zA-Z]{2,4})')
emailRegex2 = re.compile(r'({[^\}]+}@[\w\-]+\.[a-zA-Z]{2,4})')
for patt in emailRegex2.findall(fileContent):
    emailsArr.append(patt)

for string in emailsArr:
    domain = string[string.index('@'):]
    usernameRegex = re.compile(r'[\w\._%\-]+')
    usernames = usernameRegex.findall(string)[:-1]
    for username in usernames:
        email = username + domain
        emails.append(email)
print('-------------------Type 2 emails fetched-------------------')
print(str(len(emails)) + ' fetched till now')

# Write all emails to a file (allEmails.txt)
with open(filename+'Emails.txt', 'w') as f:
    for email in emails:
        f.write("%s\n" % email)
