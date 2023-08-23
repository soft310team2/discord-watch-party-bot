# discord-watch-party-bot
Discord bot for organising watch-parties. A University of Auckland SOFTENG 310 Team 2 creation. You're welcome!

## What does the Discord Watch-Party Bot do?
Add this bot to your Discord server and let it help you select the best movie or TV show to watch with your friends.

Discord watch-party bot is not just great at selecting media based on you and your friends' preferences, it also keeps track of what you've already watched!

Well... At least in theory. We are still working on getting everything set up.

## Please See:
#### [Code of Conduct](CODE_OF_CONDUCT.md)
#### [License](LICENSE)
#### [Contributing](CONTRIBUTING.md)

## How to use the bot for yourself in its current state:
TBD
### 1. Fork and clone this repository to your local machine
See the [Github Cloning Guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) if unfamiliar. Or download the files manually from Github.
### 2. Install Python
Version 3.11.4 is recommended for running this bot and contributing to its development. See [Download Python](https://www.python.org/downloads/)
### 3. Set up Python Environment
Set up a Python environment for the code editor of your choice. It is recommended to use a virtual Python environment to avoid installing packages globally. For help with this simply google the name of your preferred IDE and "virtual python environment".
### 4. Install Dependencies
In the root folder of the project - the one with your .venv folder in it - use the terminal to install nextcord using `pip install nextcord`, and install dotenv using `pip install dotenv`. You can check your .venv folder's Lib folder to see that these dependencies have been installed successfully in your virtual environment.
### 5. Start using the bot or make your own
#### Use The Existing Bot (not currently recommended):
Use the existing Bot: You can invite the existing bot to your Discord server via this link: [Invite Popcorn Bot](https://discord.com/api/oauth2/authorize?client_id=1138633131432366194&permissions=18685255740480&scope=bot%20applications.commands). The bot will need to be invited by a member of the server with admin priviledges. NOTE: The bot currently has access to message content for debugging purposes.

Using this method, you will only be able to use the bot when it is being run for testing at this stage of development, and not all features may work correctly. To use the bot anytime with complete freedom you can create your own personal version through the discord developer portal outlined in Option B below.
#### Create Your Own Bot:
Create your own bot from the [Discord Developer's Portal](https://discord.com/developers/docs/intro). Follow this [Creating a Discord Bot Guide](https://www.ionos.com/digitalguide/server/know-how/creating-discord-bot/).

Give the bot the following Scopes:
![bot scopes](https://github.com/mattysteves/discord-watch-party-bot/assets/39393161/1d23b1c5-4095-44a7-9877-ccd746bed773)

And the following Permissions:
![bot permissions](https://github.com/mattysteves/discord-watch-party-bot/assets/39393161/b84481a3-8be4-4d19-a8ed-2e79128e3352)

Then copy the generated URL, paste it into your browser, and you will be prompted to add the bot to one of your servers. Once the bot is invited, it will not be able to perform any functions until bot.py is configured for your bot's token and your server's guild ID. bot.py will also need to be running with an internet connection for any commands to work.

#### Adding Your Bot Token and Guild ID to the project:
Create a file called .env in the root project folder (same level as bot.py):

![env](https://github.com/mattysteves/discord-watch-party-bot/assets/39393161/e5ea59ca-0fbd-46e3-9bbe-d273094fff6d)

In that file, copy your bot token from the Discord Developer Application page:

![botTOKEN](https://github.com/mattysteves/discord-watch-party-bot/assets/39393161/17c563bc-bf83-45fe-87a4-106d4aafff3e)

The bot token goes here:

![envfileBOT](https://github.com/mattysteves/discord-watch-party-bot/assets/39393161/7725b15e-7f60-4caa-94cf-98b8b22e5407)

The Guild ID for a server can be found by right-clicking the server's name in the top left, and selecting the "Copy Guild ID" option form the dropdown:

![guildTOKEN](https://github.com/mattysteves/discord-watch-party-bot/assets/39393161/6cfcec40-c7be-4363-9614-10b9ad4f3481)

The Guild ID goes here:

![envfileGUILD](https://github.com/mattysteves/discord-watch-party-bot/assets/39393161/7301a59e-144a-46b0-8e05-2dbdbe50833a)

#### IMPORTANT
Do not share your bot token with anyone!

## How to help improve the bot
1. Fork, clone, and install the bot by following the guide above.
## License and usage
TBD
