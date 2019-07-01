# mark1
# 27.06.2019
#SpawnShield :  the program which gets executed when you right click 
#					 and select 'Protect this folder option' 
# Purpose: 	It spawns Tree like recursive folders on the front line.
# Any ransomware tries to alter the beacon.ssq which is at the front line
# Engine.py monitors the beacon.ssq and opens the task manager incase of any change in the file.
import os,ctypes,datetime
beacon='beacon.ssq' #The file which is being monitored for attack, 
z_file='dont_tamper.zombie' #dummy file to get feed to the ransomware
db_file='loc_db.dat' #file name of the locations to protect
b_path=''  
c_path='' #current path
sc_flag=0
a_flag=0
threshold=10 # number of folders to be casted as ghost in case of attack
till=4 # how deep the recursion tree goes!!
#Recursive function
def r_fun(path,i,j):
    sub_path = path+'/'+str(i)
    if j>till:
        return
    if not os.path.exists(sub_path):
#        print('going to function',i,j+1)
#        print(path,sub_path)
        for k in range(1,till):
            r_fun(sub_path,k,j+1)
    if not os.path.exists(path):
#        print(sub_path,j)
        os.makedirs(sub_path)
		#creating dummy file in each folder
        try:
            x=datetime.datetime.now()
            timestamp=x.strftime("%d_%m_%Y_%H_%M_%S")
            fpath=path+'/'+'SuCiDeSqUaD_'+timestamp+'.dat'
            file=open(fpath,'wb')
            file.close()
        except Exception as e:
            print(e)
            
			#function to cast the shield spell
def spawnshield():
    global c_path,sc_flag,a_flag
    c_path=os.path.join(os.getcwd(),'_sc') #Root directory creation, so that file system of user is not screwed
    if not os.path.exists(c_path):
        os.mkdir(c_path)
        sc_flag=1 #successfull creation indicator
        ret=ctypes.windll.kernel32.SetFileAttributesW(c_path,0x02)  #making the folder hidden
#        print(ret)
    else:
        a_flag=1		#indicating existence of _sc folder already!!
    os.chdir(c_path)   #changing the root directory
    for i in range(1,till):
        r_fun(c_path,i,0)
        
def deploy_beacon():
    global b_path
    for i in range(0,till):
       b_path+='1/'
    b_path+=beacon
#    print(b_path)
    b_file=open(b_path,'w')
    b_file.write('Dont alter this file....')
    b_file.close()
    
def storelocation():
    global sc_flag
    p_folder=os.path.expanduser('~')+'\SucideSquad'
    print('location stored')
    if not os.path.exists(p_folder):
        os.makedirs(p_folder)
    db_path=p_folder+'/'+db_file
#    print(db_path)
    if sc_flag:
        with open(db_path,'a') as file:
            file.write(c_path+'\n')

if __name__=='__main__':
	spawnshield()
	deploy_beacon()
	#for avoiding duplicate entries
	if not a_flag:
		storelocation()