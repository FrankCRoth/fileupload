import os
MAX_CONTENT_LENGTH = 1024 * 1024 * 5000 # 5 GB
UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']
UPLOAD_PATH = os.getenv('UPLOAD_PATH') or 'uploads' 