import feedparser
from kivy.storage.jsonstore import JsonStore

class News:
    def __init__(self, **kwargs):
        self.store = JsonStore("parameters/ordo_news.json")
        self.rss_list = self.store.get("rss_list")
        self.news = self.load_news()

    def load_news(self):
        news=[]
        for rss in self.rss_list:
            d = feedparser.parse(rss)
            for entry in d.entries:
                news.append({"title":entry.title, "description":entry.description, "published":entry.published})
        return news
