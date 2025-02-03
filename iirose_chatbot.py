from loguru import logger
from API.api_iirose import APIIirose
from globals.globals import GlobalVal
from API.api_get_config import get_master_id
from API.decorator.command import on_command, MessageType
import asyncio
from openai import OpenAI

API = APIIirose()

# 初始化聊天机器人，在这里设置你的API密钥和基础URL
client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="YOUR_BASE_URL",
)


# 定义一个简单的聊天机器人类
class ChatBot:
    def __init__(self, client):
        self.client = client

    async def get_response(self, text):
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": text,
                    }
                ],
                model="MODAL_NAME", # 例如deepseek-ai/DeepSeek-V3 请参考api网站命名 这里是手动切换
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            logger.error(f"Error in chat completion: {e}")
            return None


# 初始化 chat_bot
chat_bot = ChatBot(client)


@on_command(
    ".聊天", True, command_type=[MessageType.room_chat, MessageType.private_chat]
)
async def chat_command(Message, text):
    prefix = "\\\\\\* "  # 定义前缀
    if text.strip() == "帮助":
        help_text = f"""{prefix}**聊天机器人帮助**

使用方法：
- 发送 '.聊天 <你想说的话>' 与 AI 对话。
- 发送 '.聊天帮助' 查看此帮助信息。

例如：
- '.聊天 你好吗？'
- '.聊天 今天天气怎么样？'
        """
        await API.send_msg(Message, help_text)
    elif not text.strip():  # 检查 text 是否为空或仅包含空格
        await API.send_msg(Message, f"{prefix}请输入您想说的话。")
    else:
        # 使用 chat_bot 进行处理
        response = await chat_bot.get_response(text)
        if response:
            await API.send_msg(Message, f"{prefix}{response}")  # 添加前缀
        else:
            await API.send_msg(Message, f"{prefix}An error occurred.")  # 添加前缀


async def on_init():
    logger.info("插件初始化完成，聊天机器人已加载")
