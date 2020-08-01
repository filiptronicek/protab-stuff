import os

it = 0

def run():
    os.system("python3 ulozky/alien.py")
    try:
        run()
        print("Ran run no.", it)
    except Exception:
        run()
run()