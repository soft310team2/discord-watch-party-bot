# Discord watch party bot - 🍿 Popcorn 🍿
This is a Discord bot for organising watch-parties, named Popcorn. A University of Auckland SOFTENG 310 Team 2 creation. You're welcome!

## What does Popcorn do?
Add this bot to your Discord server and let it help you select the best movie or TV show to watch with your friends.

Popcorn is not just great at selecting media based on you and your friends' preferences, it also keeps track of what you've already watched!

Well... At least in theory. So far, only release 1 has been implemented.

| Release | Description |
| --- | --- |
| **Release 1** | Bot that can be run by an individual from their machine with a local memory that can be accessed by all server members. Basic adding, deleteing, viewing, notifications, and permissions functionality is implemented. Basic user experience to use bot for watchlists in servers fullly implemented. |
| **Release 2** | We will work on adding tags and statuses to individual media for better filtering. More thorough user experience will be implemented, with more specific commands. |
| **Release 3** | We will add API connectiosn to get third party searching and media information to show real world info about media items. Voting implementation will be implemented, possibly with discord event set up as well. |

## Please See:
#### [Code of Conduct](CODE_OF_CONDUCT.md)
#### [License](LICENSE)
#### [Contributing](CONTRIBUTING.md)

## How to use the bot for yourself in its current state:

### 1. Fork and clone this repository to your local machine
See the [Github Cloning Guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) if unfamiliar. Or download the files manually from Github.
### 2. Install Python
Version 3.11.4 is recommended for running this bot and contributing to its development. See [Download Python](https://www.python.org/downloads/)
### 3. Set up Python Environment
Set up a Python environment for the code editor of your choice. It is recommended to use a virtual Python environment to avoid installing packages globally. For help with this simply google the name of your preferred IDE and "virtual python environment".
### 4. Install Dependencies
In the root folder of the project - the one with your .venv folder in it - use the terminal to install nextcord using `pip install nextcord`, and install dotenv using `pip install python-dotenv`. You can check your .venv folder's Lib folder to see that these dependencies have been installed successfully in your virtual environment.
### 5. Start using the bot or make your own
#### Use The Existing Bot (not currently recommended):
Use the existing Bot: You can invite the existing bot to your Discord server via this link: [Invite Popcorn Bot](https://discord.com/api/oauth2/authorize?client_id=1138633131432366194&permissions=18685255740480&scope=bot%20applications.commands). The bot will need to be invited by a member of the server with admin priviledges. NOTE: The bot currently has access to message content for debugging purposes.

Using this method, you will only be able to use the bot when it is being run for testing at this stage of development, and not all features may work correctly. To use the bot anytime with complete freedom you can create your own personal version through the discord developer portal outlined below.
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

You **must** turn on Developer Mode to see this (Settings > Advanced > Developer Mode)

The Guild ID goes here:

![envfileGUILD](https://github.com/mattysteves/discord-watch-party-bot/assets/39393161/7301a59e-144a-46b0-8e05-2dbdbe50833a)

#### Run bot.py
If everything is configured properly, run bot.py and you should see your bot go online in your server (where you obtained the guild ID).
Use the '/' prefix to issue bot commands in your server's text channels:
![image](https://github.com/soft310team2/discord-watch-party-bot/assets/100410646/02d1203e-a723-4a80-87a8-02f46c261b77)
If you type "/popcorn", you can see a popup list of all of the commands. You can also use the /help command.
![image](https://github.com/soft310team2/discord-watch-party-bot/assets/100410646/e9fa32f7-edf8-4aeb-9432-3db4ac249bee)

Your bot is now working, hooray!

#### IMPORTANT
Do not share your bot token with anyone! Make sure to include the local .env file in your .gitignore, so that your bot token is never uploaded to the repository! If you accidentally leak your bot's token, you will have to regenerate the token from the discord developers portal.

## How to help improve the bot
1. Fork, clone, and install the bot by following the [Contributing](CONTRIBUTING.md) guidelines.

## License and usage
[License](LICENSE)

## Contacts
For additional information about the bot, contact email: jwei578@aucklanduni.ac.nz
