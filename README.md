# Polymarket 数据分析机器人

每天自动拉取 Polymarket 热门市场数据，用 Claude AI 生成分析简报，推送到 Telegram。

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# 编辑 .env 填入你的 key
cd src && python main.py
```

## 环境变量

| 变量 | 说明 |
|------|------|
| ANTHROPIC_API_KEY | Claude API Key |
| TELEGRAM_BOT_TOKEN | Telegram Bot Token |
| TELEGRAM_CHAT_ID | 推送目标频道/群组 ID |
| SCHEDULE_HOUR | 每天推送时间（默认9点） |
| MARKET_LIMIT | 拉取市场数量（默认20） |

## 项目结构

```
src/
├── main.py              # 入口 + 定时调度
├── config.py            # 配置管理
├── data/polymarket.py   # Polymarket API 客户端
├── core/analyzer.py     # Claude AI 分析
└── external/telegram.py # Telegram 推送
```
