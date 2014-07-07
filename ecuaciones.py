class Ecuaciones:
	"""Esta aplicacion crea una funcion polinomial para aplicar distintas operaciones algebraicas y de calculo.
	Basta con introducir dentro de la inicializacion el orden de la ecuacion como primer parametro y como segundo
	parametro una lista con sus respectivas constantes."""
	def __init__(self, grado, constantes):
		"""Contructor de la clase 'Ecuaciones'. Es imperativo indicar el grado y las constantes. El siguiente es un ejemplo
		la declaracion de un objeto perteneciente a 'Ecuaciones':
			
					ecuacion = Ecuacion(grado, [constantes])"""
		self.grado = grado  # El atributo 'grados' es guardado.
		matriz = [0] *  (grado + 1)
		matriz[:len(constantes)] = constantes[:] # Se crea la lista de constantes.
		self.constantes = matriz  # El atributo 'contantes' es guardado.
		ecu = ''
		g = grado
		aux = 0
		for num in matriz:   # Bucle que imprime la ecuacion en representacion algebraica.
			if aux == 0:
				aux += 1
				if num  == 0:
					if g == 0:
						ecu =  ecu + '= 0'
						break
					else:
						g -= 1
				elif num == 1:
					if g == 0:
						ecu = ecu + str(num) + '= 0'
						break
					elif g == 1:
						ecu = ecu + 'x'
						g -= 1
					else:
						ecu = ecu + 'x^' + str(g)
						g -= 1
				elif num < -1:
					if g == 0:
						ecu = ecu + str(num) + '= 0'
						break
					elif g == 1:
						ecu = ecu + str(num) +'x'
						g -= 1
					else:
						ecu = ecu + str(num) + 'x^' + str(g)
						g -= 1
				elif num == -1:
					if g == 0:
						ecu = ecu + str(num) + '= 0'
						break
					elif g == 1:
						ecu = ecu + '-x'
						g -= 1
					else:
						ecu = ecu + '-x^' + str(g)
						g -= 1
				else:
					if g == 0:
						ecu = ecu + str(num) + '= 0'
						break
					elif g == 1:
						ecu = ecu + str(num) + 'x'
						g -= 1
					else:
						ecu = ecu + str(num) + 'x^' + str(g)
						g -= 1
			else:	
				if num  == 0:
					if g == 0:
						ecu =  ecu + '= 0'
						break
					else:
						g -= 1
				elif num == 1:
					if g == 0:
						ecu = ecu + '+ ' + str(num) + '= 0'
						break
					elif g == 1:
						ecu = ecu + '+ x'
						g -= 1
					else:
						ecu = ecu + '+ x^' + str(g)
						g -= 1
				elif num < -1:
					if g == 0:
						ecu = ecu + str(num) + '= 0'
						break
					elif g == 1:
						ecu = ecu + str(num) +'x'
						g -= 1
					else:
						ecu = ecu + str(num) + 'x^' + str(g)
						g -= 1
				elif num == -1:
					if g == 0:
						ecu = ecu + str(num) + '= 0'
						break
					elif g == 1:
						ecu = ecu + '-x'
						g -= 1
					else:
						ecu = ecu + '-x^' + str(g)
						g -= 1
				else:
					if g == 0:
						ecu = ecu + '+ ' + str(num) + '= 0'
						break
					elif g == 1:
						ecu = ecu + '+ ' + str(num) + 'x'
						g -= 1
					else:
						ecu = ecu + '+ ' + str(num) + 'x^' + str(g)
						g -= 1
		print ecu 
