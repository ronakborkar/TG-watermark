import unittest
import os
from core.ffmpeg import add_watermark
from pyrogram import Client

class TestFFmpegWatermark(unittest.TestCase):
    
    def setUp(self):
        self.video_path = "test_video.mp4"
        self.watermark_path = "test_watermark.png"
        self.output_path = "test_output.mp4"
        
        # Create dummy video and watermark files
        with open(self.video_path, "w") as f:
            f.write("dummy video content")
        with open(self.watermark_path, "w") as f:
            f.write("dummy watermark content")

    def test_add_watermark(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(add_watermark(self.video_path, self.watermark_path, self.output_path))
        self.assertTrue(os.path.exists(self.output_path))
        
    def tearDown(self):
        os.remove(self.video_path)
        os.remove(self.watermark_path)
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

if __name__ == '__main__':
    unittest.main()
