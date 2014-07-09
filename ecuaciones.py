from imprimir_ecuaciones import impecu

class Ecuaciones:
"""Esta aplicacion crea una funcion polinomial para aplicar distintas operaciones algebraicas y de calculo.
Basta con introducir dentro de la inicializacion el orden de la ecuacion como primer parametro y como segundo
parametro una lista con sus respectivas constantes."""
	def __init__(self, grado, constantes):
"""Contructor de la clase 'Ecuaciones'. Es imperativo indicar el grado y las constantes. El siguiente es un ejemplo
la declaracion de un objeto perteneciente a 'Ecuaciones':
			
			ecuacion = Ecuacion(grado, [constantes])"""
		self.grado = grado  # El atributo 'grado' es guardado.
		matriz = [0] *  (grado + 1)
		matriz[:len(constantes)] = constantes[:] # Se crea la lista de constantes.
		self.constantes = matriz  # El atributo 'contantes' es guardado.
		#impecu(grado, matriz)
		
	def derivada(self):  # Hace la derivada de un objeto 'Ecuaciones'.
		g = self.grado
		necu = []  # Crea una lista para agregar los nuevos coeficientes.
		for n in self.constantes:  # Aplica la formula de la derivada.
			aux = n * g
			necu.append(aux)
			g -= 1
		gr = self.grado - 1
		#impecu(gr, necu)  # Imprime el resultado.
		return gr, necu
		
	def integral(self):  # Realiza la integral de un objeto 'Ecuaciones'.
		g = self.grado   
		necu = [0] * (g + 2)  
		i = 0
		for n in self.constantes:  # Aplica la formula de la integral para polinomios.
			aux = n / (g + 1.0)
			necu[i] = aux
			g -= 1
			i += 1
		gr = self.grado + 1
		impecu(gr, necu)  # Imprime el resultado.
		return gr, necu
	
	def evaluar(self, var): # Evalua la funcion polinomial con el valor de 'var'
		g = self.grado
		aux = 0
		for n in self.constantes: # Bucle para viajar por cada constante
			if g == 0:
				aux = aux + n * (var ** g) 
				break
			else:
				aux = aux + n * (var ** g) # Formula de la integral de polinimios
				g -= 1 # Disminuye el grado de la ecuacion
		return aux
	
	def Newton_Method(self, objeto): # Metodo de Newton-Rhapson para el calculo de raices polinomiales.
		g = objeto.grado
		dg, dc = objeto.derivada()  # Determina la derivada de 'objeto'.
		deriv = Ecuaciones(dg, dc)  # Crea la ecuacion de la derivada
		op = 's'
		while op == 's':
			res = float(raw_input('Valor Inicial: '))  # C.I. de las iteraciones
			cont = 1
			while cont < 20:  # 20 iteraciones para converger
				res = res - (objeto.evaluar(res) / deriv.evaluar(res)) # Formula del metodo
				cont += 1
			print res
			op = raw_input('Continuar? (s/n): ') # Cambiar el valor de la C.I.
		
	def impecuacion(self):  # Imprime la ecuacion de un objeto 'Ecuaciones.'
		ecu = ''
		g = self.grado
		aux = 0
		for num in self.constantes:   # Bucle que imprime la ecuacion en representacion algebraica.
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

