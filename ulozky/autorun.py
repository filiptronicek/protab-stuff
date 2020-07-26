import os


def run():
    os.system("python dinosaurus.py")
    try:
        run()
    except Exception:
        run()
run()