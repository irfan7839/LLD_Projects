from logger_system.log_processor import LogProcessor


class ErrorLogProcessor(LogProcessor):
    def log(self, log_level, message):
        if log_level == self.ERROR:
            print(f'ERROR: {message}')
        else:
            super().log(log_level, message)
