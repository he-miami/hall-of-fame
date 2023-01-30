class Func:
    def __init__(self, name, author, delegate):
        self.name = name
        self.author = author
        self.delegate = delegate


def example():
    print("You are definitely awesome Today ...!")
    print("Keep it up!")


func = Func("example-func", "...", example)

functions = [
    func,
    Func("hej", "jakub", lambda: print("wszystkiego dobrego i do zobaczenia"))
]

while True:
    print("Good morning ...")
    print("List of available functions:")
    print(type(functions))
    for index, function in enumerate(functions):
        print(f'{index + 1}. Function: >{function.name}<, by: {function.author}')

    selection = input("What function would you like to run:")
    functions[int(selection) - 1].delegate()
