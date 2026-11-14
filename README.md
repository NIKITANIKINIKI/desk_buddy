# Desk Buddy

Учебный CLI-агент на [LangChain](https://docs.langchain.com/) и [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview).

Агент отвечает на вопросы, ходит в две тулзы (заметки и калькулятор) и помнит диалог внутри процесса.

```
START → assistant ── нет tool_calls ──► END
              │
              └── есть tool_calls ──► tools ──► assistant
```

## Структура

```
.
├── main.py                 # точка входа
├── requirements.txt
├── .env.example
└── desk_buddy/
    ├── config.py           # модель и переменные окружения
    ├── prompts.py          # системный промпт
    ├── cli.py              # REPL
    ├── data/               # база заметок
    ├── tools/              # lookup_notes, add
    └── graph/
        ├── state.py        # состояние графа
        ├── nodes.py        # assistant, tools, роутер
        └── builder.py      # сборка StateGraph
```

## Запуск

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

В `.env` укажите ключ API. Затем:

```bash
python main.py
```

Примеры:

```
you> Что такое langgraph?
you> 21+21
you> Меня зовут Никита
you> Как меня зовут?
```

Пустая строка завершает сессию.

## Модель

По умолчанию используется `google_genai:gemini-4-hydrogen`. Если упираетесь в квоту Free Tier, в `.env` поставьте более лёгкую модель:

```
MODEL=google_genai:gemini-2.5-flash
```

Или OpenAI:

```
OPENAI_API_KEY=sk-...
MODEL=openai:gpt-4o-mini
```
