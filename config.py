
from dotenv import load_dotenv
import os


load_dotenv()



ALLOWED_EXTENSIONS =['png', 'jpg', 'jpeg']
 


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
class ApplicationConfig:
    SECRET_KEY = os.environ["SECRET_KEY"]
