import webbrowser

class Media:

    def __init__(self,query):
        self.url = f"www.youtube.com/search?q={query}"

    def open_url(self):
        webbrowser.open(self.url)