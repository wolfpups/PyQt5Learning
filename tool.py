# -*- coding: utf-8 -*-

'''
    ����顿
	uiת����py��ת������
     
'''

import os 
import os.path 

# UI�ļ����ڵ�·�� 
dir = './'  

# �г�Ŀ¼�µ�����ui�ļ�
def listUiFile(): 
	list = []
	files = os.listdir(dir)  
	for filename in files:  
		#print( dir + os.sep + f  )
		#print(filename)
		if os.path.splitext(filename)[1] == '.ui':
			list.append(filename)
	
	return list

# �Ѻ�׺Ϊui���ļ��ĳɺ�׺Ϊpy���ļ���	
def transPyFile(filename): 
	return os.path.splitext(filename)[0] + '.py' 

# ����ϵͳ�����uiת����py
def runMain():
	list = listUiFile()
	for uifile in list :
		pyfile = transPyFile(uifile)
		cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile,uifile=uifile)  
		#print(cmd)
		os.system(cmd)

###### ����������		
if __name__ == "__main__":  	
	runMain()