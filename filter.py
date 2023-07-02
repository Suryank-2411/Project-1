import os
import shutil
print(os.getcwdb())
list_of_files = []
list_of_folders = []
list_dir = os.listdir('/mnt/c/users/surya_h3yma/Autodesk/python')
print(list_dir)
# defining a function for getting the extension of the file
def getextension(fullfilename):
    length = len(fullfilename)
    index =0
    o=0
    for k in fullfilename:
        if(k=="."):
            index = fullfilename.index(k)
            o=o+1
            break
        else:
            continue
    if(o!=1):
        return print(" . not found")
    new_string = []
    ext = ''
    for char in range(index,length):
        new_string.append(fullfilename[char])
        print(new_string)
    for elem in new_string:
        ext = ext + elem
    return ext
# defining a function for checking that file is normal file or a directory
def check_if_file_or_dir(path_of_file):        # this path will receive the name of the element in the list of files in any folder
    if(os.path.isfile(path_of_file)):
        return "file"
    elif(os.path.isdir(path_of_file)):
        return "directory"
    else:
        return "none"
# making seperate list of files and folders
def create_list_of_files_and_folders(folder_list):
    for files in folder_list:
        check = check_if_file_or_dir(files)
        if(check == "file"):
            list_of_files.append(files)
        elif(check=="directory"):
            list_of_folders.append(files)
create_list_of_files_and_folders(list_dir)
print(list_of_folders)
print(list_of_files)
list_of_folders_in_Extensions_folder = os.listdir('/mnt/c/users/surya_h3yma/Autodesk/python/Extensions')
print(list_of_folders_in_Extensions_folder)
# defining a function to make a new directory in extensions folder
def make_new_directory_in_Extensions(name_of_folder):
    os.chdir('/mnt/c/Users/surya_h3yma/Autodesk/python/Extensions')
    print(os.getcwdb())
    os.mkdir(name_of_folder)
    print("New folder created named"+name_of_folder)
    os.chdir('/mnt/c/Users/surya_h3yma/Autodesk/python')

# now picking up files one by one and moving it to particular extension folder if not there creating it 
for anyfile in list_of_files:
    ext = getextension(anyfile)
    print(ext) 
    path = '/mnt/c/users/surya_h3yma/Autodesk/python/Extensions'+'/'+ext
    if(list_of_folders_in_Extensions_folder.count(ext) > 0):
        get_list_ext = os.listdir(path)
        if(get_list_ext.count(anyfile)>0):
            os.chdir('/mnt/c/users/surya_h3yma/Autodesk/python')
            newfile = '1_'+anyfile
            os.rename(anyfile,newfile)
        else:
            shutil.move(anyfile,path)
    else:
        make_new_directory_in_Extensions(ext)
        shutil.move(anyfile,path)