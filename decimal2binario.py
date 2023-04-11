import unittest


def decimal2binario(decimal):
    decimal = int(decimal)
    final = ""
    while decimal >= 2:
        final = final + str(decimal%2)
        decimal = decimal//2
    final = final + str(decimal)
    final = final[:: -1]
    return(final)


if __name__ == '__main__':
    unittest.main()
