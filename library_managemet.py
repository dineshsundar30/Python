                                     #library managemet
class Library():

  def __init__(self,list):
      self.all_book_list = list
      self.available_books_list = list[:]
      self.books_lended_list = {}
  def available_book_list(self):
           for book in self.available_books_list:                                    # or print(self.available_books_list)
               print(book)
  def all_books_list(self):
          for book in self.all_book_list:
             print(book)
  def lend_books(self,name,book):
           if book not in self.all_book_list:
              print("your entered incorrect book name")
           elif book in self.available_books_list:
               print("you can len the book")
               self.available_books_list.remove(book)
               self.books_lended_list.update({book:name})        #also we can use like self.books_lended_list[book] = name  # ✔️ Recommended
           else:
               if book not in self.available_books_list:
                   print("the book is already taken by "+ self.books_lended_list[book])

  def return_book(self,book):
      del self.books_lended_list[book]
      self.available_books_list.append(book)

if __name__=="__main__":
      lib = Library(["book1","book2","book3","book4","book5"])
      print("welcome to library")
      while True:
          print("enter 1. see the available book list")
          print("enter 2 to see all book list")
          print("enter 3 for lend books")
          print("enter 4 return the book")
          print("enter 5 to quit")
          usrchoice = input("enetr your choice: ")

          if usrchoice=='1':
               lib.available_book_list()
          elif usrchoice=="2":
              lib.all_books_list()
          elif usrchoice=="3":
              name=input("enter your name: ")
              book=input("enetr your book: ")
              lib.lend_books(name,book)
          elif usrchoice == "4":
              book = input("enter the returning book name: ")
              lib.return_book(book)
          elif usrchoice=="5":
              break
          else:
              print("entered a incorrect number")
