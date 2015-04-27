# -*- coding: utf-8 -*-
#!/usb/bin/env python2

class Calculadora:
    def potencia(self, num1, num2):
        """
        Realiza la potencia de num1 en base a num2.
        """
        return num1**num2

    def division(self, num1, num2):
	"""
	Realiza la división de num1 sobre num2 (num1/num2).
	"""
	if num2==0:
		return "No se puede dividir por 0."
	return num1/num2
