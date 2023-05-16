# Clash Config Mixin

This project is dedicated to mixing a custom config into an existing Clash config. The Clash config is a YAML file with many fields. The existing Clash config is served on a HTTP URL. The custom config is a subset of the Clash config. The project includes an automatic config updater based on GitHub Actions, which updates the config based on the subscribed version and the user custom config automatically every day.

## Project Structure

```
├── .github
│   └── workflows
│       └── update_config.yml
├── custom
│   └── custom_config.yml
├── scripts
│   └── update_config.py
├── tests
│   └── test_update_config.py
└── server.py
```

## How to Use

1. Clone this repository.
2. Add your custom config to the `custom_config.yml` file in the `custom` directory.
3. Set the `CLASH_CONFIG_URL` secret in your repository's settings to the URL of the original Clash config.
4. The GitHub Actions workflow will run the `scripts/update_config.py` script every day at midnight, update the `merged_config.yml` file with the latest version of the original Clash config, commit the updated config file, and push the commit back to your repository.
5. Run the `server.py` script to start a Flask server that serves the merged config as a YAML file. You can do this with the following command:

```bash
python server.py
```

The server will start running on `http://localhost:5000`. You can get the merged config by sending a GET request to `http://localhost:5000/config?url=<URL>`, where `<URL>` is the URL of the original Clash config.

## Testing

You can run the tests for the `merge_configs` function with the following command:

```bash
python -m unittest tests/test_update_config.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Security

This project takes security seriously. The Clash configuration contains some important information, so it's crucial to store it properly. The original Clash config URL is stored as a secret in the repository settings, and the merged config is served dynamically by the Flask server, so it's not stored in the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
