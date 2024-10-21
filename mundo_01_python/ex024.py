cidade = str(input('Escreva o nome de sua cidade = ')).strip()
print(cidade[:5].lower() == 'santo')
print('Santo' in cidade[:5] or 'santo' in cidade[:5])
