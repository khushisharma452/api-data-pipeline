import schedule
import time
from pipeline import run_pipeline

# Run every 1 minute (for demo)
schedule.every(1).minutes.do(run_pipeline)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)