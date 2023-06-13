import os
from dotenv import load_dotenv
from pyrogram import Client


load_dotenv()

Bot = Client(
    "QR Code Bot",
    bot_token=os.environ.get("BOT_TOKEN", "5945201344:AAGuw0vSH5z3Lmc3S08bAtJEcKkZ2nAuftI"),
    api_id=int(os.environ.get("API_ID", "29390803")),
    api_hash=os.environ.get("API_HASH", "4227e730acf4483f59ad2799c2bd063f"),
    plugins=dict(root="plugins")
)

Bot.run()
