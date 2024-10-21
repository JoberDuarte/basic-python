def voto(ano):
    from datetime import date    
    ano = date.today().year
    idade = ano - nasc
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO!'
    elif idade >= 17 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    else:
        return f'Com {idade} anos: VOTO OPICIONAL!'


nasc =int(input('Em que ano você nasceu? '))
print(voto(nasc))