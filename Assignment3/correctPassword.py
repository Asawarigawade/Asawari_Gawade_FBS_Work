
correct_userid = "admin"
correct_password = "1234"

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == correct_userid and password == correct_password:
    print("Login successful!")
else:
    print("Invalid User ID or Password.")