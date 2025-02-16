# Discord Bot Automation

A Python bot for automated management of Discord server structures.

## Installation

1. Create a virtual environment:
```bash
cd Discord-Bot-Automation
python3 -m venv venv
source venv/bin/activate
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Setup

1. Create a Discord Bot:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application"
   - Go to the "Bot" section
   - Enable all "Privileged Gateway Intents"
   - Copy the bot token

2. Configure the bot:
```bash
python src/setup.py
```
Enter your bot token when prompted.

3. Invite the bot to your server:
   - In the Developer Portal, go to "OAuth2" -> "URL Generator"
   - Select scopes: "bot" and "applications.commands"
   - For Bot Permissions, select "Administrator"
   - Open the generated URL in your browser
   - Select your server

## Usage

1. Start the bot:
```bash
python src/discord_bot.py
```

2. Follow the prompts:
   - Enter the desired server name
   - Confirm the changes

The bot will:
- Update the server name
- Delete all existing channels
- Create new categories and channels based on the template file

## Customizing Server Structure

The server structure is defined in `src/templates/server_template.json`. You can edit this file to customize the categories and channels.

## Project Structure

```
Discord-Bot-Automation/
├── README.md
├── requirements.txt
├── src/
│   ├── config/
│   │   └── .env
│   ├── templates/
│   │   └── server_template.json
│   ├── discord_bot.py
│   └── setup.py
└── venv/
```

## Security Notes

- Never share your bot token
- The bot token is securely stored in the .env file
- Ensure the bot has Administrator rights
- Be aware of Discord's limit of 10 server creations per day

## Features

- Automated server structure creation
- Customizable categories and channels
- Support for both text and voice channels
- Emoji support in channel names
- Clean and organized project structure
- Secure configuration handling

## Requirements

- Python 3.11 or higher
- discord.py library
- python-dotenv for configuration
- Internet connection
- Discord account with server management permissions

## Contributing

Feel free to fork this repository and submit pull requests for any improvements you'd like to add.

## License

This project is open source and available under the MIT License.
