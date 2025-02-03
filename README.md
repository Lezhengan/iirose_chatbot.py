# iirose_chatbot.py
蔷薇花园的一个基于小草机器人的openai适配器（支持第三方）

```markdown
# iirose Chatbot Plugin

这是一个基于 iirose 平台的聊天机器人插件，它使用 支持 OpenAI 的输入输出格式的模型进行对话。
例如deepseek、qwen等

## 功能

-   使用 `.聊天 <你想说的话>` 指令与 AI 对话。
-   提供帮助信息，使用 `.聊天 帮助` 查看。
-   仅将用户输入的实际对话内容发送到 OpenAI API，不会发送 `.聊天` 前缀。

## 安装

1.  将插件文件（如 `plugin.py`）放入 iirose 平台的插件目录。
2.  在 iirose 平台中启用该插件。
3.  配置 OpenAI API 密钥和基础 URL。你需要在插件代码中替换以下内容：

    ```python
    client = OpenAI(
        api_key="YOUR_API_KEY",  # 替换为你的 OpenAI API 密钥
        base_url="YOUR_BASE_URL", # 替换为你的 OpenAI API 基础 URL
    )
    ```

## 使用方法

-   在 iirose 平台聊天窗口中，输入 `.聊天 <你想说的话>`，例如：
    ```
    .聊天 你好吗？
    .聊天 今天天气怎么样？
    ```
-   输入 `.聊天 帮助` 查看插件帮助信息。
-   如果输入 `.聊天` 或 `.聊天  ` 等不带实际对话内容的指令，会提示用户输入内容。

## 配置

-   **OpenAI API 密钥：** 你需要在插件代码中设置你的 OpenAI API 密钥。
-  **OpenAI API Base URL：** 你需要在插件代码中设置你的 OpenAI API Base URL。

## 依赖

-   `loguru`
-   `openai`

你可以使用以下命令安装依赖：

```bash
pip install loguru openai
```

## 许可证

本项目使用 MIT 许可证。有关更多信息，请参阅 [LICENSE](LICENSE) 文件。

## 贡献

欢迎贡献代码！请随意提交 issue 或 pull request。

## 作者

[乐正安](https://github.com/Lezhengan)

## 免责声明

本插件仅供学习和交流使用，请勿用于非法用途。使用本插件所产生的任何后果，开发者概不负责。

## 示例

```
用户：.聊天 你好吗？
AI 机器人：\\\\* 我很好，谢谢你的关心！
```

---
**提示：**
**替换占位符：** 请将 `YOUR_API_KEY` 和 `YOUR_BASE_URL` 替换为你实际的 OpenAI API 密钥和基础 URL
