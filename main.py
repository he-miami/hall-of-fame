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

def fromOla():
    print("Goodbye and good luck! It was great to work with you!")


func = Func("example-func", "...", example)
gabiFunc = Func("from-gabi", "Gabriela Chacuś", fromGabi)
olaFunc = Func("from-ola", "Aleksandra Dura", fromOla)

functions = [
    Func("hej", "jakub", lambda: print("wszystkiego dobrego i do zobaczenia")),
    gabiFunc,
    olaFunc
]

while True:
    print("Good morning ...")
    print("List of available functions:")
    for index, function in enumerate(functions):
        print(f'{index + 1}. Function: >{function.name}<, by: {function.author}')

    selection = None
    while selection is None:
        tmp = input("What function would you like to run:")
        if not tmp.isnumeric():
            continue
        tmp = int(tmp) - 1
        if tmp < 0 or tmp >= len(functions):
            continue
        selection = tmp
    print()
    functions[selection].delegate()
    print()
