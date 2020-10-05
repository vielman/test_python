"""
>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120

>>> recursivo.factorial(13)
6227020800
"""



def fibonacci(number):
    if number == 0: return 0
    elif number == 1: return 1
    else: return fibonacci(number -1) + fibonacci(number - 2)


# implementacion del DocString dentro de la funcion
def palindromo(sentence):
    """Retorna verdadero si el parametro es un palindromo
    en caso contrario retorna falso

    sentence -- srting o entero

    >>> palindromo("anita lava la tina")
    True

    >>> palindromo(12321)
    True

    palindromo("CodigoFacilito")
    False

    """

    sentence =str(sentence).lower().replace(" ", "") 
    return sentence == sentence[::-1]

# implementacion del DocString al principio del archivo 
class Recursivo:
    def factorial(self, number):
        if number == 0: return 1
        else: return number * self.factorial(number - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    doctest.testfile("test1.txt") # prueba de archivos externos