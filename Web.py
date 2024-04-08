import webbrowser

class Browser:

    def __init__(self):
        self.url_wikipedia = "https://en.wikipedia.org/wiki/{}"
        self.url_google = "https://www.google.com/search?q={}"
        self.url_youtube = "https://www.youtube.com/results?search_query={}"

    def open_url_wikipedia(self,query):
        webbrowser.open(self.url_wikipedia.format(query))
        
    def open_url_google(self,query):
        webbrowser.open(self.url_google.format(query))
    
    def open_url_youtube(self,query):
        webbrowser.open(self.url_youtube.format(query))
 
        


