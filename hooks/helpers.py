"""Helper classes"""

from hooks import templates


class ResponseProcess:
    """Very simple class for a response process

        Init::
            text An text from slack

        Methods::
            make_response Return a message template by key
    """
    def __init__(self, text):
        self.text = text

    DEFAULT_WORDS = {
        'algos-resources': templates.ALGOS_RESOURCES,
        'hitchhikers-zen': templates.HITCHHIKERS_ZEN
    }

    def make_response(self):
        if self.text.lower() in self.DEFAULT_WORDS.keys():
            return self.DEFAULT_WORDS[self.text]
