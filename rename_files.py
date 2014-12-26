import os

def rename_files():
    path = os.getcwd()+"/prank/"
    file_list = os.listdir(path)
    
    for file_name in file_list:
        
        new_name = file_name.translate(None, "1234567890")
        os.rename(path+file_name, path+new_name)
        print(file_name+" to "+new_name+"\n")
        

rename_files()
