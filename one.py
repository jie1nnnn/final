class books():
    def __init__(self):
        self.name = "xiaohan"
        self.title = "x"
        self.price = 0
        self.book = {}

    def Add(self):
        self.title = input("Enter the name of the book you add.")
        self.author = input("Enter the author of the book you add.")
        self.price = str(input("Enter the price of the book you add."))

        print("You have added", self.title)
   
 
    def Muins(self):
        self.title = input("Enter the name of the book you remove   \n")
        try:
            str(self.title)
            if self.title in self.book:
             del self.book[self.title]
            print(self.book) 

        except:
            print("Plases enter a book title")


    def showbook(self):
        for x in self.book:
         print(x)
         print(self.book[x]['Author'])  
         print(self.book[x]["price"])

    def save(self):
        filename = input("what do you want the file to be called?")
        with open(filename, "a") as file:
         for x in file:
           print("title", self.title)
           print("author:", self.book[self.title]["author"])
           print("price:", self.book[self.title]["price"])



    def load(self):
        filename = input("which file do you want to open?")
        with open(filename, "f") as file:
             print("title: ",self.title)
             print("author: ", self.Book[self.title]["author"] )
             print("price: ", self.Book[self.title]["price"])






 
