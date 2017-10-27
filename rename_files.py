import os

def rename_files():
    #(1) Get file names from folder
    file_list = os.listdir(r"C:\practice\prank")
    print(file_list)
    os.chdir(r"C:\practice\prank")
    print("Current working directory is "+os.getcwd())
    
    #(2) Rename files
    for file_name in file_list:
        print("Old name - "+file_name)
        print("New name - "+file_name.translate(None, "0123456789"))
        os.rename(file_name,file_name.translate(None, "0123456789"))

rename_files()
