import subprocess

async def add_watermark(video_path, watermark_path, output_path):
    command = [
        "ffmpeg",
        "-i", video_path,
        "-i", watermark_path,
        "-filter_complex", "overlay=10:10",
        "-codec:a", "copy",
        output_path
    ]
    process = await asyncio.create_subprocess_exec(*command)
    await process.communicate()
