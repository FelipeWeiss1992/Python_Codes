a = float(input('Altura da parede?'))
l = float(input('Largura da parede?'))
area = a * l
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m² \nPara pintar essa parede, voce precisará de {}l de '
      'tinta.'.format(a,l, area, tinta))

