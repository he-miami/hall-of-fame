class Func:
    def __init__(self, name, author, delegate):
        self.name = name
        self.author = author
        self.delegate = delegate


def example():
    print("You are definitely awesome Today ...!")
    print("Keep it up!")


def fromGabi():
    print("It was a pleasure working with You!")
    print("Fly high and good luck!")


func = Func("example-func", "...", example)
gabiFunc = Func("from-gabi", "Gabriela Chacuś", fromGabi)

functions = [
    gabiFunc
]

while True:
    print("Good morning ...")
    print("List of available functions:")
    for index, function in enumerate(functions):
        print(f'{index + 1}. Function: >{function.name}<, by: {function.author}')

    selection = input("What function would you like to run:")
    functions[int(selection) - 1].delegate()

