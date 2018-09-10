
from configs import DEVICES
from threading import Thread


def do_something(arg1, arg2):
    print(str(arg1) + '\n' + str(arg2))


if __name__ == '__main__':
    for key, value in DEVICES.items():

        thread = Thread(target=do_something, args=(key, value))
        thread.daemon = True
        thread.start()
