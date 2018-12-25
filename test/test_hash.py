import unittest
from web_crawler.hash import Hash

class TestHash(unittest.TestCase):

    def setUp(self):
        self.func = Hash()


    def test_lookup_Found(self):
        hashtable = self.func.make_hashtable(3)
        self.func.update(hashtable, 'foo', 1)
        self.func.update(hashtable, 'bar', 2)
        self.func.update(hashtable, 'baz', 3)

        self.assertEqual(self.func.lookup(hashtable, 'bar'), 2)

    def test_lookup_NotFound(self):
        hashtable = self.func.make_hashtable(3)
        self.func.update(hashtable, 'foo', 1)
        self.func.update(hashtable, 'bar', 2)
        self.func.update(hashtable, 'baz', 3)

        self.assertIsNone(self.func.lookup(hashtable, 'are'))


    def test_update_Add(self):
        hashtable = self.func.make_hashtable(3)
        self.func.update(hashtable, 'foo', 1)

        self.assertEqual(len(hashtable[0]), 1)
        self.assertEqual(hashtable[0][0], ['foo', 1])
        self.assertEqual(len(hashtable[1]), 0)
        self.assertEqual(len(hashtable[2]), 0)

    def test_update_Update(self):
        hashtable = self.func.make_hashtable(3)
        self.func.update(hashtable, 'foo', 1)
        self.func.update(hashtable, 'foo', 2)
        self.assertEqual(len(hashtable[0]), 1)
        self.assertEqual(hashtable[0][0], ['foo', 1])
        self.assertEqual(len(hashtable[1]), 0)
        self.assertEqual(len(hashtable[2]), 0)


    def test_get_bucket(self):
        hashtable = [[1], [2], [3]]
        # ord('a') = 97, buckets_size = 3, 97 % 3 = 1
        self.assertEqual(self.func.get_bucket(hashtable, 'a'), hashtable[1])
        self.assertEqual(self.func.get_bucket(hashtable, 'a'), [2])


    def test_hash_string_EmptyString(self):
        self.assertEqual(self.func.hash_string('', 12), 0)

    def test_hash_string_Normal(self):
        self.assertEqual(self.func.hash_string('a', 12), 1)
        self.assertEqual(self.func.hash_string('b', 12), 2)
        self.assertEqual(self.func.hash_string('c', 12), 3)
        self.assertEqual(self.func.hash_string('LIJ', 12), 7)


    def test_make_hashtable(self):
        hashtable = self.func.make_hashtable(3)

        self.assertEqual(len(hashtable), 3)
        self.assertEqual(hashtable, [[], [], []])

        # Don't use [[]] * n
        hashtable[1].append('url')
        self.assertEqual(hashtable, [[], ['url'], []])


if __name__ == '__main__':
    unittest.main()
