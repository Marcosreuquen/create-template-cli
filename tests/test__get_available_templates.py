import unittest
import os
import json
from app.main import get_available_templates
import shutil


def check_and_remove_existing_folder(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)


class TestGetAvailableTemplates(unittest.TestCase):

    def test_no_templates_available(self):
        folder_name = "./templates-test-empty"
        check_and_remove_existing_folder(folder_name)
        os.mkdir(folder_name)
        # Testing when no templates are available in the templates directory
        # The function should return an empty list
        expected_result = []

        result = get_available_templates(folder_name)
        self.assertEqual(result, expected_result)
        check_and_remove_existing_folder(folder_name)

    def test_templates_available(self):
        folder_name = "./templates-test-full"
        check_and_remove_existing_folder(folder_name)

        def create_json(folder_name, expected_result):
            for name in expected_result:
                file_path = os.path.join(folder_name, "{}.json".format(name))
                open(file_path, "w").close()
                json_string = json.dumps({}, indent=4)
                with open(file_path, 'w') as json_file:
                    json_file.write(json_string)

        expected_result = ["template1", "template2", "template3"]

        os.mkdir(folder_name)
        create_json(folder_name, expected_result)

        result = get_available_templates(folder_name)

        self.assertEqual(len(result), len(expected_result))
        check_and_remove_existing_folder(folder_name)


if __name__ == "__main__":
    unittest.main()
