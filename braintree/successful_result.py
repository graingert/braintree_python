class SuccessfulResult:
    def __init__(self, attributes):
        self.is_success = True
        self.attributes = attributes

    def __getattr__(self, key):
        if key in self.attributes:
            return self.attributes[key]
        else:
            return None