import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
print(os.getenv("XRAY_API_BASE_URL"))