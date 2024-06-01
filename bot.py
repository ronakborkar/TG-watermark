import os
import time
import json
import asyncio
from pyrogram import Client, filters
from configs import Config
from core.ffmpeg import add_watermark
from core.clean import delete_all

bot = Client("watermark_bot", bot_token=Config.BOT_TOKEN, api_id=Config.API_ID, api_hash=Config.API_HASH)

@bot.on_message(filters.command(["start", "help"]) & filters.private)
async def start_help(client, message):
    await message.reply_text("Send me a PNG/JPG/GIF to use as a watermark, followed by a video.")

@bot.on_message(filters.photo & filters.private)
async def handle_watermark_image(client, message):
    # Save watermark image
    watermark_path = f"{Config.DOWN_PATH}/{message.from_user.id}_watermark.jpg"
    await message.download(file_name=watermark_path)
    await message.reply_text("Watermark saved. Now send a video to apply this watermark.")

@bot.on_message(filters.video & filters.private)
async def handle_video(client, message):
    watermark_path = f"{Config.DOWN_PATH}/{message.from_user.id}_watermark.jpg"
    if not os.path.exists(watermark_path):
        await message.reply_text("No watermark image found. Please send a watermark image first.")
        return

    # Download video
    video_path = f"{Config.DOWN_PATH}/{message.from_user.id}_video.mp4"
    await message.download(file_name=video_path)
    
    # Add watermark
    output_path = f"{Config.DOWN_PATH}/{message.from_user.id}_output.mp4"
    await add_watermark(video_path, watermark_path, output_path)

    # Send video
    await client.send_video(message.chat.id, video=output_path, caption="Here is your watermarked video.")
    delete_all(Config.DOWN_PATH, message.from_user.id)

bot.run()
