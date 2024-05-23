import random
import string
password = ("")
string.ascii_letters
PasswordLengthComparer = 0
PasswordLength = int(input("What is the desired length of your password? >"))
while PasswordLengthComparer < PasswordLength:
	LetterOrNumber = random.randrange(0,2)
	if LetterOrNumber == 0:
		password += str(random.randint(0,9))
	else:
		password += random.choice(string.ascii_letters)
	PasswordLengthComparer += 1
print(password)
