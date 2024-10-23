import os
import subprocess
import threading

BOTS_DIR = "/home/orangepi/bots"  # Adjust this path to where your bots folder is located

def run_bot(bot_path):
    """
    Function to run a bot file using subprocess
    """
    try:
        print(f"Running bot: {bot_path}")
        subprocess.run(['python3', bot_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {bot_path}: {e}")

def scan_and_run_bots():
    """
    Function to scan the bots folder and run each bot.py file
    """
    for root, dirs, files in os.walk(BOTS_DIR):
        for file in files:
            if file == "bot.py":
                bot_path = os.path.join(root, file)
                bot_thread = threading.Thread(target=run_bot, args=(bot_path,))
                bot_thread.start()

if __name__ == "__main__":
    scan_and_run_bots()