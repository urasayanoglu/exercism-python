#Defining two_fer function with arguement None
def two_fer(name = None):
    if name == None:
        return "One for you, one for me."
    else:
        return f"One for {name.title()}, one for me."

#Defining two_fer function in another way
def two_fer(name: str = "you") -> str:
    return f"One for {name}, one for me."
