def convert(number):
    b = ''
    if number % 3 == 0:
        b += 'Pling'
    if number % 5 == 0:
        b += 'Plang'
    if number % 7 == 0:
        b += 'Plong'
    if b == '':
        return str(number)
    return b
