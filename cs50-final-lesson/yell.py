def main():
  yell("hello", "world", "this", "is", "a", "sentence")
def yell(*words):
         uppercased = map(str.upper, words)
         print(*uppercased)  
if __name__ == "__main__":
  main()