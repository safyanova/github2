import os
from dotenv import load_dotenv

STAGE = os.environ["STAGE"]
print(STAGE)