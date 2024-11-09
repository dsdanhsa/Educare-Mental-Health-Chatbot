# chatbot/logging_config.py

import logging
import sys
import io

# Reconfigure stdout và stderr để sử dụng encoding 'utf-8'
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if sys.stderr.encoding.lower() != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Định nghĩa SafeStreamHandler để xử lý UnicodeEncodeError
class SafeStreamHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            msg = self.format(record)
            self.stream.write(msg + self.terminator)
            self.flush()
        except UnicodeEncodeError:
            # Thay thế các ký tự không thể mã hóa bằng '?'
            msg = self.format(record).encode('utf-8', errors='replace').decode('utf-8')
            self.stream.write(msg + self.terminator)
            self.flush()
        except Exception:
            self.handleError(record)

# Khởi tạo logging
logger = logging.getLogger('chatbot_logger')
logger.setLevel(logging.INFO)

# Tạo FileHandler với encoding 'utf-8'
file_handler = logging.FileHandler("chatbot.log", encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Tạo SafeStreamHandler với sys.stdout đã được reconfigure
stream_handler = SafeStreamHandler(sys.stdout)
stream_formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
stream_handler.setFormatter(stream_formatter)
logger.addHandler(stream_handler)
