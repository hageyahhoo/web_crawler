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
        if keyword in index:
            if url not in index[keyword]:
                index[keyword].append(url)
            return
        index[keyword] = [url]


    def add_page_to_index(self, index, url, content):
        words = content.split()
        for word in words:
            self.add_to_index(index, word, url)


    def union(self, a, b):
        for e in b:
            if e not in a:
                a.append(e)


    def crawl_web(self, seed):
        toCrawl = [seed]
        crawled = []
        index = {}

        while toCrawl:
            page = toCrawl.pop()
            if page not in crawled:
                content = self.get_page(page)
                self.add_page_to_index(index, page, content)
                self.union(toCrawl, self.get_all_links(content))
                crawled.append(page)

        return index


    def lookup(self, index, keyword):
        if keyword in index:
            return index[keyword]
        return None
