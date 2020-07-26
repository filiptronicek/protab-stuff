def f(n: int) -> float:
    return int(n)
print(f("5")) # functions normally
try:
    print(f("bruh")) # doesn't work
except ValueError as e:
    print(f"Didn't work, error: {e}")