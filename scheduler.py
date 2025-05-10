import schedule
import subprocess
import time
from datetime import datetime

def run_main1():
    now = datetime.now().time()
    if now.hour >= 8 and now.hour < 24:  # From 08:00 to 23:59
        print(f"Running main1 at {now}")
        subprocess.Popen(["python", r"D:/Paleden_Project/main.py"])

def run_main2():
    print("Running main2 at 03:00 AM")
    subprocess.Popen(["python", r"D:/Paleden_Project/Project1/scraper.py"])

# Schedule main1 to check every minute but only run if time is between 8AM–12AM
schedule.every(1).minutes.do(run_main1)

# Schedule main2 to run once daily at 3:00 AM
schedule.every().day.at("03:00").do(run_main2)

print(" Scheduler started... Press Ctrl+C to stop.")


while True:
    schedule.run_pending()
    time.sleep(60)
