def isPrime(N):
    a = 2
    k = N // 2
    while k >=a :
        if N % 2 ==0:
            return False
        a   += 1
        k = N // a
    return True

def isPalindrom(n):
    return n ==n[::-1]


def isOdd(n):
    if n%2 == 0 :
        return False
    return True


def isArmstrong(num):
    sum=0
    temp = num
    while temp>0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        return True
    return  False

def check():
    number = int(input("enter the number"))
    if(isPrime(number)):
        print(number, "is a prime a number")
    if(isOdd(number)):
        print(number,"is an odd number")
    else:
        print(number,"is a even number")
    if(isArmstrong(number)):
        print(number,"is a armstrong number")

    n = "malyalam"
    ans = isPalindrom(n)
    if ans :
        print("yes")
    else:
        print("no")
check()
