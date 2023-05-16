import unittest
from scripts.update_config import merge_configs

class TestUpdateConfig(unittest.TestCase):
    def test_merge_configs(self):
        # Define a mock URL and a mock custom config path
        url = 'http://example.com/path/to/original/config'
        custom_config_path = '../custom/custom_config.yml'

        # Call the function
        merged_config = merge_configs(url, custom_config_path)

        # Check if the merged config is a dictionary (you might want to add more specific checks here)
        self.assertIsInstance(merged_config, dict)

if __name__ == '__main__':
    unittest.main()
