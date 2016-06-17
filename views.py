"""
	Views.py file contains methods about what should be returned to the viewport.
"""

from django.shortcuts import render
from django.http import HttpResponse


def hey(request):
	return render(request, 'wisumUtleie/scannernew.html')
	#return HttpResponse("<h1>HALLAO!</h1>")


def scanner(request):

	""" Her brukes request-objektet flittigself.
		
		request.method, returnerer hvilken metode som er brukt 
		  for å sende data via Http-protokollen, GET eller POST.
		
		request.GET, er en dictionary(JSON-object) som inneholder 
		   alle variabler som er sendt med Http GET.
				
			GET:
			- ?  - starten på en GET-request
			- %  - markerer et mellomrom i en GET-request string.
			- &  - markerer begynnelsen på en ny variabel
			- =  - skilletegn mellom variabel-navn og variabel-verdi.
	  	"""

	#if request.GET:
	#	varenummer = request.GET
	#	print('\nDette er printet i consollen: ', varenummer['d'], '\n')
	#	return HttpResponse("<h1>" + varenummer['d'] + "</h1>")

	return render(request, 'wisumUtleie/scannernew.html')
