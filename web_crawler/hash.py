class Hash:

    def hash_function(self, keyword, buckets):
        hash_value = 0
        for char in keyword:
            hash_value = (hash_value + ord(char)) % buckets
        return hash_value

    def make_hash_table(self, buckets):
        hashtable = []
        for unused in range(0, buckets):
            hashtable.append([])
        return hashtable
