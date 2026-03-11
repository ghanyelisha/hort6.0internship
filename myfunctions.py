def Hannah_prime_2():


    num3 = int(input("Enter a number: "))

    mylist = []
    for i in range(1, num3+1):
        mylist.append(num3%i)

    print(mylist)

    if mylist.count(0) == 2:
        print(f"{num3} is a prime number.")
    else:
        print(f"{num3} is not a prime number.")