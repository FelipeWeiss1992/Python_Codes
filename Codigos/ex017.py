from math import radians, sin, cos, tan
ang = int(input('Digite o ângulo que voce deseja:'))
radians(ang)
sen = sin(radians(ang))
cos = cos(radians(ang))
tag = tan(radians(ang))
print('O angulo de {:.1f} tem o SENO de {:.2f}'.format(ang, sen))
print('O angulo de {:.1f} tem o COSSENO de {:.2f}'.format(ang, cos))
print('O angulo de {:.1f} tem a TANGENTE de {:.2f}'.format(ang, tag))


