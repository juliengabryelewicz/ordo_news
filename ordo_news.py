import plugin
from .screens.news_screen import NewsScreen

class NewsPlugin(plugin.PluginObject):

	def get_main_screen():
		return NewsScreen()

	def get_screens():
		return [NewsScreen()]