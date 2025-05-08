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

       
        print("You have added", self title)
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
    with open("append_file.txt", "a") as file:
       file.write(str self.Books)
       print(f" (self.title) saved to (name)")

def 

