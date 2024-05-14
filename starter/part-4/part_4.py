### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here


# def create_new_book():
    

#     author = input('Who is the author of the book? ')

#     title = input('What is the title of the book? ')

#     year = input('When was the book published? ')

#     rating = input('What rating did this book recieve? ')

#     pages = input('How many pages does this book have? ')

#     new_dict = {
#         'title': title,
#         'author': author,
#         'year': year,
#         'rating': rating,
#         'pages': pages
#     }
#     return new_dict
# print(create_new_book())

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# def converting_data_types ():
#     years = int(input('When was the book published? '))
#     pages = int(input('How many pages does this book have? '))
#     ratings = float(input('What rating did this book recieve? '))
# print(converting_data_types())







### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here


def create_new_book():
    

    author = input('Who is the author of the book? ')

    title = input('What is the title of the book? ')
    try:
        year = int(input('When was the book published? '))
    except:
        year = int(input('give me a number'))

    try:
        rating = float(input('What rating did this book recieve? '))
    except:
        rating  = float(input('give me a number'))
    try:
        pages = int(input('How many pages does this book have? '))
    except:
        pages = int(input('give me a number'))

    new_dict = {
        'title': title,
        'author': author,
        'year': year,
        'rating': rating,
        'pages': pages
    }
    return new_dict
# print(create_new_book())



### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

current_books = [
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "year": 1997,
        "rating": 4.5,
        "pages": 309
    },
    {
        "title": "Twilight",
        "author": "Stephenie Meyer",
        "year": 2005,
        "rating": 3.6,
        "pages": 498
    },
    {
        "title": "The Fault in Our Stars",
        "author": "John Green",
        "year": 2012,
        "rating": 4.2,
        "pages": 313
    },
    {
        "title": "Divergent",
        "author": "Veronica Roth",
        "year": 2011,
        "rating": 4.2,
        "pages": 487
    }
]

def main_menu():


    while True:
        choice = input('a for adding a book, b for seeing a book, c to exit the books')

        if choice == 'a':
            new_book = create_new_book()
            print(new_book)
            current_books.append(new_book)

        elif choice == 'b':
            for book in current_books:
                print(book)
        

        if choice == 'c':
            print('goodbye')
            break
       

main_menu()

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here


