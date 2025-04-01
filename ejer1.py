tem_fam= float(input('Ingrese la temperatura en F: '))
""" temp_c= tem_fam - 32
temp_c= temp_c * 5
temp_c= temp_c / 9 """

temp_c=((tem_fam -32)*5)/9


temp_k= temp_c + 273.15
print(f'Grados celsius {temp_c:.2f}')
print(f'Grados kelvin {temp_k:.2f}')