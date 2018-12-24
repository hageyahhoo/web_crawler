import unittest
from web_crawler.hash import Hash

class TestHash(unittest.TestCase):

    def setUp(self):
        self.func = Hash()


    def test_hash_function_emptyString(self):
        self.assertEqual(self.func.hash_function('', 12), 0)

    def test_hash_function_normal(self):
        self.assertEqual(self.func.hash_function('a', 12), 1)
        self.assertEqual(self.func.hash_function('b', 12), 2)
        self.assertEqual(self.func.hash_function('c', 12), 3)
        self.assertEqual(self.func.hash_function('LIJ', 12), 7)


    def test_make_hash_table(self):
        hashtable = self.func.make_hash_table(3)

        self.assertEqual(len(hashtable), 3)
        self.assertEqual(hashtable, [[], [], []])

        hashtable[1].append('url')
        self.assertEqual(hashtable, [[], ['url'], []])


if __name__ == '__main__':
    unittest.main()
