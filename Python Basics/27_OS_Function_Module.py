#All OS functions
#Directory means folder

import os
curDir = os.getcwd() #gives out current directory address
print(curDir)

#make new Directory names 'newDir'
os.mkdir('newDir')


#changing name of 'newDir' to 'newDir2'
os.rename('newDir','newDir2')

#remove directory
os.rmdir('newDir2')

