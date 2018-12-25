class Hash:

    def get_element(self, bucket, keyword):
        for element in bucket:
            if element[0] == keyword:
                return element
        return None


    def lookup(self, hashtable, keyword):
        element = self.get_element(self.get_bucket(hashtable, keyword), keyword)
        if element:
            return element[1]
        return None


    def update(self, hashtable, keyword, value):
        bucket = self.get_bucket(hashtable, keyword)

        element = self.get_element(bucket, keyword)
        if element:
            element[1] = value
        else:
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
