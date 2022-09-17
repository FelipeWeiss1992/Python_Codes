m = float(input('Uma distancia em metros:'))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('A média de {}m corresponde a {}km / {}hm / {}dam\n{}dm / {:.0f}cm / {:.0f}mm'.format(m, km, hm, dam, dm, cm ,mm  ))
