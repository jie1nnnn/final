class books():
    def __init__(self):
        self.name = "xiaohan"
        self.title = "x"
        self.price = 0
        self.book = {}

    def Add(self):
        self.title = input("Enter the name of the book you add.")
        self.author = input("Enter the author of the book you add.")
        self.price = float(input("Enter the listing price of the book you add."))

       
        print("You have added", self.title)
        print(self.books)
 
def Muins(self):
    self.title = input("Enter the name of the book you remove   \n")
    try:
        str(self.title)
        if self.title in self.Book:
          del self.Books[self.title]
          print(self.Books) 

    except:
        print("Plases enter a book title")


def showbook(self):
    for x in self.Books:
        print(x)
        print(self.Books[x]['Author'])  
        print(self.Books[x]["price"])  

def save(self):
    filename = input("what do you want the file to be called?")
    with open(filename, "a") as file:
       file.write(str(self.Books))
       print(f" (self.title) saved to (filename)")

def load(self):
    filename = input("which file do you want to open?")
    with open(filename, "f") as file:
        print("title: ",self.title)
        print("author: ", self.Books[self.title]["author"] )
        print("price: ", self.Books[self.title]["price"])






 
