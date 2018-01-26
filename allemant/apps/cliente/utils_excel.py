# -*- coding: utf-8 -*-

# from servers.models import *
# import csv

# # de prueba para excel
# def handle_uploaded_file(file, valid_fields_method, record_creation_function):

# 	file.seek(0)

# 	# !importtant
# 	# archivo csv debe ser codificado en UTF-8
# 	# la clase Sniffer se utiliza para deducir el formato de un archivo CSV.
# 	sniffdialect = csv.Sniffer().sniff(file.read(10000))
# 	file.seek(0)

# 	#print sniffdialect.fieldnames
# 	data = csv.DictReader(file, dialect=sniffdialect)

# 	if not valid_fields_method(data.fieldnames):
# 		return False, -1
# 		print "no es valido lo que subiste"

# 	result, rows_error = record_creation_function(data)

# 	return result, rows_error


# def account_valid_fields(field_names):
# 	required_fields = ('first_name', 'last_name', 'unique_id')

# 	for field in required_fields:
# 		if field not in field_names:
# 			return False
# 	return True


# def create_account_in_db(dict_data):
# 	list_data = []
# 	result = False
# 	rows_error = 0
# 	for record in dict_data:
# 		first_name = record['first_name']
# 		last_name = record['last_name']
# 		unique_id = record['unique_id']

# 		account = Account(first_name=first_name,\
# 			last_name=last_name,\
# 			unique_id=unique_id)#,\
# 			#grad_year=grad_year,\
# 			#account_type=account_type)
# 		list_data.append(account)

# 	if list_data:
# 		# bulk_create pasa la variable con todos los datos como un listado
# 		created_accounts = Account.objects.bulk_create(list_data)
# 		if len(list_data) == len(created_accounts):
# 			result = True
# 		else:
# 			rows_error = len(list_data) - len(created_accounts)
	
# 	return result, rows_error