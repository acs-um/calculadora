# -*- coding: utf-8 -*-
#!/usb/bin/env python2

class Calculadora:
    def potencia(self, num1, num2):
        """
        Realiza la potencia de num1 en base a num2.
        """
        return num1**num2

    def modulo(self, num1, num2):
	"""
	Modulo de num1 y num2
	"""
	    if num2==0:
		    return "No se puede obtener el modulo si el num2 es 0"

	    return num1%num2

	def multi(self,num1,num2):

	    return num1*num2

    def division(self, num1, num2):
        if num2 == 0:
		    return "No se puede dividir por 0."

        return num1/num2

    def resta(self,num1, num2):
	"""Realiza la resta de dos numeros"""
        return num1-num2
