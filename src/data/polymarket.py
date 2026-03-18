import requests
from loguru import logger

CLOB_BASE = "https://clob.polymarket.com"

class PolymarketClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def get_markets(self, limit: int = 20) -> list:
        try:
            resp = self.session.get(
                f"{CLOB_BASE}/markets",
                params={"limit": limit, "active": True},
                timeout=10
            )
            resp.raise_for_status()
            return resp.json().get("data", [])
        except Exception as e:
            logger.error(f"获取市场数据失败: {e}")
            return []
