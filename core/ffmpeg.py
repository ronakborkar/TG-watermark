import subprocess
import asyncio

async def add_watermark(video_path, watermark_path, output_path, position=(10, 10), size=100, quality=23):
    x, y = position
    scale = f"iw*{size/100}:-1" if size != 100 else "iw"
    command = [
        "ffmpeg",
        "-i", video_path,
        "-i", watermark_path,
        "-filter_complex", f"[1]scale={scale}[wm];[0][wm]overlay={x}:{y}",
        "-c:v", "libx264",
        "-crf", str(quality),
        "-preset", "ultrafast",
        "-codec:a", "copy",
        output_path
    ]
    process = await asyncio.create_subprocess_exec(*command)
    await process.communicate()
