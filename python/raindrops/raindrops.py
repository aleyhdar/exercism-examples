def convert(number):

    _sound: str = ""

    _sound += "" if number%3 else "Pling"
    _sound += "" if number%5 else "Plang"
    _sound += "" if number%7 else "Plong"

    return _sound if _sound else str(number)


