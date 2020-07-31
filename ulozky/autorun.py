import os

it = 0

def run():
    os.system("python3 ulozky/mimo.py")
    try:
        run()
        print("Ran run no.", it)
    except Exception:
        run()
run()