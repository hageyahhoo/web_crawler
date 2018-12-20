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
        self.assertEqual(url, None)
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
        index = []
        self.func.add_to_index(index, "google", "http://www.google.com")
        self.func.add_to_index(index, "twitter", "http://www.twitter.com")
        self.assertEqual(len(index), 2)
        self.assertIn(["google", ["http://www.google.com"]], index)
        self.assertIn(["twitter", ["http://www.twitter.com"]], index)

    def test_add_to_index_duplicateKeyword(self):
        index = []
        self.func.add_to_index(index, "google", "http://www.google.com")
        self.func.add_to_index(index, "google", "http://www.twitter.com")
        self.assertEqual(len(index), 1)
        self.assertIn(["google", ["http://www.google.com", "http://www.twitter.com"]], index)

    def test_add_to_index_duplicateKeywordAndURL(self):
        index = []
        self.func.add_to_index(index, "google", "http://www.google.com")
        self.func.add_to_index(index, "google", "http://www.twitter.com")
        self.func.add_to_index(index, "google", "http://www.google.com")
        self.assertEqual(len(index), 1)
        self.assertIn(["google", ["http://www.google.com", "http://www.twitter.com"]], index)


    def test_add_page_to_index_HasNoContent(self):
        index = []
        self.func.add_page_to_index(index, "http://www.google.com", "")
        self.assertEqual(len(index), 0)

    def test_add_page_to_index_HasContent(self):
        index = []
        self.func.add_page_to_index(index, "http://www.google.com", "This is Google")
        print index
        self.assertEqual(len(index), 3)
        self.assertIn(["This", ["http://www.google.com"]], index)
        self.assertIn(["is", ["http://www.google.com"]], index)
        self.assertIn(["Google", ["http://www.google.com"]], index)


    def test_union(self):
        a = [1, 2, 3]
        b = [1, 4, 5]
        self.func.union(a, b)
        self.assertEqual(a, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
