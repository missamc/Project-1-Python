my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.
#which should accept a dictionary as an argument when called,
#and return a string of the info in that book-dictionary in a user-friendly readable format.
# Code below

# def my_dictionary(my_book):

#     print(my_book)

# def my_dictionary(**kwargs):
#     print(kwargs)
#     if 'title' in kwargs:
#         print('My fruit of choice is {}'.format(kwargs['title']))
#         else:
#             print('Theres no book here')



def my_dictionary(my_book):

   

    book_string = f" {my_book['title']}, written by {my_book['author']}, was published in {my_book['year']}, is {my_book['pages']} pages, and recieved a rating of {my_book['rating']}"
    return book_string

print(my_dictionary(my_book))





# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def my_dictionary(my_book):
    
    for key in my_book.items():
        return my_book['title']

print(my_dictionary(my_book))

def my_dictionary(my_book):
    for key in my_book.items():
        return my_book['author']

print(my_dictionary(my_book))

def my_dictionary(my_book):
    for key in my_book.items():
        return my_book['year']

print(my_dictionary(my_book))

def my_dictionary(my_book):
    for key in my_book.items():
        return my_book['rating']

print(my_dictionary(my_book))

def my_dictionary(my_book):
    for key in my_book.items():
        return my_book['pages']

print(my_dictionary(my_book))


# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

new_book = {
    "title": "Holes",
    "author": "alouis Sachar",
    "year": 1998,
    "rating": 4.5,
    "pages": 233
}

old_book = {
    "title": "The Lord of the Rings",
    "author": "J.R.R.Tolkien",
    "year": 1954,
    "rating": 4.7,
    "pages": 500
}


mylist = [old_book, new_book, my_book]

def page_count(books):
    counter = 0
    for book in books:
        pages = book['pages']
        counter = counter + pages
    return counter

print (page_count(mylist))

# build a set of all of the authors in your library

def author_set(books):
    authors = set()
    for book in books:
        author = book['author']
        authors.add(author)
    return authors
print(author_set(mylist))


from statistics import mean
def average(books):
    ratings = []
    for book in books:
        rating = book['rating']
        ratings.append(rating)
    return mean (ratings)
print (average(mylist))




# index_count = 0

# def new_dictionary(list):
#     for item in list:
#         print(list[index_count])
#         index_count += 1

# print (new_dictionary(mylist))




# def combine_dictionary(a=0,b=0,c=0):
#     for item in zip(a,b,c):
#         print(combine_dictionary(my_book, old_book, new_book))