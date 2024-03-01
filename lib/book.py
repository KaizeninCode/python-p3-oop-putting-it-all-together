#!/usr/bin/env python3

# class Book:
#     def __init__(self, title, page_count):
#         if not isinstance(page_count, int):
#             print('page_count must be an integer')
#         else:
#             self.page_count = page_count    
#         self.title = title    

#     def turn_page(self):
#         print('Flipping the page...wow, you read fast!')
#     def __str__(self):
#         return f'Book({self.title},{self._page_count})'        


class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self.current_page = 0

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        self._page_count = value

    def turn_page(self):
        if self.current_page < self.page_count:
            self.current_page += 1
            print("Flipping the page...wow, you read fast!")
        else:
            print("You've reached the end of the book.")