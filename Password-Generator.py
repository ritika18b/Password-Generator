
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_"
while True:
    print("Length of password: ")
    n=int(input())

    print("Password required: ")
    c=int(input())

    for i in range(0,c):
        password = ""
        for j in range(0,n):
            temp = random.choice(char)
            password = password+temp
        print("The generated password is:",password)    
    print("Do you want to generate more passwords?")
    repeat=input()
    
    if repeat =="no":
        break
print("  Thanku  ")
