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

        self.book = {}
        self.book['title'] = "x"
        self.book['name'] = "xiaohan"
        self.book['price'] = "0"

        