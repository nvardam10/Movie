import schedule
import time

def my_task():
    print("Scheduled task executed!")

# Schedule the task to run every day at 2:00 PM
schedule.every().day.at("14:00").do(my_task)

while True:
    schedule.run_pending()
    time.sleep(1)