import csv
book0 = "Book,Author,Year Released\n"  # start with blank intentional
book1 = "To Kill A Mockingbird,Harper Lee,1960\n"
book2 = "A Brief History of Time,Stephen Hawking,1988\n"
book3 = "The Great Gatsby,F. Scott Fitzgerald,1922\n"
book4 = "The Man Who Mistook His Wife for a Hat,Oliver Sacks,1985\n"
book5 = "Pride and Prejudice,Jane Austen,1813\n"

file = open("Books.csv", "w")
inputList = [book0, book1, book2, book3, book4, book5]
file.write(str(book0))
file.write(str(book1))
file.write(str(book2))
file.write(str(book3))
file.write(str(book4))
file.write(str(book5))

file.close()