def intersects(a, b, c, d):
   # Estas instruções assert especificam e verificam o domínio da função.
   assert a < b
   assert c < d
   
   if b - c <= 0 or a - d >= 0:
      return 'Não Interseção'
   
   elif b - c > 0 or a - d < 0:
      return 'Interseção'

a = float(input('a? '))
b = float(input('b? '))
c = float(input('c? '))
d = float(input('d? '))
print(intersects(a, b, c, d))