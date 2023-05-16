import requests
from deepmerge import always_merger
import yaml
import sys

def merge_configs(url, custom_config_path):
    # Fetch the original Clash config
    response = requests.get(url)
    original_config = yaml.safe_load(response.text)

    # Load the custom config
    with open(custom_config_path, 'r') as f:
        custom_config = yaml.safe_load(f)
        custom_config = {} if custom_config is None else custom_config

    # Merge the configs
    merged_config = always_merger.merge(original_config, custom_config)

    return merged_config

if __name__ == '__main__':
    # Get the URL of the original Clash config from the command-line arguments
    url = sys.argv[1]

    # Merge the configs
    merged_config = merge_configs(url, '../custom/custom_config.yml')

    # Write the merged config to a file
    with open('merged_config.yml', 'w') as f:
        yaml.safe_dump(merged_config, f)
