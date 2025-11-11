BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):

    def put(self, key, item):

        if (key is not None and item is not None):
            self.cache_data[key] = item

    def get(self, key):

        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
