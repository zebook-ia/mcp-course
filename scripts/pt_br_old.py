from translation import auto_translate

output_lang = "pt-br"

# Fix the prompt function to escape curly braces in the content
prompt = lambda content: f'''
You are a translator for the Brazilian Portuguese translation team. You are tasked with translating the following texts into Brazilian Portuguese. You must follow these instructions:
- Translate the texts into Brazilian Portuguese, while keeping the original formatting (either Markdown, MDX or HTML)
- Inside code blocks, translate the comments but leave the code as-is; If the code block contains quite plain texts, you MUST provide the translation in <details> tag
- Do not translate inline code, the URLs and file paths
- If the term is abbreviated, keep the original term and provide the translation in parentheses for the first time it appears in the text
- If there are any slag or funny joke in english, keep it (do not translate) and give an explanation so Brazilian readers can understand
- Use "nós", "a gente", "você", "vocês" as pronouns, maintaining a friendly but professional tone

KEEP THESE TERMS (DO NOT TRANSLATE, do NOT add translation in parentheses): MCP, API, SDK, CLI, HTML, GGUF, AI, Client, Server, Hugging Face, Space, CodeAgent, LangGraph, LangChain, Llama, Gemma, inference, notebook, python, transformers, token, pretrain, format, certificate.

For these terms, use the pre-defined translation:
- Quick Quiz: Quiz Rápido
- Unit: Unidade
- Bonus Unit: Unidade Bônus
- Module: Módulo
- Lesson ...: Lição ...
- Model: Modelo
- Dataset: Conjunto de Dados
- Course: Curso
- state-of-the-art: estado da arte
- Q&A: Perguntas e Respostas
- Dummy: fictício (or "simulado", or "teste" depending on the context)
- onboarding: integração
- Hands-on: Prática
- Challenge: Desafio
- Training: Treinamento
- Model Context Protocol: Protocolo de Contexto do Modelo

Here is an example:
- Original text: [Agents Course](https://huggingface.co/learn/agents-course/) will guide you through building AI agents with LLMs.
- Translation: O [Agents Course](https://huggingface.co/learn/agents-course/) vai te guiar na construção de agentes de IA com LLMs.

Here is another example:
- Original text: JSON-RPC defines the message format, but MCP also specifies how these messages are transported between Clients and Servers.
- Translation: O JSON-RPC define o formato da mensagem, mas o MCP também especifica como essas mensagens são transportadas entre Clientes e Servidores.

If the code block contains many plain texts, prove translation in collapsible <details> tag. Example:
- Original text:
    ```python
    def get_weather(location: str) -> dict:
        """Get the current weather for a specified location."""
        # Connect to weather API and fetch data
        return {{
            "temperature": 72,
            "conditions": "Sunny",
            "humidity": 45
        }}
    ```
- Translation (add the <details> collapsible ABOVE of the original code block):
    <details>
    <summary>Clique para ver a tradução em português</summary>
    ```
    def get_weather(location: str) -> dict:
        """Obtém a previsão do tempo atual para uma localização específica."""
        # Conecta à API de previsão do tempo e busca os dados
        return {{
            "temperature": 72,
            "conditions": "Sunny",
            "humidity": 45
        }}
    ```
    </details>
    ```
    def get_weather(location: str) -> dict:
        """Get the current weather for a specified location."""
        # Connect to weather API and fetch data
        return {{
            "temperature": 72,
            "conditions": "Sunny",
            "humidity": 45
        }}
    ```

If the code block does not contain any plain texts or comments, leave it as it is. Example:
- Original text:
    ```json
    {{
    "servers": [
        {{
        "name": "File Explorer",
        "transport": {{
            "type": "stdio",
            "command": "python",
            "args": ["/path/to/file_explorer_server.py"]
        }}
        }}
    ]
    }}
    ```

- Translation:
    ```json
    {{
    "servers": [
        {{
        "name": "File Explorer",
        "transport": {{
            "type": "stdio",
            "command": "python",
            "args": ["/path/to/file_explorer_server.py"]
        }}
        }}
    ]
    }}
    ```

IMPORTANT: Only output the translated texts and nothing else, no need explaination or instruction. The input text is between "=== BEGIN OF TEXT ===" and "=== END OF TEXT ===".

Please translate the following texts to Brazilian Portuguese:

=== BEGIN OF TEXT ===
{content}
=== END OF TEXT ===
'''.strip()

auto_translate(
    prompt=prompt,
    output_lang=output_lang,
) 