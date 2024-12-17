import threading
import time


def set_reminder(details):
    reminder_time = int(details.get('time', 10))  # Default to 10 seconds
    message = details.get('message', 'Reminder!')

    def remind():
        time.sleep(reminder_time)
        print(f"Reminder: {message}")

    threading.Thread(target=remind).start()
    return {"status": "success", "message": f"Reminder set for {reminder_time} seconds"}
