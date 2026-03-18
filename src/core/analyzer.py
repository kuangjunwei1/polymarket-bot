import anthropic
from loguru import logger

class MarketAnalyzer:
    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)

    def analyze(self, markets: list) -> str:
        if not markets:
            return "暂无市场数据"

        market_summary = []
        for m in markets[:10]:
            tokens = m.get("tokens", [])
            yes_price = next((t["price"] for t in tokens if t.get("outcome") == "Yes"), "N/A")
            market_summary.append(
                f"- {m.get('question', '未知')} | Yes概率: {yes_price} | 成交量: ${m.get('volume', 0):,.0f}"
            )

        prompt = f"""你是一个预测市场分析师。以下是 Polymarket 今日热门市场数据：

{chr(10).join(market_summary)}

请用中文生成一份简洁的市场简报（200��以内），包括：
1. 最值得关注的2-3个市场及其含义
2. 整体市场情绪判断
3. 一句话投资者提示

格式要适合 Telegram 消息，使用 emoji 增加可读性。"""

        try:
            message = self.client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text
        except Exception as e:
            logger.error(f"Claude 分析失败: {e}")
            return "AI 分析暂时不可用"
