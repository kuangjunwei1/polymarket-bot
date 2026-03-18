import re
import requests
from loguru import logger

class TelegramBot:
    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id
        self.base_url = f"https://api.telegram.org/bot{token}"

    def send_report(self, text: str) -> bool:
        if len(text) > 4000:
            text = text[:4000] + "\n...(已截断)"
        try:
            resp = requests.post(
                f"{self.base_url}/sendMessage",
                json={"chat_id": self.chat_id, "text": text},
                timeout=10
            )
            resp.raise_for_status()
            logger.info("报告发送成功")
            return True
        except Exception as e:
            logger.error(f"Telegram 发送失败: {e}")
            return False
