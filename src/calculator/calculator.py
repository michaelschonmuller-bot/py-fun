
# class Calculator(object):
#     _instance = None

#     def add(_self, a, b):
#         return a + b
    
#     def sub(_self, a, b):
#         return 0
    
#     def mul(_self, a, b):
#         return 0
    
#     def div(_self, a, b):
#         return 0
    
#     def factorize(_self, n):
#         return []

#     def __init__(self):
#         pass


class Calculator(object):
    _instance = None

    def to_number(self, value):
        # Si ya es un número, lo devolvemos directamente.
        if isinstance(value, (int, float)):
            return value

        # Eliminamos espacios al principio y al final.
        value = value.strip()

        # Primero intentamos convertir números como "1" o "1.600".
        try:
            return float(value)
        except ValueError:
            pass

        # Números escritos en distintos idiomas.
        numbers = {
            # English
            "zero": 0, "one": 1, "two": 2, "three": 3,
            "four": 4, "five": 5, "six": 6, "seven": 7,
            "eight": 8, "nine": 9,

            # German
            "null": 0, "eins": 1, "zwei": 2, "drei": 3,
            "vier": 4, "fünf": 5, "sechs": 6, "sieben": 7,
            "acht": 8, "neun": 9,

            # Spanish
            "cero": 0, "uno": 1, "dos": 2, "tres": 3,
            "cuatro": 4, "cinco": 5, "seis": 6,
            "siete": 7, "ocho": 8, "nueve": 9,

            # Russian
            "ноль": 0, "один": 1, "два": 2, "три": 3,
            "четыре": 4, "пять": 5, "шесть": 6,
            "семь": 7, "восемь": 8, "девять": 9,

            # Chinese
            "零": 0, "一": 1, "二": 2, "三": 3,
            "四": 4, "五": 5, "六": 6, "七": 7,
            "八": 8, "九": 9
        }

        # Buscamos la palabra en el diccionario.
        if value.lower() in numbers:
            return numbers[value.lower()]

        # Números romanos.
        roman = {
            "I": 1, "II": 2, "III": 3, "IV": 4,
            "V": 5, "VI": 6, "VII": 7,
            "VIII": 8, "IX": 9, "X": 10
        }

        if value.upper() in roman:
            return roman[value.upper()]

        raise ValueError(f"Unknown number: {value}")

    def add(self, a, b):
        return self.to_number(a) + self.to_number(b)

    def sub(self, a, b):
        return self.to_number(a) - self.to_number(b)

    def mul(self, a, b):
        return self.to_number(a) * self.to_number(b)

    def div(self, a, b):
        return self.to_number(a) / self.to_number(b)

    def factorize(self, n):
        n = self.to_number(n)

        if not float(n).is_integer() or n < 2:
            raise ValueError("Factorization requires an integer >= 2")

        n = int(n)
        factors = []
        divisor = 2

        while divisor * divisor <= n:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor

            divisor += 1

        if n > 1:
            factors.append(n)

        return factors

    def __init__(self):
        pass


    # Singleton pattern by overloading the new operator, see
    # https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons
