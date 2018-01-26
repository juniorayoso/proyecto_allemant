# -*- coding: utf-8 -*-

from .models import *
import datetime, xlrd 


def handle_uploaded_file(file_independiente, poliza_id):

	# busca desde la columna cero
	file_independiente.seek(0)

	print "el id de la poliza en excel-indepente : %s " %poliza_id
	result = False
	book = xlrd.open_workbook(file_contents=file_independiente.read())
	sheet = book.sheet_by_name("Sheet1")
	list_data = []


	for row in range(0, sheet.ncols):
		label = sheet.cell(0, row).value
		for r in range(1 , sheet.nrows):
			fila = r
			valor = sheet.cell(r,row).value

			dependiente = ImportarDependiente(fila=fila,
											label=label, 
											valor=valor, 
											poliza_independiente_id=poliza_id)

			list_data.append(dependiente)

	if list_data:
		created_dependiente = ImportarDependiente.objects.bulk_create(list_data)

		if len(list_data) == len(created_dependiente):
			result = True

