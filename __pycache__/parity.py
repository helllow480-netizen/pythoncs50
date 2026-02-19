def main():
    x = int(input("whats x? "))
    if is_even(x):
        print("true")
    else:
        print("false")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()