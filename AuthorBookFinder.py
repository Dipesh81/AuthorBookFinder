import re

# Data: Person and their books
people_books = [
    {"name": "Rahul Nagar", "book": "Rahul Industrial Associate"},
    {"name": "Rahul Shah", "book": "Rahul Furniture"},
    {"name": "Rahul Trivedi", "book": "Rahul Co-operative"},
    {"name": "Rahul Parikh", "book": "Anita Marketing Basics"},
    {"name": "Anita Patel", "book": "Anita Finance Guide"}
]

# Input search
search_name = input("Enter person name to search: ").strip()

# Regex: match first name exactly at start of author's name AND check book contains first name
author_pattern = re.compile(rf"^{re.escape(search_name)}\b", re.IGNORECASE)
book_pattern = re.compile(rf"\b{re.escape(search_name)}\b", re.IGNORECASE)

# Collect books where author first name matches AND book title contains first name
found_books = [
    entry["book"]
    for entry in people_books
    if author_pattern.search(entry["name"]) and book_pattern.search(entry["book"])
]

# Display results
if found_books:
    print(f"\nBooks by {search_name}:")
    for b in found_books:
        print("-", b)
else:
    print("No books found for this person.")
