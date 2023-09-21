from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from ordo_news.model.news import News

class NewsScreen(Screen):

	list_news = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(NewsScreen, self).__init__(**kwargs)

	def on_enter(self, *args):
		self.news_list = News()
		Clock.schedule_once(self.show_news)

	def show_news(self,dt):
		self.list_news.clear_widgets()
		if len(self.news_list.news) > 0 :
			self.list_news.height=50*len(self.news_list.news)
			self.list_news.parent.height=self.list_news.height
			for news in self.news_list.news:
				title = (news["title"][:100] + '..') if len(news["title"]) > 100 else news["title"]
				item = AccordionItem(title=title, width=800)
				item.add_widget(Label(text=('[b]' +news["title"] + '[/b]' + '\n' + news["description"]),text_size=(800, None), markup=True))
				self.list_news.add_widget(item)