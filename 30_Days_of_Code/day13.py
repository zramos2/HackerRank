from abc import ABCMeta, abstractmethod

# Referece: https://stackoverflow.com/questions/7375595/class-with-object-as-a-parameter
# 'object' as a parameter, bascially 'classic class' and turns it into 'new-style' class
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(): pass     # when 'pass' is executed, nothing happens
                            #Referece: https://docs.python.org/2.0/ref/pass.html

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price

    def display(self):
       print('Title: ' + title)
       print('Author: ' + author)
       print('Price: ' + str(price))


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
