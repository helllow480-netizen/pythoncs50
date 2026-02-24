import re

email = input (" what is your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("valid email")
else:
    print("invalid email")