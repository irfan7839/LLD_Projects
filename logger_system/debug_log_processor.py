from logger_system.log_processor import LogProcessor


class DebugLogProcessor(LogProcessor):
    def log(self, log_level, message):
        if log_level == self.DEBUG:
            print(f'DEBUG: {message}')
        else:
            super().log(log_level, message)
