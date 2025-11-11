from collections import OrderedDict, defaultdict
from utils.singleton import singleton

@singleton
class KVStore:
    def __init__(self, capacity=4):
        self.store = OrderedDict()
        self.value_count = defaultdict(int)
        # self.store = {} # main store
        # self.value_count = {} # helper to count values for keys
        self.transactions = [] # stack to keep track of txns [key, val]
        self.capacity = capacity

    def _evict_if_needed(self):
        print("store is: ", self.store)
        if len(self.store) >= self.capacity:
            lru_key, lru_val = self.store.popitem(last=True)
            self.value_count[lru_val] -= 1
        

    def set(self, key, value):

        # if we are in txns
        if self.transactions:
            # save the original value for rollback
            if key not in self.transactions[-1]:
                self.transactions[-1][key] = self.store.get(key)

        # update the value count for old values
        old_value = self.store.get(key)
        if old_value is not None:
            self.value_count[old_value] -= 1
        
        # set the new value
        self.store[key] = value
        self.store.move_to_end(key, last=False)
        self.value_count[value] = self.value_count.get(value, 0) + 1

        self._evict_if_needed()

    def get(self, key):
        if key not in self.store:
            return None
        self.store.move_to_end(key, last=False)
        return self.store.get(key)
    
    def delete(self, key):
        """
        Here is the rationale:

        Transactions allow undoing (rollback):
        Suppose you're in a transaction and you delete a key. 
        Later, you might decide to rollback the transaction. 
        To undo the delete, you need to know what the value was before deletion.

        Avoid overwriting previous state:
        If the key was already recorded as part of this transaction 
        (due to a prior set or another delete), we don’t want to overwrite the 
        earlier state. That’s why there's a check: if key not in self.transactions[-1].
        """
        if key not in self.store:
            print("Invalid key")
            return
        
        # if the key present, check if we are in txn
        if self.transactions:
            if key not in self.transactions[-1]:
                self.transactions[-1][key] = self.store.get(key)

        old_value = self.store.get(key)
        self.value_count[old_value] -= 1
        del self.store[key]

    def count(self, value):
        return self.value_count.get(value, 0)
    
    def begin(self):
        return self.transactions.append({})
    
    def roll_back(self):
        if not self.transactions:
            print("No Transaction")
            return
        
        last_changes = self.transactions.pop()
        for key, old_value in last_changes.items():
            # rever value
            new_value = self.store.get(key)
            if new_value is not None:
                self.value_count[new_value] -= 1
            
            if old_value is None:
                self.store.pop(key, None)
            else:
                self.store[key] = old_value
                self.store.move_to_end(key, last=False)
                self.value_count[old_value] = self.value_count.get(old_value, 0) + 1

    def commit(self):
        if not self.transactions:
            print("No Transaction")
            return
        
        self.transactions.clear()
