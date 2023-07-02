# All the paths of directories given below are hardcoded as per my computer for decreasing complication
# All the path has to be taken input by the user, this has to be implemented afterwards 
import os
import shutil
print(os.getcwdb())# cwd '/mnt/c/users/surya_h3yma/Autodesk/python'
list_dir = os.listdir('/mnt/c/users/surya_h3yma/Autodesk/python')# list of files and directories(folders) in python directory
os.mkdir('directory_for_files') # created a folder for storing all the files extracted from inside folders

# lets say i have taken all the files from python directory amd moved them to extensions folder in python directory
# no i am left with four directories or folders in python directory(Extensions,Numbers,directory_for_files)
# now moving forward from numbers directory, assuming only one extra folder in home directory
name_of_source_folder = input("Enter the name of source folder : ")
path_of_source = '/mnt/c/users/surya_h3yma/Autodesk/python/'+name_of_source_folder
print(path_of_source)
# defining a function such that it takes a path of certain folder and makes list of all files or folders inside it
#   
def recursion(path):
    ls_of_f_and_fol_in_given_path=os.listdir(path)
    print(ls_of_f_and_fol_in_given_path)
    j=0
    for file in ls_of_f_and_fol_in_given_path:
        print(j)
        os.chdir(path)
        print("check file")
        print(ls_of_f_and_fol_in_given_path)
        print("again file")
        print(file)
        print(os.getcwdb())
        if(os.path.isfile(file)):#  if it is file
            i =5
            print("It is a file")
            if(((os.listdir('/mnt/c/users/surya_h3yma/Autodesk/python/directory_for_files')).count(file))==0):
                shutil.move(file,'/mnt/c/users/surya_h3yma/Autodesk/python/directory_for_files')# then moving all files to directory created in home  
            else:
                print(file)
                print("old"+str(i))
                newname= str(j)+ "_"+file
                print(newname)
                os.rename(file,newname)
                shutil.move(newname,'/mnt/c/users/surya_h3yma/Autodesk/python/directory_for_files')# then moving all files to directory created in home                
            i=i+1
            print("Newi" + str(i))
        elif(os.path.isdir(file)):# if it is folder
            print("It is a folder")
            path2 = path + '/'+ file # here we have checked above that this file is a folder
            print(path2)
            recursion(path2)
        j=j+2
recursion(path_of_source)
print("program completed")            