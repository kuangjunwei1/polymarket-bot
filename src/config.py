import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
    SCHEDULE_HOUR = int(os.getenv("SCHEDULE_HOUR", "9"))
    MARKET_LIMIT = int(os.getenv("MARKET_LIMIT", "20"))

    @classmethod
    def validate(cls):
        missing = [k for k, v in {
            "ANTHROPIC_API_KEY": cls.ANTHROPIC_API_KEY,
            "TELEGRAM_BOT_TOKEN": cls.TELEGRAM_BOT_TOKEN,
            "TELEGRAM_CHAT_ID": cls.TELEGRAM_CHAT_ID,
        }.items() if not v]
        if missing:
            raise ValueError(f"缺少环境变量: {', '.join(missing)}")
