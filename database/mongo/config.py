from urllib.parse import quote_plus

from motor.motor_asyncio import AsyncIOMotorClient

username = "admin"
password = "admin"
host = "0.0.0.0"
database = "ecom"
port = 27017

escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

# connection_string = f"mongodb://{escaped_username}:{escaped_password}@{host}:{port}/{database}"
# connection_string = f"mongodb://{host}:{port}/{database}"
connection_string = "mongodb://mongodb:27017/ecom"

client = AsyncIOMotorClient(connection_string)

db = client[database]

FORMS = db["forms"]
