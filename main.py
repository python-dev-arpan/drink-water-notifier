import time
from threading import Thread
from win10toast import ToastNotifier
from playsound import playsound

notification = ToastNotifier()


def playsound_fx():
    playsound(
        "C:/Users/Karmakar's PC/Documents/Arpan Karmakar/Python Programming/projects/drink_water_notifier/water.wav"
    )


while True:
    Thread(target=playsound_fx).start()
    notification.show_toast(
        title="Drink Water Notifier",
        msg="We should drink about 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
        icon_path="C:/Users/Karmakar's PC/Documents/Arpan Karmakar/Python Programming/projects/drink_water_notifier/water.ico",
        duration=10,
    )
    time.sleep(1800)
