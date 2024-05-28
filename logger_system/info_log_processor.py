from logger_system.log_processor import LogProcessor


class InfoLogProcessor(LogProcessor):
    def log(self, log_level, message):
        if log_level == self.INFO:
            print(f'INFO: {message}')
        else:
            super().log(log_level, message)
