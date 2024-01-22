class LLMResponse():
    def __init__(self, content, status_code = 200, errors = []):
        self.status_code = status_code
        self.errors = errors
        self.content = content