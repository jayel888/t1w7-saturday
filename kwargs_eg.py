def personal_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} ---> {value}")

personal_details(name = "Jess", age = "31", address = "Melbourne")

def myFunction(*onestar, **twostars):
    print("args: ", onestar)
    print("kwargs: ", twostars)

myFunction('I', 'Love', 'Coding', first = "I", second = "love", third = "coding!")