import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import schedule
import time
from loguru import logger
from config import Config
from data.polymarket import PolymarketClient
from core.analyzer import MarketAnalyzer
from external.telegram import TelegramBot

def run_daily_report():
    logger.info("开始生成每日市场简报...")
    client = PolymarketClient()
    markets = client.get_markets(limit=Config.MARKET_LIMIT)
    logger.info(f"获取到 {len(markets)} 个市场")

    analyzer = MarketAnalyzer(Config.ANTHROPIC_API_KEY)
    report = analyzer.analyze(markets)

    bot = TelegramBot(Config.TELEGRAM_BOT_TOKEN, Config.TELEGRAM_CHAT_ID)
    bot.send_report("📊 *Polymarket 每日简报*\n\n" + report)

def main():
    Config.validate()
    logger.add("logs/bot.log", rotation="1 day", retention="7 days")
    run_daily_report()
    schedule.every().day.at(f"{Config.SCHEDULE_HOUR:02d}:00").do(run_daily_report)
    logger.info(f"定时任务已设置，每天 {Config.SCHEDULE_HOUR}:00 运行")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
