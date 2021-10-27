from math import sqrt

def get_leap_years(start, end):
    '''
    Afiseaza anii biscti din intervalul start si end
    :param start: primul an
    :param end: al doilea an
    '''
    lst=[]
    for i in range(start,end+1):
        if i%400==0 or (i%100!=0 and i%4==0):
            lst.append(i)
    return lst

def test_get_leap_years():
    assert get_leap_years(1582, 1600)==[1584, 1588, 1592, 1596, 1600]
    assert get_leap_years(1701,1720)==[1704, 1708, 1712, 1716, 1720]


def get_perfect_squares(start, end):
    '''
    Afiseaza patratele perfecte din intervalul start si end
    :param start: primul numar
    :param end: al doilea numar
    '''
    lst=[]
    for i in range(start,end+1):
        if int(sqrt(i))==sqrt(i):
            lst.append(i)
    return lst

def test_get_perfect_squares():
    assert get_perfect_squares(1,10)==[1, 4, 9]
    assert get_perfect_squares(25, 37)==[25, 36]

def is_palindrome(n):
    '''
    Determină dacă un număr dat este palindrom.
    :param n: un numar
    :return: True daca este palindrom sau False in caz contrar
    '''
    x=n
    inv=0
    while x!=0:
        c=x%10
        inv=inv*10+c
        x=x//10
    if inv==n:
        return True
    return False

def test_is_palindrome():
    assert is_palindrome(121) is True
    assert is_palindrome(97) is False

def main():
    test_get_leap_years()
    test_get_perfect_squares()
    test_is_palindrome()
    while True:
        print('1.Afiseaza toti anii bisecti intre doi ani dati')
        print('2.Afiseaza toate patratele perfecte intre doua numere date')
        print('3.Determină dacă un număr dat este palindrom.')
        print('x.Iesire din program')
        opt=input('Alege optiunea: ')
        if opt=='1':
            start=int(input('Dati primul nr:'))
            end=int(input('Dat al doilea nr:'))
            print(get_leap_years(start,end))
        elif opt=='2':
            start = int(input('Dati primul nr:'))
            end = int(input('Dat al doilea nr:'))
            print(get_perfect_squares(start, end))
        elif opt=='3':
            n=int(input('Dati numarul:'))
            print(is_palindrome(n))
        elif opt=='x':
            break
        else:
            print("optiune invalida")
main()