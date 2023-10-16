import os
import unittest
from app.main import create_directory_structure_from_json
import shutil


class TestCreateDirectoryStructureFromJson(unittest.TestCase):

    def test_create_directory_structure(self):
        data = [
            {
                "name": "folder1",
                "type": "folder",
                "values": [
                    {
                        "name": "subfolder1",
                        "type": "folder",
                        "values": [
                            {
                                "name": "file1.txt",
                                "type": "file",
                                "values": "This is file 1"
                            },
                            "file2.txt"
                        ]
                    },
                    "subfolder2"
                ]
            },
            "folder2"
        ]

        create_directory_structure_from_json(data)

        # Check if directory structure is created correctly
        self.assertTrue(os.path.exists("folder1"))
        self.assertTrue(os.path.exists("folder1/subfolder1"))
        self.assertTrue(os.path.exists("folder1/subfolder1/file1.txt"))
        self.assertTrue(os.path.exists("folder1/subfolder1/file2.txt"))
        self.assertTrue(os.path.exists("folder1/subfolder2"))
        self.assertTrue(os.path.exists("folder2"))

        # Check if file contents are correct
        with open("folder1/subfolder1/file1.txt", "r") as f:
            content = f.read()
            self.assertEqual(content, "This is file 1")
        if os.path.exists("folder1/"):
            unittest.addModuleCleanup(shutil.rmtree, "./folder1")
            unittest.addModuleCleanup(shutil.rmtree, "./folder2")


if __name__ == "__main__":
    unittest.main()
