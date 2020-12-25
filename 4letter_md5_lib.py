import hashlib 

aa=[ 'a','b','c','d','e','f','g','h','i','j','k','l','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','@','£','#','_','&','-','+','(',')','/','*','"',"'",':',';','!','?','~','`','|','•','√','π','÷','×','¶','∆','€','¥','$','¢','^','°','=','{','}','%','©','®','™','✓','[',']','<','>','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

myhash=str(input('Enter your Hash\n'))
code=2
print('Wait i am working.')
#level 1 combinations trial +++

def level1(myhash):
    for a in aa:
        
        hash= hashlib.md5(a.encode('utf-8')).hexdigest()
        if myhash == hash :
            print ("\n\n\n |--------------|  YOUR KEY IS HERE |--------------| \n\n|{:<40} | {:<15}|".format("HASH","DECRYPTED")  )
            print("|{:<40} | {:<15}|".format('--------------------------------------','---------------'))
            print("|{:<40} | {:<15}|".format(hash,a))
            code=1
            break
            #trying 2 letter test
        for b in aa:
             dd=str(a+b)
             hash= hashlib.md5(dd.encode('utf-8')).hexdigest()
             if myhash == hash :
                 print ("\n\n\n |--------------|  YOUR KEY IS HERE |--------------| \n\n|{:<40} | {:<15}|".format("HASH","DECRYPTED")  )
                 print("|{:<40} | {:<15}|".format('--------------------------------------','---------------'))
                 print("|{:<40} | {:<15}|".format(hash,a+b))
                 code=1
                 break  
             for c in aa:
                 dd=str(a+b+c)
                 hash= hashlib.md5(dd.encode('utf-8')).hexdigest()
                 if myhash == hash :
                     print ("\n\n\n |--------------|  YOUR KEY IS HERE |--------------| \n\n|{:<40} | {:<15}|".format("HASH","DECRYPTED")  )
                     print("|{:<40} | {:<15}|".format('--------------------------------------','---------------'))
                     print("|{:<40} | {:<15}|".format(hash,a+b+c))
                     code=1
                     break  
                     
def level2(myhash):
                     for a in aa:
                         for b in aa:
                             for c in aa:
                                 for d in aa:
                                     dd=str(a+b+c+d)
                                     hash= hashlib.md5(dd.encode('utf-8')).hexdigest()
                                     if myhash == hash :
                                         print ("\n\n\n |--------------|  YOUR KEY IS HERE |--------------| \n\n|{:<40} | {:<15}|".format("HASH","DECRYPTED")  )
                                         print("|{:<40} | {:<15}|".format('--------------------------------------','---------------'))
                                         print("|{:<40} | {:<15}|".format(hash,a+b+c+d))
                                         code=1
                                         break                                                                
level1(myhash)
         
if code == 2 :    
        print('trying level 2')
        level2(myhash)
                 
                 
if code==2:                 
    print('if you dont find your key then increase no of forloops to try more combinations')
         


