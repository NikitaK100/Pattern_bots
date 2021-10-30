import os

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
admins = os.getenv('ADMIN_ID')

# DATA_NAME = os.getenv('DATA_NAME')
# PASSWORD_DB = os.getenv('PGPASSWORD')
# HOST_DB = os.getenv('PGHOST')
# DATABASE = os.getenv('DATABASE')
