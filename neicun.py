# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(peng.zhou)s
"""

import ctypes
import os
import platform
import sys
import time
import shutil

model_path="./shapes20190516T2147/"#"C:/Users/My/Desktop/giga/"
free_detected_path="./"
rename_path="/media/jushi/ZHOUPENG/model_rename/"
i=0#time
def get_free_space_mb(folder):
  """ Return folder/drive free space (in bytes)
  """
#  print(platform.system())
  if platform.system() == 'Windows':
    free_bytes = ctypes.c_ulonglong(0)
    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
    final=free_bytes.value/1024/1024/1024
    return final
  else:
    st = os.statvfs(folder)
    return st.f_bavail * st.f_frsize/1024/1024/1024
#print(get_free_space_mb('C:\\'),'GB')
while(True):
    #file_list=os.listdir(model_path)#重复更新model_path下的所有文件
    file_list=os.listdir(model_path)
    s=[]
    file_list.sort(key=lambda x:(x[-7:-3]))
    for file in file_list:
            string=os.path.join(model_path,file)
            #print(string)
            s.append(string)
    #print("final",s)                
    #print(s[3])
    final_bytes=get_free_space_mb(free_detected_path)
    if i==40000:    
        print("checking the memory:\n",final_bytes,'GB')
        i=0

    if final_bytes>4:#you need change it to debug
        pass

            
    else:
        #add the logs/file_name/file_name.h5
        print("the",s[3],"will be renamed to",rename_path)
        shutil.move(s[3],rename_path)
        final_bytes=get_free_space_mb(free_detected_path)
        print("renamed over:",s[3],"----->and now the bytes is:",final_bytes,'GB')
    i+=1

    

