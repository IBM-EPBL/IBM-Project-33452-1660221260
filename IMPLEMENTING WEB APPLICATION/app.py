import ibm_db

hostname="3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
uid="wqf68667"
pwd="i8rNrSxSu183vv0e"
driver="{IBM DB2 ODBC DRIVER}"
db="bludb"
port="31498"
protocol="TCPIP"
cert="Certificate.crt"

dsn=(
    "DATABASE={0};"
    "HOSTNAME={1};"
    "PORT={2};"
    "UID={3};"
    "SECURITY=SSL;"
    "SSLServerCertificate={4};"
    "PWD={5};"
).format(db,hostname,port,uid,cert,pwd)
print(dsn)

try:
    db2=ibm_db.connect(dsn,"","")
    print("connected to database")
except:
    print("unable to connect",ibm_db.conn_errormsg())