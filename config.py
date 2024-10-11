 
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-default-secret-key'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/yourdatabase'
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    PADDLE_VENDOR_ID = os.environ.get('PADDLE_VENDOR_ID')
    GOOGLE_CLOUD_API_KEY = os.environ.get('GOOGLE_CLOUD_API_KEY')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    PADDLE_CLIENT_TOKEN = os.environ.get('PADDLE_CLIENT_TOKEN')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit
    PROPAGATE_EXCEPTIONS = True
    WTF_CSRF_ENABLED = True
    WTF_CSRF_CHECK_DEFAULT = False
    CSRF_ENABLED = True