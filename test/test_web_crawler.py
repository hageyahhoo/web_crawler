import unittest
from web_crawler.web_crawler import WebCrawler

class TestWebCrawler(unittest.TestCase):

    def setUp(self):
        self.func = WebCrawler()


    def test_get_page_success(self):
        self.assertNotEqual(self.func.get_page('https://www.google.com'), '')

    def test_get_page_failure(self):
        self.assertEqual(self.func.get_page('hoge'), '')


    def test_get_next_target_NotFound(self):
        page = 'foo <a hre> bar'
        url, end_quote = self.func.get_next_target(page)
        self.assertIsNone(url)
        self.assertEqual(end_quote, 0)

    def test_get_next_target_Found(self):
        page = 'foo <a href="http://www.google.com"> bar'
        url, end_quote = self.func.get_next_target(page)
        self.assertEqual(url, 'http://www.google.com')
        self.assertEqual(end_quote, 34)


    def test_get_all_links_HasNoLink(self):
        page = 'foo <a hre> bar'
        self.assertEqual(self.func.get_all_links(page), [])

    def test_get_all_links_HasSomeLink(self):
        page = 'foo <a href="http://www.google.com"> bar <a href="http://www.twitter.com"> baz'
        self.assertEqual(self.func.get_all_links(page), ["http://www.google.com", "http://www.twitter.com"])


    def test_add_to_index_simply(self):
        index = {}
        self.func.add_to_index(index, "google", "http://www.google.com")
        self.func.add_to_index(index, "twitter", "http://www.twitter.com")
        self.assertEqual(len(index), 2)
        self.assertEqual(index["google"], ["http://www.google.com"])
        self.assertEqual(index["twitter"], ["http://www.twitter.com"])

    def test_add_to_index_duplicateKeyword(self):
        index = {}
        self.func.add_to_index(index, "google", "http://www.google.com")
        self.func.add_to_index(index, "google", "http://www.twitter.com")
        self.assertEqual(len(index), 1)
        self.assertEqual(index["google"], ["http://www.google.com", "http://www.twitter.com"])

    def test_add_to_index_duplicateKeywordAndURL(self):
        index = {}
        self.func.add_to_index(index, "google", "http://www.google.com")
        self.func.add_to_index(index, "google", "http://www.twitter.com")
        self.func.add_to_index(index, "google", "http://www.google.com")
        self.assertEqual(len(index), 1)
        self.assertEqual(index["google"], ["http://www.google.com", "http://www.twitter.com"])


    def test_add_page_to_index_HasNoContent(self):
        index = {}
        self.func.add_page_to_index(index, "http://www.google.com", "")
        self.assertEqual(len(index), 0)

    def test_add_page_to_index_HasContent(self):
        index = {}
        self.func.add_page_to_index(index, "http://www.google.com", "This is Google")
        self.assertEqual(len(index), 3)
        self.assertEqual(index["This"], ["http://www.google.com"])
        self.assertEqual(index["is"], ["http://www.google.com"])
        self.assertEqual(index["Google"], ["http://www.google.com"])


    def test_union(self):
        a = [1, 2, 3]
        b = [1, 4, 5]
        self.func.union(a, b)
        self.assertEqual(a, [1, 2, 3, 4, 5])


    def test_lookup_NotFound(self):
        index = {}
        self.func.add_to_index(index, "google", "http://www.google.com")
        self.func.add_to_index(index, "twitter", "http://www.twitter.com")
        self.assertIsNone(self.func.lookup(index, "Facebook"))

    def test_lookup_Found(self):
        index = {}
        self.func.add_to_index(index, "google", "http://www.google.com")
        self.func.add_to_index(index, "twitter", "http://www.twitter.com")
        result = self.func.lookup(index, "twitter")
        self.assertEqual(len(result), 1)
        self.assertEqual(result, ["http://www.twitter.com"])


if __name__ == '__main__':
    unittest.main()
