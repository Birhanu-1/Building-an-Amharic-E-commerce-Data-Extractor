
import os
import csv
import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto
import nest_asyncio

# Allow nested asyncio loops (needed for Jupyter/IPython)
nest_asyncio.apply()

# Load environment variables
load_dotenv('../.env')
api_id = int(os.getenv('TG_API_ID'))
api_hash = os.getenv('TG_API_HASH')

client = TelegramClient('scraping_session', api_id, api_hash)

async def scrape_channel(client, channel_username, writer, media_dir):
    entity = await client.get_entity(channel_username)
    channel_title = entity.title

    async for message in client.iter_messages(entity, limit=10000):
        media_path = None
        if message.media and isinstance(message.media, MessageMediaPhoto):
            filename = f"{channel_username}_{message.id}.jpg"
            media_path = os.path.join(media_dir, filename)
            await client.download_media(message.media, media_path)

        message_text = message.message or ''
        message_date = message.date.strftime('%Y-%m-%d %H:%M:%S') if message.date else ''

        writer.writerow([channel_title, channel_username, message.id, message_text, message_date, media_path])

async def main():
    await client.start()

    media_dir = '../data1/photos'
    os.makedirs(media_dir, exist_ok=True)

    with open('../data1/telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])

        channels = ['@MerttEka','@aradabrand2','@belaclassic','@marakisat2', '@kuruwear']
        success_count = 0
        for channel in channels:
            try:
                print(f"Scraping {channel} ...")
                await scrape_channel(client, channel, writer, media_dir)
                success_count += 1
                print(f"Done: {channel}")
            except Exception as e:
                print(f"Failed: {channel} — {e}")
        print(f"\n🔎 Total channels scraped: {success_count}/{len(channels)}")


async def run():
    async with client:
        await main()

# Run the scraper inside the running event loop (Jupyter friendly)
await run()