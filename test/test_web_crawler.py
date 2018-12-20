import unittest
from web_crawler.web_crawler import WebCrawler

class TestWebCrawler(unittest.TestCase):

    def setUp(self):
        self.func = WebCrawler()


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


    def test_get_page_success(self):
        self.assertNotEqual(self.func.get_page('https://www.google.com'), '')

    def test_get_page_failure(self):
        self.assertEqual(self.func.get_page('hoge'), '')


    def test_union(self):
        a = [1, 2, 3]
        b = [1, 4, 5]
        self.func.union(a, b)
        self.assertEqual(a, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
