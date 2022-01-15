import os
import datetime
import subprocess
import json
import time
def make_backup(path_to_xampp,db_name,backup_path):
    if not (os.path.isdir(backup_path)) :
        os.mkdir(backup_path) # if the directory is not exsist create it
    x=datetime.datetime.now()
    x=x.strftime("%Y%m%H%M%S")
    output_file_name=x
    cmd='%smysqldump -u root %s > %s%s%s.sql'
    cmd=cmd%(path_to_xampp,db_name,backup_path,db_name,output_file_name)
    s=os.system('cmd /c "%s"'%cmd)
    print (s)


# Opening JSON file
config_folder= 'c:\\backup_config'
config_file ='data.json'
if not (os.path.isdir(config_folder)) :
	os.mkdir (config_folder)
	print ("Make pro file directory")
if (os.path.isfile(config_folder + config_file)) :
	f = open(config_folder+ "\\" + config_file)
else :
	f = open(config_folder+ '\\'+ config_file, "w")
	txt='{ "db_info" : {"path_to_xampp" : "c:\\\\xampp\\\\mysql\\\\bin\\\\","backup_path" : "d:\\\\db\\\\","db_name" : "masar","db_user": "root","db_pass":""}}'
	f.write (txt)
	f.close()
	f = open(config_folder+ "\\" + config_file)
 
# returns JSON object as
# a dictionary
data = json.load(f)
# Closing file
f.close()


path_to_xampp=data['db_info']['path_to_xampp']
backup_path=data['db_info']['backup_path']
db_name=data['db_info']['db_name']
db_user=data['db_info']['db_user']
db_pass=data['db_info']['db_pass']
cnf_file = '.my1.cnf'
if (os.path.isfile(path_to_xampp + cnf_file)) : # Check if my.cnf file is excict
    make_backup(path_to_xampp,db_name,backup_path)
else :
    print ("Mycnf is not exsist .. Create one")
    f = open(path_to_xampp +cnf_file, "w")
    f.write (f"[mysqldump]\nuser={db_user}\npassword='{db_pass}'")
    f.close()
    make_backup(path_to_xampp,db_name,backup_path)
     
time.sleep(5) 
