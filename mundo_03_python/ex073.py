times_brasileirao = (
    "Palmeiras SP",
    "Gremio",
    "Atletico Mineiro MG",
    "Flamengo",
    "Botafogo FR RJ",
    "Red Bull Bragantino SP",
    "Fluminense RJ",
    "CA Paranaense PR",
    "Internacional RS",
    "Fortaleza CE",
    "São Paulo FC SP",
    "Cuiabá Esporte Clube MT",
    "Corinthians SP",
    "Cruzeiro",
    "Vasco Gama",
    "Bahia",
    "Santos FC SP",
    "Goiás EC GO",
    "Coritiba PR"
)
for t in times_brasileirao:
    print(t)
print('-='*20)
print(f'Os 5 primeiros são = {times_brasileirao[:5]}')
print('-='*20)
print(f'Os 4 últimos são = {times_brasileirao[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética = {sorted(times_brasileirao)}')
print('-='*20)
print(f'O Botafogo FR RJ está na  {times_brasileirao.index("Botafogo FR RJ")+1}ª posição ')