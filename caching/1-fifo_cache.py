
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):


    def __init__(self):

        super().__init__()

    def put(self, key, item):

        if key and item:
            self.cache_data.update({key: item})
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                for k, v in self.cache_data.items():
                    print('DISCARD:', list(self.cache_data.keys())[0])
                    break
                self.cache_data.pop(k)
            else:
                pass

    def get(self, key):

        if key is None:
            return None
        return self.cache_data.get(key)
