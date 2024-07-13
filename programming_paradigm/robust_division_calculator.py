def safe_divide(numerator, denominator):
    try:
        safe_divide(numerator, denominator)
    except ZeroDivisionError as e:
        print(e)

    try:
        numerator, denominator= float(numerator), float(denominator)
    except TypeError as e:
        print(e)


