class LogProcessor:
    INFO = 1
    DEBUG = 2
    ERROR = 3

    def __init__(self, next_processor):
        self.next_processor = next_processor

    def log(self, log_level, message):
        if self.next_processor:
            self.next_processor.log(log_level, message)
