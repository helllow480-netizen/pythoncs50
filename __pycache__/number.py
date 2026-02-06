try:  
    x = int(input("whats c? "))
    print(f"x is {x}")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
except ValueError:
    print("x is not an integer")