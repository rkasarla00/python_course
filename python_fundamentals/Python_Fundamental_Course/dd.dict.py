addresses = {
    "John": {"address": "123 Main St", "city": "Anytown", "state": "CA"},
    "Jane": {"address": "456 Oak Ave", "city": "Otherville", "state": "NY"},
    "Bob": {"address": "789 Maple St", "city": "Smallville", "state": "TX"},
    "Mary": {"address": "101 Elm St", "city": "Bigcity", "state": "IL"}
}

# access John's address
john_address = addresses["John"]["address"]
print(john_address)

# create a dictionary of books
books = {
    "Harry Potter": {"author": "J.K. Rowling", "year": 1997},
    "To Kill a Mockingbird": {"author": "Harper Lee", "year": 1960},
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "year": 1925}
}

# access the author of Harry Potter
hp_author = books["Harry Potter"]["author"]
print(hp_author)
