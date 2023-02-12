def divide(q, w):
    try:
        result = q / w
    except ZeroDivisionError:
        print("Вы что, пытаетесь делить на ноль, какой ужас!!!?")
        return
    return result


try:
    p1 = float(input("q = "))
    p2 = float(input("w = "))
    print(f"q / w = {divide(p1, p2)}")
except ValueError:
    print("Incorrect input value")
