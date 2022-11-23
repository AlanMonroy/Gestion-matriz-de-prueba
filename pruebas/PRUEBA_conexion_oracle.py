import cx_Oracle

try:
	# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
	connection = cx_Oracle.connect(user="QAVIEW", password="Passw0rd#20",
	                               dsn="10.184.40.120:1521/FCTPEQA.FEMCOM.NET")
	cursor = connection.cursor()
	
	#cursor.execute("""
	#        SELECT first_name, last_name
	#        FROM employees
	#        WHERE department_id = :did AND employee_id > :eid""",
	#        did = 50,
	#        eid = 190)
	#for fname, lname in cursor:
	#    print("Values:", fname, lname)
except Exception as error:
	print(error)