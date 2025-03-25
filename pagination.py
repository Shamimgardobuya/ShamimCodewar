# TODO: complete this class

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
       # The code snippet `self.items_per_page = items_per_page` is storing the number of items that
       # fit within a single page in the PaginationHelper class instance.
        self.items_per_page = items_per_page
        self._cached_partition = [self.collection[i:i+self.items_per_page] for i in range(0, len(self.collection), self.items_per_page)]
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    def partition(self):
        return self._cached_partition

    # returns the number of pages
    def page_count(self):
        blocks = self.partition()
        return len(blocks)

        
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        #dependant on length of items, and definitely page, 
        #split the collection in items of 4 for each iteration
        pages = self.page_count()
        blocks = self._cached_partition
        if page_index in range(pages) :  
            return len(blocks[page_index])
        return -1
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if 0 <= item_index < len(self.collection):
            return item_index // self.items_per_page  # Direct calculation of page index
        return -1
        # if 0 <= item_index < len(self.collection):
        #     item = self.collection[item_index]
        #     blocks = self.partition()
        #     for i, val in enumerate(blocks):
        #         if item in  val:
        #             return i
        # return -1
        

book = PaginationHelper(['a','b','c','d','e','f'], 4)

print(book.page_item_count(2))