import os
from pathlib import Path

def setup_bot():
    print("Discord Bot Setup")
    print("================")
    
    # Get the token
    token = input("\nPlease enter your Discord bot token: ").strip()
    if not token:
        print("Error: Token cannot be empty")
        return False
        
    try:
        # Create config directory if it doesn't exist
        config_dir = Path(__file__).parent / 'config'
        config_dir.mkdir(exist_ok=True)
        
        # Create .env file
        env_path = config_dir / '.env'
        with open(env_path, 'w') as f:
            f.write(f'DISCORD_TOKEN={token}')
            
        print("\n✅ Setup completed successfully!")
        print("You can now run the bot using: python src/discord_bot.py")
        return True
        
    except Exception as e:
        print(f"\n❌ Error during setup: {str(e)}")
        return False

if __name__ == "__main__":
    setup_bot()
