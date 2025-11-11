
BaseCaching = __import__('base_caching').BaseCaching



class LRUCache(BaseCaching):


    def __init__(self):
        super().__init__()
        self.head, self.tail = '-', '='
        self.next, self.prev = {}, {}
        self.handle(self.head, self.tail)

    def handle(self, head, tail):
      
        self.next[head], self.prev[tail] = tail, head

    def _remove(self, key):
        
        self.handle(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def _add(self, key, item):
     
        self.cache_data[key] = item
        self.handle(self.prev[self.tail], key)
        self.handle(key, self.tail)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.next[self.head]))
            self._remove(self.next[self.head])

    def put(self, key, item):

        if key is not None and item is not None:
            if key in self.cache_data:
                self._remove(key)
            self._add(key, item)

    def get(self, key):
       
        if key is None or key not in self.cache_data.keys():
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            self._remove(key)
            self._add(key, value)
            return value
