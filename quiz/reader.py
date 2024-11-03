class TextReader():
    def __init__(self, article):
        self._article = article
        with open(self._article, 'r') as file:
            self._text = file.read()

    def text(self):
        return self._text

