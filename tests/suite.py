import unittest

# Import your test files
from tests.test__create_directory_structure import TestCreateDirectoryStructureFromJson
from tests.test__create_dist_folder import CreateDistFolderTestCase
from tests.test__get_available_templates import TestGetAvailableTemplates
from tests.test__get_args import get_args


def create_test_suite():
    suite = unittest.TestSuite()

    # Add test cases from different test modules
    suite.addTest(unittest.makeSuite(TestCreateDirectoryStructureFromJson))
    suite.addTest(unittest.makeSuite(TestGetAvailableTemplates))
    suite.addTest(unittest.makeSuite(CreateDistFolderTestCase))
    suite.addTest(unittest.makeSuite(get_args))

    return suite


if __name__ == '__main__':
    test_suite = create_test_suite()
    runner = unittest.TextTestRunner()
    result = runner.run(test_suite)
