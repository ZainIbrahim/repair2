'''
import requests

helo = requests.get('http://www.hipstercode.com' , 'w')

outfile = open("/Users/zeinalabidin/desktop/ccc/text.txt")
outfile.write(str(helo.text.encode('utf-8')))

#print(helo.text.encode('utf-8'))
'''

'''

#Email validator
import re

f= open ('ValidEmails.txt', 'w')

def is_email():
    email=input("Enter your email")
    pattern = '[\.\w]{1,}[@]\w+[.]\w+'
    file = open('ValidEmails.txt','w')
    if re.match(pattern, email):
        file.write(email)

        file.close
        print("Valid Email")
    else:
        print("Invalid Email")

#The Menu
print("The Email validator progam \n")
print("What do you want to do\n")
print("Validate the Email")
print("Quit")

while True:
        answer=(input("Press V, or Q : "))
        if answer in("V" ,"v"):
            is_email()
        elif answer in("Q" ,"q"):
            break
        else:
            print("Invalid response")

'''

line1 = []
line1.append("xyz ")
line1.append("abc")
line1.append("mno")

#file = open("file.txt","r+")
for i in range(3):
    open("file.txt", "r+").write(line1[i])

    #file.write("\n")


'''
for line in file:
    print(line)
file.close()
'''