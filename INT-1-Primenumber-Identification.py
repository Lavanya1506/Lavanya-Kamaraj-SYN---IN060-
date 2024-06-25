num = int(input("Enter your number : "))
count = 0
if num > 0:
    for i in range(1,num+1):
        if num%i == 0:
            count = count + 1
    if count == 2:
        print("the number is prime")
    else : 
        print("the number is not prime")