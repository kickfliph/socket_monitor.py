import os
import sys
import glob
from datetime import datetime

def file_search(log_path, keyword, collect):
  count_lines = []  
  space = ' '
  for fname in glob.glob(log_path):
     with open(fname, 'r') as fp:
        x = len(fp.readlines())
        print('Total lines: ',fname, x)
 
        assing = fname+space+str(x)
        count_lines.append(assing)
        print(count_lines)
     try:
        with open(fname) as openfile:
           for line in openfile:
             #  space = ' '  
               noted = fname+space+line  
               if keyword in line:
                 collect.append(noted)
     except:
        print('Exception while reading file')
       
def file_compare(collect, white_ip, file_result):
  leng_01 = len(collect)
  leng_02 = len(white_ip)
  space = ' '
  for i in range(leng_01):
    line_content = collect[i].strip()
    line_split = line_content.partition("key_word_to_be_split")[2]
    k = 0
    print('this is k', k)
    print('this is White_IPs', leng_02)
    while (k < leng_02):
       print('Hello')
       print('split line', line_split)   
       print('white ip list', white_ip[k])
       if line_split == white_ip[k]:
          print('IP Found')
          print(line_split)
          print('Bye')

          on_list = 'This IP is White listed '
          on_list_result = line_content+space+on_list
          file_result.append(on_list_result)
          break
       else:
          k = k + 1
          print('this is k+ ==', k)
          print('next')
          if k == leng_02:
             off_list = 'This IP is NOT White listed '
             off_list_result = line_content+space+off_list
             file_result.append(off_list_result) 

def set_output(path_file, file_result):
  with open(path_file, 'w') as output:    
    for line in file_result:
      output.write(line)
      output.write('\n')
        
if __name__ == '__main__':
     scrped_file = []
     output_file = []
     file_time = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
     wss_ip_list = ['xxx.xxx.xxx.xxx', 'xxx.xxx.xxx.xxx', 'xxx.xxx.xxx.xxx']
     file_search(r'C:\path\of\the\file\to\filter, 'connection', scrped_file)
     file_compare(scrped_file, wss_ip_list, output_file)
     set_output(r'C:\path\of\the\where\to\output\results'+file_time+'.txt', output_file)           
