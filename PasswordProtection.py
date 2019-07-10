#program checks if the password is correct



with open("password.txt") as f:
        password_from_file = f.readline()
print("Enter your password:")
password = input()

while password != password_from_file:
    print("Enter your password:")
    password = input()

print("Correct password, you may enter")
