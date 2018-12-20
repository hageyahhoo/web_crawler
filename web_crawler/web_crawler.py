class WebCrawler():

    def get_page(self, url):
        try:
            import urllib
            return urllib.urlopen(url).read()
        except:
            return ""


    def get_next_target(self, page):
        start_link = page.find('<a href=')
        if start_link == -1:
            return None, 0

        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]

        return url, end_quote


    def get_all_links(self, page):
        links = []
        while True:
            url, endPos = self.get_next_target(page)
            if url:
                links.append(url)
                page = page[endPos:]
            else:
                break
        return links


    def add_to_index(self, index, keyword, url):
        for k, u in index:
            if k == keyword:
                if url not in u:
                    u.append(url)
                return
        index.append([keyword, [url]])


    def add_page_to_index(self, index, url, content):
        words = content.split()
        for word in words:
            self.add_to_index(index, word, url)


    def union(self, a, b):
        for e in b:
            if e not in a:
                a.append(e)
