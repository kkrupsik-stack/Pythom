def square(x, y):

    numbers_row = "| " + " | ".join(str(i) for i in range(1, x + 1)) + " |"

    underline_top = "  " + "  _  ".join([""] * x) + "  "

    underline_bottom = "  " + "  ^  ".join([""] * x) + "  "

    result = ""
    for i in range(y):
        result += underline_top + "\n"
        result += numbers_row + "\n"
        result += underline_bottom + "\n"
    
    print(result)

square(2, 3)
