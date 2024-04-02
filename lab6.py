

class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        self.balance +=amount
        return f"your amount deposit is ${amount} and new balance is ${self.balance}"
 
    def withdrawal(self,amount):
         self.amount=amount
         self.balance -= amount
         return f"your amount withdrawal is ${amount} and new balance is ${self.balance}"

    def check_balance(self):
            
            return f"your current balance is ${self.balance}"


         
class savingAccount(BankAccount):
      def __init__(self, account_number, balance):
           BankAccount.__init__(self,account_number, balance)
      def interests(self,iterests):
           
           self.balance += iterests
           return f"your interests is ${iterests} and new balance is ${self.balance}"
Account1= savingAccount("34",1000)
#Account1.deposit(500)
numb1=int(input("Enter deposit amount:"))

print(Account1.deposit(numb1))  
print(Account1.check_balance())
numb2=int(input("Enter Withdrawal amount:"))

print(Account1.withdrawal(numb2))  
print(Account1.check_balance())
numb3=int(input("Enter interest amount:"))

print(Account1.interests(numb3))


# #                                              Task(2)
# class Book:
#     def __init__(self,title,author,available):
#          self.title=title
#          self.author=author
#          self.available=available
#     def check_out(self):
#          if self.available==True:
#            return f"Title book is {self.title} and its author is {self.author}"
#          else:
#             return f"Sorry, book is {self.title} and its author is {self.author} is currently not available."
#     def return_book(self):
#         if self.available==True:
#             return f"Thank you for returning the book '{self.title}' by {self.author}."
#         else:
#             return f"The book '{self.title}' by {self.author} is already available."

# book1 = Book("To Kill a Mockingbird", "Harper Lee")
# book2 = Book("1984", "George Orwell")
# book3=Book("Atomic Habits" , "James Clear")

# library = {
#     "To kill a Mockingbird": book1,
#     "1984": book2,
#     "Atomic Habits": book3,
# }

# while True:
#     print("Library Catalog:")
#     print("1. Checkout a book")
#     print("2. Return a book")
#     print("3. Exit")
#     choice = input("Enter your choice (1-3): ")
#     if choice=="1":
#         #print("\n Books available:")
#         book_title = input("Enter the title of the book you want to checkout: ")

#         for book_title in library.items():

#          #if self.available:

#             #print(f"- {book_title} by {self.author}")


#             print(library.get(book_title))
#         if selected_book:
#             print(selected_book.check_out())
#         else:
#             print("Book not found or unavailable.")

#     elif choice == "2":
#         book_title = input("Enter the title of the book you want to return: ")
#         selected_book = library.get(book_title)
#         if selected_book:
#             print(selected_book.return_book())
#         else:
#             print("Book not found or already available.")

#     elif choice == "3":
#         print("Exiting the library catalog. Thank you!")
#         break

#     else:
#         print("Invalid choice. Please enter a valid option.")






    
         
