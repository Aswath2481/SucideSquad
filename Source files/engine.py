# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 15:08:02 2019
mark 1
@author: Zero
"""
import os,shutil,time
beacon='beacon.ssq' # how deep the recursion tree goes!!
z_file='dont_tamper.zombie' # #dummy file to get feed to the ransomware
db_file='loc_db.dat' #file name of the locations to protect
b_path=''   #template location of beacon 
threshold=10 # number of folders to be casted as ghost in case of attack
till=4 # how deep the recursion tree goes!!
p_folder=''#location of the db file
b_loc=[]  #location of all the beacons are stored in this list 
z_loc=[] #zombie location list
loc=[]   # locations to protect
#for starting task manager
taskmgr=os.path.join(os.environ['WINDIR'],'system32','taskmgr.exe')
#reading the locations to monitor
def read_loc():
    global sc_flag,p_folder,loc,b_path,b_loc
    for i in range(0,till):
       b_path=os.path.join(b_path,'1')
    b_path=os.path.join(b_path,beacon)
    #location of db file
    p_folder=os.path.join(os.path.expanduser('~'),'SucideSquad',db_file)
    # reading line by line
#    loc=[file.readlines() for file in open(p_folder,'r')]
    try:
        with open(p_folder,'r') as file:
            loc=[os.path.join(line.strip()) for line in file ]
#        os.path.join(line,b_path)
    except:
        pass
    b_loc=[os.path.join(i,b_path) for i in loc]
#    for u in b_loc:
#        print(u)

def monitor():
    flag=0
    global threshold
    global z_file,z_loc
    index=1
    z_path=''
    for j in range(0,till):
        z_path=os.path.join(z_path,str(int(till/2)))
    z_loc=[os.path.join(i,z_path) for i in loc]               
#    print(z_loc)
    # making container [ 1-10 ] in till/2 folder
    for j in z_loc:
        for i in range(1,threshold+1):
            cz_path=''
            cz_path=os.path.join(j,str(i))
            print(cz_path)
            if not os.path.exists(cz_path):
                os.makedirs(cz_path)

#        print(cz_path) 
    while 1:
        try:
            time.sleep(0.2)
            for i in b_loc:     #scanning all beacons
#                print(i)
                if not os.path.exists(i):
                    print('attack detected, spawning zombies...')
                    os.startfile(taskmgr)
                    flag=1
                    break
            if flag:        # to break the infy loop only when the attck is detetcted
                break
        except:
            break 
        
    while flag:
        time.sleep(0.1)
        try:
           for i in z_loc:
                     
               cz_path='' #zombie folder path
               cz_path=os.path.join(i,str(index))
#               print('CZ path: '+cz_path)
               if not os.path.exists(cz_path):  
                   os.makedirs(cz_path) # creating zombie folder
               zf_path=os.path.join(cz_path,z_file) #Creating zombie file
#               print('Zf path: '+zf_path)
               #dummy file creation using zombie extension
               file=open(zf_path,'w')
               file.write('die malware, die...')
               file.close()
               
               rm=os.path.join(i,str((index%10)+1)) # dynammically removing folder to contain the malware 
               if os.path.exists(rm):
                   shutil.rmtree(rm)
           index=index+1
           if index>threshold:
               index=1
            
        except Exception as e:
           print(e)
           break
def deploy_beacon():
    global b_loc
    for i in b_loc:
        print(i)
        with open(i,'w') as b_file:
            b_file.write('Dont alter this file....')

if __name__=='__main__':
    read_loc()
    deploy_beacon()    
    monitor() 
