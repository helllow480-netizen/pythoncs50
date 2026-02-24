email = input (" what is your email? ").strip()

username, domain = email.split("@")
domain, extension = domain.split(".")
if username and domain and extension:
    print("valid email")  
else:   print("invalid email")