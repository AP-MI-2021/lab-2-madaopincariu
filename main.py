def get_leap_years(start, end):
    '''
    Afiseaza anii biscti din intervalul start si end
    :param start: primul an
    :param end: al doilea an
    '''
    list=[]
    for i in range(start,end+1):
        if i%400==0:
            list.append(i)
    return list
def test_get_leap_years():
    assert get_leap_years(1,1000)=="400 800"
    assert get_leap_years(2400, 3765) == "2400 2800 3200 3600"


def get_perfect_squares(start, end)
    '''
    Afiseaza patratele perfecte din intervalul start si end
    :param start: primul numar
    :param end: al doilea numar
    '''
    lst=[]
    for i in range(start,end+1):
        for j in range(2,i//2+1):
            if i/j==0:
                lst.append(i)
    return lst
def test_get_perfect_squares()
    assert get_perfect_squares(1,10)=="1 4 9"
    assert get_perfect_squares(25, 37)=="25 36"

while True:
    print('1.Afiseaza toti anii bisecti intre doi ani dati')
    print('Afiseaza toate patratele perfecte intre doua numere date')
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
    elif opt=='x':
        break
    else:
        print("optiune invalida")
