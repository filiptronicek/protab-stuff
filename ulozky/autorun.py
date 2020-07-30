import os


def run():
    os.system("python3 ulozky/alien.py")
    try:
        run()
        print(1)
    except Exception:
        run()
run()