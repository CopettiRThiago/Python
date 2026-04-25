# Conversor de Medidas

medida = float(input('Informe a medida em metros : '))
print('A medida de {} metros corresponde a:'.format(medida))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('{:.4f} km \n{:.3f} hm \n{:.2f} dam \n{:.0f} dm \n{:.0f} cm'
'\n{:.0f} mm'.format(km, hm, dam, dm, cm, mm))


# print('{} km'.format(km))
# print('{} hm'.format(hm))
# print('{} dam'.format(dam))
# print('{:.0f} dm'.format(dm))
# print('{:.0f} cm'.format(cm))
# print('{:.0f} mm'.format(mm))
