
# BumperAZ

BumperAZ is a Python script that scrapes car ads from the turbo.az website and sends them regularly to Telegram subscribers.

## Table of Contents

- [BumperAZ](#bumperaz)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Configuration](#configuration)
  - [Usage Examples](#usage-examples)
    - [Sending a message to Telegram](#sending-a-message-to-telegram)
    - [Scraping car ads from turbo.az](#scraping-car-ads-from-turboaz)
    - [Sending car ads to Telegram subscribers](#sending-car-ads-to-telegram-subscribers)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Installation

To install BumperAZ, you will need to have Python 3 installed on your system. You can download Python 3 from the official website: https://www.python.org/downloads/

Once you have Python 3 installed, you can install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

## Usage

To use BumperAZ, you will need to have a Telegram bot token and a chat ID. You can create a new bot and get its token by following the instructions on the Telegram website: https://core.telegram.org/bots#6-botfather

Once you have a bot token and a chat ID, you can run the script by executing the following command:

```
python main.py
```

The script will prompt you to enter a message, which will be sent to the Telegram chat. The script will then wait for a response from the chat and print it to the console.

## Configuration

You can configure BumperAZ by editing the `config.py` file. This file contains the following settings:

- `TELEGRAM_BOT_TOKEN`: The token for your Telegram bot.
- `TELEGRAM_CHAT_ID`: The ID of the chat where you want to send the messages.
- `SCRAPER_INTERVAL`: The interval (in seconds) at which the scraper should run.
- `SCRAPER_MAX_PAGES`: The maximum number of pages to scrape.

## Usage Examples

Here are some examples of how you can use BumperAZ:

### Sending a message to Telegram

To send a message to Telegram, run the following command:

```
python main.py
```

The script will prompt you to enter a message, which will be sent to the Telegram chat. The script will then wait for a response from the chat and print it to the console.

### Scraping car ads from turbo.az

To scrape car ads from turbo.az, run the following command:

```
python get_all_advertisements.py
```

The script will scrape all car ads from turbo.az and save them to a JSON file.

### Sending car ads to Telegram subscribers

To send car ads to Telegram subscribers, run the following command:

```
python broadcaster_bot.py
```

The script will read the car ads from the JSON file and send them to the Telegram chat at the specified interval.

## Contributing

If you would like to contribute to BumperAZ, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request.

## License

BumperAZ is released under the MIT License. See `LICENSE` for more information.

## Acknowledgments

BumperAZ uses the following third-party libraries:

- `beautifulsoup4`
- `python-telegram-bot`
- `requests`
