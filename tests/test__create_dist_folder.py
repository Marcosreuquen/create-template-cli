import os
import shutil
import unittest
from app.main import create_dist_folder


class CreateDistFolderTestCase(unittest.TestCase):

    def setUp(self):
        self.dist_folder = "./dist"

    def tearDown(self):
        if os.path.exists(self.dist_folder):
            shutil.rmtree(self.dist_folder)

    def test_create_dist_folder(self):
        # Test that the dist folder is created when it doesn't exist
        create_dist_folder(self.dist_folder)
        self.assertTrue(os.path.exists(self.dist_folder))

    def test_create_dist_folder_existing(self):
        # Test that the dist folder is deleted and recreated when it already exists
        os.makedirs(self.dist_folder, exist_ok=True)
        create_dist_folder(self.dist_folder)
        self.assertTrue(os.path.exists(self.dist_folder))


if __name__ == '__main__':
    unittest.main()
