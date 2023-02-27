import time
import threading
from win10toast import ToastNotifier
from playsound import playsound

notification = ToastNotifier()


def notification_function():
    while True:
        notification.show_toast(
            title="Drink Water Notifier",
            msg="We should drink about 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            icon_path="C:/Users/Karmakar's PC/Documents/Arpan Karmakar/Python Programming/projects/drink_water_notifier/water.ico",
            duration=10,
        )
        time.sleep(1800)


def playsound_function():
    playsound(
        "C:/Users/Karmakar's PC/Documents/Arpan Karmakar/Python Programming/projects/drink_water_notifier/water.wav"
    )


# ChatGPT assisted code:

notification_thread = threading.Thread(target=notification_function)
playsound_thread = threading.Thread(target=playsound_function)

# Start both threads
notification_thread.start()
playsound_thread.start()

# Wait for both threads to finish
notification_thread.join()
playsound_thread.join()
