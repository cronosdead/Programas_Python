# Programa para contar el numero de una letra especifica
# dentro de una cadena intruducida por el usuario.
def contador_letras(cadena, letra):
	con = 0
	con2 = 0
	for l in cadena:
		if l == letra:
			con += 1
		if l == ' ':
			con2 += 1
	print 'Hay ', con, letra + '(s).\n'
	print 'Numero de Palabras: ', con2 + 1, '.'
