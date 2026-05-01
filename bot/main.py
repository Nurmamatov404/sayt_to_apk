import requests
from telethon import TelegramClient, events

api_id = 20464354
api_hash = "c6fa656e333fd6c9d5b9867daf028ea1"
bot_token = "SENING_BOT_TOKENING"

GITHUB_TOKEN = "GITHUB_TOKEN"
REPO = "Nurmamatov404/sayt_to_apk"

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage)
async def handler(event):
    url = event.raw_text.strip()

    if not url.startswith("http"):
        await event.reply("Link yubor ❌")
        return

    await event.reply("⏳ APK tayyorlanmoqda...")

    # GitHub Action trigger
    requests.post(
        f"https://api.github.com/repos/{REPO}/dispatches",
        headers={
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        },
        json={
            "event_type": "build_apk",
            "client_payload": {
                "url": url,
                "chat_id": event.chat_id
            }
        }
    )

client.run_until_disconnected()
