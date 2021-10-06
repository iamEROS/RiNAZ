import os,shutil
folder={
    'Videos':['.mp4','.mkv','.avi','mpeg4','3gp'],
    'Audio':['.mp3','.wav'],
    'Images':['.jpg','.png'],
    'Documents':['.doc','.docx','.xlsx','.xls','.pdf','.ppt','.pptx'],
    'Compressed Files':['.zip','.rar'],
    
}    

def rename_folder():
    for folder in os.listdir(directory):
        if os.path.isdir(os.path.join(directory,folder))==True:
            os.rename(os.path.join(directory,folder),os.path.join(directory,folder.lower()))


#print(folder)
#for folder_name in folder:
#    print(folder_name,folder[folder_name])

def create_move(ext,file_name):
    find=False
    for folder_name in folder:
        if "."+ext in folder[folder_name]:
            if folder_name not in os.listdir(directory):
                os.mkdir(os.path.join(directory,folder_name))
            shutil.move(os.path.join(directory,file_name),os.path.join(directory,folder_name))
            find=True
            #print('found',folder_name)
            break
    if find!=True:
        if other_name not in os.listdir(directory):
            os.mkdir(os.path.join(directory,other_name))
        shutil.move(os.path.join(directory,file_name),os.path.join(directory,other_name))

  

directory = "C:\\Users\\Andrew Gardner\\Desktop\\files" 
other_name = input("Enter the folder name for Unknown Files:")
rename_folder()

all_file=os.listdir(directory)
length=len(all_file)
count=1
#print(all_file)
for i in all_file:
   if os.path.isfile(os.path.join(directory,i))==True:
       create_move(i.split(".")[-1],i)
   print(f"Total Files: {length}| Done: {count}| Left: {length-count}")
   count+=1
       #print("Yes")
    
