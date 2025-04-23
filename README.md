
# Nepovtorimo Telegram Bot Store

Telegram-бот для демонстрации и продажи одежды через категории:
- Jacket/Skirt
- Suit
- Dress

## Запуск локально

1. Установите зависимости:

```bash
pip install -r requirements.txt
```

2. Замените `YOUR_TOKEN` в `bot.py` на ваш Telegram Bot Token.

3. Запустите бота:

```bash
python bot.py
```

## Развёртывание на Render

1. Создайте Web Service с:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python bot.py`
2. Укажите переменную среды `YOUR_TOKEN` со значением вашего токена.

---

Проект создан как MVP для демонстрации Telegram-магазина с интеграцией оплаты (будет добавлено позже).
