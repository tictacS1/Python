def swap(s:str):
    a = ''
    l = len(s) - 1
    while l >= 0:
        a = a + s[l]
        l = l - 1
    print(a)

st = 'carambar'
swap(st)
st2= 'Bonjour_a_Tous'
swap(st2)