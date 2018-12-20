class WebCrawler():

    def get_next_target(self, page):
        start_link = page.find('<a href=')
        if start_link == -1:
            return None, 0

        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]

        return url, end_quote


    def get_page(self, url):
        try:
            import urllib
            return urllib.urlopen(url).read()
        except:
            return ""


    def union(self, a, b):
        for e in b:
            if e not in a:
                a.append(e)
