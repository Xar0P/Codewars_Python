# https://www.codewars.com/kata/515bb423de843ea99400000a/train/python

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.pages = self.items_in_page(self.collection)

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        num = 0
        for i in range(0, len(self.collection), self.items_per_page):
            num += 1
        return num

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        try:
            return len(self.pages[page_index])
        except KeyError:
            return -1
    
    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        for page in self.pages:
            if item_index + 1 in self.pages[page]:
                return page
        return -1

    def items_in_page(self, collection):
        collection = list(collection)
        pages = {}

        for i in range(0, self.page_count()):
            for j in range(0,self.items_per_page):
                if not i in pages.keys():
                    pages[i] = [collection[0]]
                elif not len(collection) == 0:
                    pages[i].append(collection[0])

                if not len(collection) == 0:
                    collection.pop(0)

        return pages


collection = range(1, 25)
helper = PaginationHelper(collection, 10)
print(helper.page_count())
print(helper.page_index(23))
print(helper.item_count())
print(helper.page_item_count(3))
