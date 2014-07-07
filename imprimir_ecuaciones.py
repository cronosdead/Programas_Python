def impecu(grado, const):  # Función en forma de módulo para imprimir una ecuació polinómica.
		ecu = ''
		g = grado
		aux = 0
		for num in const:   # Bucle que imprime la ecuacion en representacion algebraica.
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
