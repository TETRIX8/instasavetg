Вот пример MD файла с объяснением и инструкцией по добавлению токена и запуску бота:

```markdown
# Telegram Bot для скачивания видео с Instagram

Этот бот позволяет пользователям отправлять ссылки на видео с Instagram, а бот будет скачивать и отправлять видео обратно.

## Функциональность

- Бот обрабатывает ссылки на видео с Instagram.
- После получения ссылки, бот скачивает видео и отправляет его обратно пользователю.
- Добавлены ограничения, чтобы пользователь не мог отправлять несколько ссылок одновременно. Необходимо дождаться завершения загрузки видео перед отправкой новой ссылки.

## Установка и запуск

### Требования

1. Python 3.7 или выше.
2. Установленные библиотеки:
   - `aiogram`
   - `requests`
   - `snapsave_downloader`

Для установки зависимостей, выполните команду:

```bash
pip install aiogram requests 
```

### Создание и настройка Telegram бота

1. Перейдите в [BotFather](https://core.telegram.org/bots#botfather) в Telegram.
2. Создайте нового бота с помощью команды `/newbot`.
3. Получите токен вашего бота.

### Добавление токена

1. Откройте файл `bot.py`.
2. Найдите строку:

```python
API_TOKEN = 'YOUR_BOT_TOKEN'  # Замените на ваш токен
```

3. Замените `YOUR_BOT_TOKEN` на ваш токен, который вы получили от BotFather.

### Запуск бота

После того, как вы добавите токен, вы можете запустить бота с помощью команды:

```bash
python bot.py
```

Бот начнет работать и будет слушать сообщения.

### Использование

1. Отправьте боту ссылку на видео с Instagram.
2. Бот начнет обрабатывать ссылку, скачает видео и отправит его обратно.
3. Пока видео загружается, пользователь не сможет отправить новую ссылку, пока предыдущая загрузка не завершится.

## Примечания

- Этот бот работает только с видео с Instagram.
- При возникновении проблем, таких как ошибки при скачивании видео или недоступность ссылок, бот отобразит соответствующие сообщения.
- Бот использует сервис SnapSave для получения ссылок на скачивание видео.

## Лицензия

Этот проект использует [MIT License](LICENSE).
```

В этом файле объясняется, как настроить токен, установить зависимости, запустить бота и использовать его. Он также содержит информацию о том, что бот поддерживает скачивание видео только с Facebook и как избежать спама с помощью ограничения на отправку ссылок.