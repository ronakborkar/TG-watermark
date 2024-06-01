import os
import shutil

def delete_all(path, user_id):
    watermark_path = f"{path}/{user_id}_watermark.jpg"
    video_path = f"{path}/{user_id}_video.mp4"
    output_path = f"{path}/{user_id}_output.mp4"
    if os.path.exists(watermark_path):
        os.remove(watermark_path)
    if os.path.exists(video_path):
        os.remove(video_path)
    if os.path.exists(output_path):
        os.remove(output_path)
    shutil.rmtree(f"{path}/{user_id}", ignore_errors=True)
