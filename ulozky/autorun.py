import os


def run():
    os.system("python mimo.py")
    try:
        run()
    except Exception:
        run()
run()