
if __name__ == '__main__':
    print("Enter a number")
    number = int(input())
    factorial = 1

    if(number<0):
        print("Error!: Factorial of a negative number is not defined")
    elif(number==0):
        print("Factorial is 1")
    else:
        for i in range(1,number+1):  #1 is inclusive and n+1 so it'll take the number
            factorial=factorial* i
        print("The factorial of", number, "is", factorial)