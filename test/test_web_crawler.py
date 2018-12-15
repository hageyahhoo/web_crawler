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


if __name__ == '__main__':
    unittest.main()
