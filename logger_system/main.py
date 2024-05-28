from logger_system.debug_log_processor import DebugLogProcessor
from logger_system.error_log_processor import ErrorLogProcessor
from logger_system.info_log_processor import InfoLogProcessor
from logger_system.log_processor import LogProcessor

error_logger = ErrorLogProcessor(None)
debug_logger = DebugLogProcessor(error_logger)
log_object = InfoLogProcessor(debug_logger)

log_object.log(LogProcessor.ERROR, 'exception found')
log_object.log(LogProcessor.DEBUG, 'debug it')
log_object.log(LogProcessor.INFO, 'info')
