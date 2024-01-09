import random
import string

def random_password():
    #set_random_password_length
    password_length = random.randint(10, 20)
    
    #generate_password
    characters = string.digits + string.ascii_letters + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    return password

#print_generated_password
password = random_password()
print("password : ", password)
