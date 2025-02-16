import discord
import json
import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv

class DiscordServerManager:
    def __init__(self):
        # Load environment variables
        load_dotenv(Path(__file__).parent / 'config' / '.env')
        self.token = os.getenv('DISCORD_TOKEN')
        
        if not self.token:
            raise ValueError("Discord token not found. Please set up your .env file.")

        # Set up intents
        intents = discord.Intents.default()
        intents.guilds = True
        self.client = discord.Client(intents=intents)

        # Load server template
        template_path = Path(__file__).parent / 'templates' / 'server_template.json'
        with open(template_path, 'r', encoding='utf-8') as f:
            self.template = json.load(f)

    async def modify_server(self, server_name):
        """Modify the server according to the template."""
        @self.client.event
        async def on_ready():
            try:
                # Get the first guild the bot is in
                guild = self.client.guilds[0]
                print(f"Modifying server '{guild.name}'...")

                # Update server name
                await guild.edit(name=server_name)
                print(f"Updated server name to '{server_name}'")

                # Delete all existing channels
                print("Deleting existing channels...")
                for channel in guild.channels:
                    await channel.delete()
                    await asyncio.sleep(0.5)

                # Create new structure
                print("Creating categories and channels...")
                for cat in self.template['categories']:
                    category = await guild.create_category(name=cat['name'])
                    print(f"Created category: {cat['name']}")
                    await asyncio.sleep(0.5)

                    for ch in cat['channels']:
                        if ch['type'] == 'text':
                            await guild.create_text_channel(name=ch['name'], category=category)
                        else:
                            await guild.create_voice_channel(name=ch['name'], category=category)
                        print(f"Created channel: {ch['name']}")
                        await asyncio.sleep(0.5)

                print(f"\n✅ Server '{server_name}' updated successfully!")
                print(f"Guild ID: {guild.id}")

            except Exception as e:
                print(f"\n❌ Error during server modification: {str(e)}")
            finally:
                await self.client.close()

        # Start the bot
        try:
            print("Connecting to Discord...")
            await self.client.start(self.token)
        except discord.LoginFailure:
            print("\n❌ Error: Invalid Discord token. Please check your .env file.")
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
        finally:
            if not self.client.is_closed():
                await self.client.close()

def main():
    print("Discord Server Manager")
    print("=====================")

    try:
        # Initialize the server manager
        manager = DiscordServerManager()

        # Get server name
        server_name = input("\nEnter the new name for your server: ")
        if not server_name.strip():
            print("Error: Server name cannot be empty.")
            return

        print("\nWarning: This will delete all existing channels and create new ones!")
        confirm = input("Are you sure you want to continue? (y/N): ")
        if confirm.lower() != 'y':
            print("Operation cancelled.")
            return

        # Modify server
        asyncio.run(manager.modify_server(server_name))

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()
