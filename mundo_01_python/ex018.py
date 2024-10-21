import math
an =float(input('Digite o ângulo: '))
sen =math.sin(math.radians(an))
cos =math.cos(math.radians(an))
tan =math.tan(math.radians(an))
print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(an,sen))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(an,cos))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(an,tan))
