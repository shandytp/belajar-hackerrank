# cara saya
def is_leap(year):
    '''
    Function untuk melakukan deteksi termasuk leap year atau tidak

    Parameters
    ---------
    year: int
        Input adalah sebuah tahun berupa `int`

    Returns
    -------
    leap: Boolean
        Hasil dari pengecekan is_leap
    '''
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 400 == 0:
        return True
    else:
        return False
            
    return leap

year = int(input())

# cara discussion

def is_leap(year):
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)