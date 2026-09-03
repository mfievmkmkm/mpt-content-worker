# Content OS Shorts Worker

Тонкая Railway-обёртка над MoneyPrinterTurbo. Получает производственное задание от Content OS,
подбирает бесплатные вертикальные кадры Pexels, озвучивает через Edge TTS, рисует субтитры и
возвращает готовый MP4 прямо в Telegram-бота.

## Railway variables

- `PEXELS_API_KEY` — ключ Pexels
- `MPT_API_KEY` — общий секрет с основным ботом
- `PORT=8080`

После деплоя добавьте в основной сервис:

```env
MPT_BASE_URL=https://your-worker.up.railway.app
MPT_API_KEY=тот-же-секрет
MPT_VOICE_NAME=ru-RU-DmitryNeural
MPT_TIMEOUT_MINUTES=20
```

Проверьте `GET /docs`, затем кнопка **🎬 Shorts** будет присылать MP4 вместо JSON.
