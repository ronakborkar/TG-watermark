import unittest
import os
from core.clean import delete_all

class TestClean(unittest.TestCase):
    
    def setUp(self):
        self.path = "downloads"
        self.user_id = 12345
        os.makedirs(self.path, exist_ok=True)
        
        self.watermark_path = f"{self.path}/{self.user_id}_watermark.jpg"
        self.video_path = f"{self.path}/{self.user_id}_video.mp4"
        self.output_path = f"{self.path}/{self.user_id}_output.mp4"
        
        with open(self.watermark_path, "w") as f:
            f.write("dummy watermark content")
        with open(self.video_path, "w") as f:
            f.write("dummy video content")
        with open(self.output_path, "w") as f:
            f.write("dummy output content")

    def test_delete_all(self):
        delete_all(self.path, self.user_id)
        self.assertFalse(os.path.exists(self.watermark_path))
        self.assertFalse(os.path.exists(self.video_path))
        self.assertFalse(os.path.exists(self.output_path))
        
    def tearDown(self):
        if os.path.exists(self.path):
            os.rmdir(self.path)

if __name__ == '__main__':
    unittest.main()
