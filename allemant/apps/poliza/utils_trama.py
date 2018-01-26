# -*- coding: utf-8 -*-

from .models import *
import datetime, xlrd 


def handle_uploaded_file(file_trama, poliza_id):


	# busca desde la columna cero
	file_trama.seek(0)

	print "el id de la poliza en excel-trama : %s " %poliza_id

	result = False

	book = xlrd.open_workbook(file_contents=file_trama.read())

	sheet = book.sheet_by_name("Sheet1")

	list_data = []

	for r in range(1, sheet.nrows):
		codigo_t = int(sheet.cell(r,0).value) 
		nombre_t = sheet.cell(r,1).value
		fecha_t = datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell(r,2).value, book.datemode))

		# test bulk_crete

		trama = ImportarTrama(codigo_t=codigo_t, nombre_t=nombre_t, fecha_t=fecha_t, poliza_trama_id=poliza_id)

		list_data.append(trama)

		if list_data:
			# bulk_create pasa la variable con todos los datos como un listado
			created_trama = ImportarTrama.objects.bulk_create(list_data)
			if len(list_data) == len(created_trama):
				result = True

