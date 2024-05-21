from collections import deque
class LRUCache:
    '''
    capacity : int > cache size
    get : int > get val if key in cache
    get,put time complex o(1)
    recently used value exists cache[-1] 
    '''
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.memory={}
        self.cache_keys=deque([])

    def _access_cache(self,key):
        '''
        cache hit/miss judge
        '''
        try: #cache hit
            key_index = self.cache_keys.index(key)
        except ValueError: #cache miss
            key_index = -1
        return key_index
    
    def _swap(self,key):
        '''
        swap in cache
        #TODO : implements double linked list... or use OrderedDict
        '''
        self.cache_keys.remove(key)
        self.cache_keys.append(key)
        
    def _append(self,key):
        '''
        if cache size >=  capacity, popleft
        '''
        if len(self.cache_keys) >= self.capacity:
            old = self.cache_keys.popleft()
            del self.memory[old]
        self.cache_keys.append(key)

    def get(self, key: int) -> int:
        '''
        if key exists, return value, else return -1
        '''
        key_index = self._access_cache(key)
        if key_index >= 0:
            value = self.memory[key]
            self._swap(key)
        else:
            value = -1
        return value

    def put(self, key: int, value: int) -> None:
        '''
        if key exists, update key
        '''
        key_index = self._access_cache(key)
        if key_index >= 0:
            self._swap(key)
        else:
            self._append(key)
        self.memory[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)