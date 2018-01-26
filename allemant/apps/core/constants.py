ID_SEXO = 1
ID_ESTADO_CIVIL = 2 
ID_GIRO_NEGOCIO = 11
ID_OPERADOR = 18
ID_AREA_SUPERVISORA = 6

'''
1	sexo
2	estado civil
3	estado allemant
4	area allemant
5	cargo allemant
6	area supervisora
7	area ejecutiva
8	estado funcionario
9	area funcionario
10	cargo funcionario
11	giro negocio
12	grupo economico
13	clasificacion cliente
14	ramo
15	estado poliza
16	tipo correo electronico
17	operador telefonico
18	codigo provincia
19	moneda
'''
'''


RAMO = 'RM'

MONEDA = 'MN'
GIRO_NEGOCIO = 'GN'
GRUPO_ECONOMICO = 'GE'
CLASIFICACION_COLEGIO = 'CC'
TIPOS = ((RAMO,'Ramo'),
		(OPERADOR,'Operador'),
		(MONEDA, 'Moneda'),
		(GIRO_NEGOCIO,'Giro Negocio'),
		(GRUPO_ECONOMICO, 'Grupo Economico'),
		(CLASIFICACION_COLEGIO,'Clasificacion Colegio'),
		)


#ESTADO CIVIL 
SOLTERO = 'SL'
CASADO = 'CS'
DIVORCIADO = 'DV'
VIUDO = 'VD'

ESTADO_CIVIL = ((SOLTERO,'Soltero'),
				(CASADO,'Casado'),
				(DIVORCIADO,'Divorciado'),
				(VIUDO,'Viudo'),)


# SEXO 
MASCULINO = "M"
FEMENINO = "F"

SEXO = ((MASCULINO,'Masculino'),
		(FEMENINO, 'Femenino'),)


# SITUACIONES FUNCIONARIOCIA / FUNCIONARIOCLIENTE
SITUACION = (('A', 'Activo'),
			('D', 'Desactivo'))


#AREA_FUNCIONARIO : FUNCIONARIOCIA / FUNCIONARIOCLIENTE
RECURSOSHUMANOS = "RHH"
COMERCIAL = "COM"
FINANZAS = "FIN"
RECUPERACIONES = "REC"
LOGISTICA = "LOG"
IMAGEN = "IMA"
FISCALIZACION = "FIS"
ADMINISTRACION = "ADM"

AREA_FUNCIONARIO = ((RECURSOSHUMANOS,'Recursos Humanos'),
					(COMERCIAL, 'Comercial'),
					(FINANZAS, 'Finanzas'),
					(RECUPERACIONES, 'Recuperaciones'),
					(LOGISTICA, 'Logistica'),
					(IMAGEN, 'Imagen'),
					(FISCALIZACION, 'Fiscalizacion'),
					(ADMINISTRACION, 'Administracion'),)


#CARGO_FUNCIONARIO : FUNCIONARIOCIA / FUNCIONARIOCLIENTE
GERENTERECURSOSHUMANOS = "GRHH"
GERENTECOMERCIAL = "GCOM"
GERENTEFINANZAS = "GFIN"
GERENTERECUPERACIONES = "GREC"
GERENTELOGISTICA = "GLOG"
GERENTEIMAGEN = "GIMA"
GERENTEFISCALIZACION = "GFIS"
GERENTEADMINISTRACION = "GADM"

CARGO_FUNCIONARIO = ((GERENTERECURSOSHUMANOS,'Gerente Recursos Humanos'),
					(GERENTECOMERCIAL, 'Gerente Comercial'),
					(GERENTEFINANZAS, 'Gerente Finanzas'),
					(GERENTERECUPERACIONES, 'Gerente Recuperaciones'),
					(GERENTELOGISTICA, 'Gerente Logistica'),
					(GERENTEIMAGEN, 'Gerente Imagen'),
					(GERENTEFISCALIZACION, 'Gerente Fiscalizacion'),
					(GERENTEADMINISTRACION, 'Gerente Administracion'),) 


# ESTADOS EMPLEADO
ESTADO_EMPLEADO = (('A', 'Alta'),
					('D', 'Descanso'),
					('V', 'Vacaciones'),
					('M', 'Maternidad'),
					('B', 'Baja'),)


#CIUDAD

Lima = 'LA'
Barranca = 'BA'
Cajatambo  = 'CO'
Canta = 'CA'
Canete = 'CE'
Huaral  = 'HL'
Huarochiri   = 'HI'
Huaura  = 'HA'

CIUDAD = ((Lima,'Lima'),
				(Barranca,'Barranca'),
				(Cajatambo,'Cajatambo'),
				(Canta,'Canta'),
				(Canete,'Canete'),
				(Huaral,'Huaral'),
				(Huarochiri,'Huarochiri'),
				(Huaura,'Huaura'),
					)

#DISTRITO
Lima = 'LIA'
Ancon='ANN'
Ate='ATE'
Barranco='BAO'
Brena='BRA'
Carabayllo='CAO'
Chaclacayo='CHO'
Chorrillos='CHS'
Cieneguilla='CIA'
Comas='COS'
ElAgustino='ELO'
Independencia='INA'
Barranca='BAA'
Paramonga='PAA'
Pativilca='PTA'
Supe='SUE'
SupePuerto='SUO'

DISTRITO = ((Lima,'Lima'),
				(Ancon,'Ancon'),
                (Ate,'Ate'),
                (Barranco,'Barranco'),
                (Brena,'Brena'),
                (Carabayllo,'Carabayllo'),
                (Chaclacayo,'Chaclacayo'),
                (Chorrillos,'Chorrillos'),
                (Cieneguilla,'Cieneguilla'),
                (Comas,'Comas'),
                (ElAgustino,'ElAgustino'),
                (Independencia,'Independencia'),
                (Barranca,'Barranca'),
                (Paramonga,'Paramonga'),
                (Pativilca,'Pativilca'),
                (Supe,'Supe'),
                (SupePuerto,'SupePuerto'),
					)
'''

