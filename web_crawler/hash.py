class Hash:

    def lookup(self, hashtable, keyword):
        # TODO Refactor
        bucket = self.get_bucket(hashtable, keyword)
        for k, v in bucket:
            if k == keyword:
                return v
        return None


    def update(self, hashtable, keyword, value):
        # TODO Refactor
        bucket = self.get_bucket(hashtable, keyword)
        for k, v in bucket:
            if k == keyword:
                # Update
                v = value
                return hashtable
        bucket.append([keyword, value])
        return hashtable


    def get_bucket(self, hashtable, keyword):
        return hashtable[self.hash_string(keyword, len(hashtable))]


    def hash_string(self, keyword, buckets_size):
        hash_string = 0
        for char in keyword:
            hash_string = (hash_string + ord(char)) % buckets_size
        return hash_string

    def make_hashtable(self, buckets_size):
        # Don't use [[]] * n
        hashtable = []
        for unused in range(0, buckets_size):
            hashtable.append([])
        return hashtable
