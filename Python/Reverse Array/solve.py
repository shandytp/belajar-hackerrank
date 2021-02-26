def reverseArray(a):
    '''
    Function untuk melakukan reversing array

    Parameters
    ----------
    a: list[int]
        Array atau inputan yang akan di reverse

    Returns
    -------
    a: list[int]
        Hasil dari reversed array
    '''
    return a[::-1]

print(reverseArray([1,2,3,4]))