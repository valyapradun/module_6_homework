"""
Implement a Pagination class helpful to arrange text on pages and list content on given page.
The class should take in a text and a positive integer which indicate how many symbols will be allowed
per each page (take spaces into account as well).
You need to be able to get the amount of whole symbols in text, get a number of pages that came out
and method that accepts the page number and return quantity of symbols on this page.
If the provided number of the page is missing print the warning message "Invalid index. Page is missing".
If you're familliar with using of Excpetions in Python display the error message in this way.
Pages indexing starts with 0.

Example:
>> pages = Pagination('Your beautiful text', 5)
>> pages.page_count
4
>> pages.item_count
19

>> pages.count_items_on_page(0)
5
>> pages.count_items_on_page(3)
4
>> pages.count_items_on_page(4)
Exception: Invalid index. Page is missing.

Optional: implement searching/filtering pages by symblos/words and displaying pages with all the symbols on it.
If you're querying by symbol that appears on many pages or if you are querying by the word that is splitted in two
return an array of all the occurences.

Example:
>> pages.find_page('Your')
[0]
>> pages.find_page('e')
[1, 3]
>> pages.find_page('beautiful')
[1, 2]
>> pages.find_page('great')
Exception: 'great' is missing on the pages
>> pages.display_page(0)
'Your '
"""


class PaginationError(Exception):
    pass


class Pagination(object):
    """ Class Pagination to help to arrange text on pages and list content on given page"""

    def __init__(self, text: str, symbols_on_page: int):
        self.text = text
        self.symbols_on_page = abs(symbols_on_page)
        self.item_count = len(text)
        self.page_count = self.item_count % abs(symbols_on_page)

    def count_items_on_page(self, page: int):
        if page >= self.page_count:
            raise PaginationError(f'Exception: Invalid index. Page {page} is missing. Pages indexing starts with 0.')
        else:
            max_item_count = (page + 1) * self.symbols_on_page
            if self.item_count < max_item_count:
                return self.symbols_on_page - (max_item_count - self.item_count)
            return self.symbols_on_page

    def display_page(self, page: int):
        if page >= self.page_count:
            raise PaginationError(f'Exception: Invalid index. Page {page} is missing. Pages indexing starts with 0.')
        else:
            start = page * self.symbols_on_page
            return self.text[start:start+self.symbols_on_page]

    def find_all_indexes(self, sub):
        start = 0
        while True:
            start = self.text.find(sub, start)
            if start == -1: return
            yield start
            start += len(sub)

    def find_page(self, substring_for_search: str):
        count_substring_for_search = self.text.count(substring_for_search)
        if count_substring_for_search == 0:
            raise PaginationError(f'{substring_for_search} is missing on the pages')
        else:
            indexes = list(self.find_all_indexes(substring_for_search))
            return [i // self.symbols_on_page for i in indexes]


if __name__ == '__main__':
    pages = Pagination('Your beautiful text', 5)
    print(pages.item_count)
    print(pages.page_count)
    print(pages.count_items_on_page(0))
    print(pages.count_items_on_page(3))
    #print(pages.count_items_on_page(4))
    print(pages.display_page(0))
    print(pages.display_page(1))
    print(pages.find_page('Your'))
    print(pages.find_page('beautiful'))
    print(pages.find_page('e'))
    #print(pages.find_page('great'))

