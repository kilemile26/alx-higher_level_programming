def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
        except:
            pass
        else:
            result += (a ** b) / i
    result += a + b
    return result
