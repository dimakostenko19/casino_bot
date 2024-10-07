# CasinoBot

CasinoBot - это Telegram-бот, построенный с использованием библиотеки Aiogram. Этот бот представляет прогнозы на такие игры как Aviator и Mines.

## Функциональность
- **Прогнозы игры Aviator✈️**
- **Прогнозы игры Mines🕹**


## Установка

1. **Клонируйте репозиторий**:
    ```bash
    git clone https://github.com/dimakostenko19/casino_bot.git
    cd casion_bot
    ```

2. **Установите зависимости**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Запустите бота**:
    ```bash
    python bot.py
    ```

## Структура проекта

```plaintext
.
├── casino_bot/
│   ├── handlers/
│   │   ├── user_handlers.py
│   ├── keyboards/
│   │   ├── keyboard.py
│   ├── bot.py
|   |── mines_signals
|   |── photo
├── requirements.txt
├── README.md
