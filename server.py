from flask import Flask, request, Response
from scripts.update_config import merge_configs
import yaml

app = Flask(__name__)


@app.route('/config', methods=['GET'])
def serve_config():
    # Get the URL of the original Clash config from the query parameters
    url = request.args.get('url')

    # Merge the configs
    merged_config = merge_configs(url, 'custom/custom_config.yml')

    # Convert the merged config to YAML format
    merged_config_yaml = yaml.safe_dump(merged_config, allow_unicode=True)

    # Return the merged config as a YAML file
    return Response(merged_config_yaml, mimetype='text/yaml')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
