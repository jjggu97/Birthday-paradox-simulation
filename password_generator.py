import random
import string

def random_password():
    # set random password length
    password_length = random.randint(10, 20)
    
    # generate random password
    characters = string.digits + string.ascii_letters + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    return password

# print generated password
password = random_password()
print("password : ", password)

# 3 attempts to enter correct password
for attempt in range(3):
    entered_password = input("Enter the password: ")

    # check entered password is correct
    if entered_password == password:
        print("Access Confirmed")
        break
    else:
        print("Incorrect password. Attempts left:", 2 - attempt)
# 3 fails -> loop ends
else:
    print("Access Denied")
    