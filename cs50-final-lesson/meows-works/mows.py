def meow(n: int) -> str:
  return "Meow\n" * n
number = int(input("number: "))
meows: str = meow(number)
print(meows)