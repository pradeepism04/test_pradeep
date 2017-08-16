import os
import json
x=os.system("sudo apt-get install python-pip")
if(x!=0):
	os.system("sudo apt install python-pip")
with open("dependency.json","r") as fp:
    data=json.load(fp)

failed=[]
for package in data['dependency']:   
    status=os.system("sudo pip install "+package)    
    if status!=0:       
        failed.append(package)
if(len(failed)>0):
    print ("installtion failed packages :")
    for fial in failed:
        print(fail)
else:
    print("All packeges has installed successfullly")
