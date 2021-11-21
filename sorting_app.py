from tkinter import *
from ftplib import FTP
from tkinter import ttk, filedialog, messagebox
import os,shutil

global ftp
ftp = FTP('192.168.1.3', user='pi', passwd='25720227')
print("connected to FTP")

def Ok():
    uname = e1.get()
    password = e2.get()


    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")
    elif(uname == "Admin" and password == "123"):
        messagebox.showinfo("","Login Success")
    else :
        messagebox.showinfo("","Incorrect Username and Password")

root = Tk()
root.title("Login")
root.geometry ("300x150")

global el
global e2

Label(root, text="UserName").place (x=10, y=10)
Label(root, text="Password").place(x=10, y=40)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")       

Button(root, text="Login", command=Ok ,height = 1, width = 5).place(x=100, y=100)

class Sorting_App:
    def __init__(self,root):
        self.root=root
        self.root.title("RiNAZ")
        self.root.geometry("1360x720+0+0")
        self.root.config(bg="#222222")
        self.logo_icon=PhotoImage(file="C:\\Users\\Andrew Gardner\\Desktop\\Rinaz\\rinaz.png")
        title=Label(self.root,image=self.logo_icon, compound=LEFT,bg="black",fg="white").place(x=0,y=0,relwidth=1)

        #-------------A---------------
        self.var_foldername=StringVar()
        lbl_select_folder=Label(self.root,text="Select Folder",font=("times new roman", 25,), bg="#222222", fg="white").place(x=175,y=100)
        text_folder_name=Entry(self.root,textvariable=self.var_foldername,font=("times new roman", 15,),state='readonly', bg="lightgrey").place(x=400,y=100,height=40,width=600)
        btn_browse=Button(self.root,command=self.browse_fn,text="Browse",font=("times new roman", 15,"bold"),bg="#222222", fg="white",activebackground="grey",cursor="hand2", activeforeground="white").place(x=1050,y=100,height=45,width=150)
        hr=Label(self.root,bg="lightgrey").place(x=50,y=160,height=2,width=1750)

        #-------------B---------------
        self.image_extensions=["Image Extensions",".png",".jpg"]
        self.audio_extensions=["Audio Extensions",'.mp3','.wav']
        self.video_extensions=["Video Extensions",'.mp4','.mkv','.avi','mpeg4','3gp']
        self.doc_extensions=["Doc Extensions",'.doc','.docx','.xlsx','.xls','.pdf','.ppt','.pptx']


        self.folder={
                 'Videos':self.video_extensions,
                 'Audio':self.audio_extensions,
                 'Images':self.image_extensions,
                 'Documents':self.doc_extensions,
                 } 


        lbl_sup_ext=Label(self.root,text="Supported Extensions",font=("times new roman", 25,), bg="#222222", fg="white").place(x=50,y=175)
        #Image
        self.image_box=ttk.Combobox(self.root,values=self.image_extensions,font=("times new roman",15,'bold'),state='readonly',justify=CENTER)
        self.image_box.place(x=60,y=230,width=270,height=35)
        self.image_box.current(0)

        #Video
        self.video_box=ttk.Combobox(self.root,values=self.video_extensions,font=("times new roman",15,'bold'),state='readonly',justify=CENTER)
        self.video_box.place(x=380,y=230,width=270,height=35)
        self.video_box.current(0)

        #Audio
        self.audio_box=ttk.Combobox(self.root,values=self.audio_extensions,font=("times new roman",15,'bold'),state='readonly',justify=CENTER)
        self.audio_box.place(x=700,y=230,width=270,height=35)
        self.audio_box.current(0)

        #Documents
        self.doc_box=ttk.Combobox(self.root,values=self.doc_extensions,font=("times new roman",15,'bold'),state='readonly',justify=CENTER)
        self.doc_box.place(x=1025,y=230,width=270,height=35)
        self.doc_box.current(0)

        #-------------C---------------
        self.image_icon=PhotoImage(file="C:\\Users\\Andrew Gardner\\Desktop\\Rinaz\\image.png")
        self.video_icon=PhotoImage(file="C:\\Users\\Andrew Gardner\\Desktop\\Rinaz\\video.png")
        self.audio_icon=PhotoImage(file="C:\\Users\\Andrew Gardner\\Desktop\\Rinaz\\audio.png")
        self.document_icon=PhotoImage(file="C:\\Users\\Andrew Gardner\\Desktop\\Rinaz\\doc.png")
        self.other_icon=PhotoImage(file="C:\\Users\\Andrew Gardner\\Desktop\\Rinaz\\other.png")

        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="#222222")
        Frame1.place(x=50,y=285,width=1265,height=300)
        self.lbl_total_files=Label(Frame1,text="Total Files: ",font=("times new roman", 20,), bg="#222222", fg="white")
        self.lbl_total_files.place(x=10,y=10)
         
        #i have input numbers myself just for reference
        
        self.lbl_total_image=Label(Frame1,bd=2,relief=RAISED,image=self.image_icon,compound=TOP,font=("times new roman",20,"bold"),bg="#222222", fg="white")
        self.lbl_total_image.place(x=10,y=65,width=230,height=200)

        self.lbl_total_video=Label(Frame1,bd=2,relief=RAISED,image=self.video_icon,compound=TOP,font=("times new roman",20,"bold"),bg="#222222", fg="white")
        self.lbl_total_video.place(x=260,y=65,width=230,height=200)

        self.lbl_total_audio=Label(Frame1,bd=2,relief=RAISED,image=self.audio_icon,compound=TOP,font=("times new roman",20,"bold"),bg="#222222", fg="white")
        self.lbl_total_audio.place(x=510,y=65,width=230,height=200)

        self.lbl_total_doc=Label(Frame1,bd=2,relief=RAISED,image=self.document_icon,compound=TOP,font=("times new roman",20,"bold"),bg="#222222", fg="white")
        self.lbl_total_doc.place(x=760,y=65,width=230,height=200)

        self.lbl_total_other=Label(Frame1,bd=2,relief=RAISED,image=self.other_icon,compound=TOP,font=("times new roman",20,"bold"),bg="#222222", fg="white")
        self.lbl_total_other.place(x=1010,y=65,width=230,height=200)
        

        #-------------D---------------

        lbl_status=Label(self.root,text="Status: ",font=("times new roman", 25,), bg="#222222", fg="white").place(x=50,y=600)
        self.lbl_st_total=Label(self.root,text="",font=("times new roman", 19,), bg="#222222", fg="white")
        self.lbl_st_total.place(x=300,y=605)

        self.lbl_st_move=Label(self.root,text="",font=("times new roman", 19,), bg="#222222", fg="white")
        self.lbl_st_move.place(x=500,y=605)

        self.lbl_st_left=Label(self.root,text="",font=("times new roman", 19,), bg="#222222", fg="white")
        self.lbl_st_left.place(x=700,y=605)


        #------Button-----


        self.btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman", 15,"bold"),bg="#222222", fg="white",activebackground="grey",cursor="hand2", activeforeground="white")
        self.btn_clear.place(x=950,y=600,height=45,width=150)
        self.btn_start=Button(self.root,state=DISABLED,command=self.start_function,text="Start",font=("times new roman", 15,"bold"),bg="#222222", fg="white",activebackground="grey",cursor="hand2", activeforeground="white")
        self.btn_start.place(x=1150,y=600,height=45,width=150)
    
    def Total_count(self):
        images=0
        audios=0
        videos=0
        documents=0
        others=0
        self.count=0
        cmbine_list=[]
        for i in self.all_file:
            if os.path.isfile(os.path.join(self.directory,i))==True:
                self.count+=1
                ext="."+i.split(".")[-1]
                for folder_name in self.folder.items():
                    #print(folder_name)
                    for x in folder_name[1]:
                        cmbine_list.append(x)
                    if ext in folder_name[1] and folder_name[0]=="Images":
                        images+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="Audio":
                        audios+=1
                    if ext in folder_name[1] and folder_name[0]=="Videos":
                        videos+=1
                    if ext in folder_name[1] and folder_name[0]=="Documents":
                        documents+=1
                    if ext in folder_name[1] and folder_name[0]=="Others":
                        others+=1
        # this is for finding other files                
        for i in self.all_file:
            if os.path.isfile(os.path.join(self.directory,i))==True:
                ext="."+i.split(".")[-1]
                if ext not in cmbine_list:
                    others+=1

        self.lbl_total_image.config(text="Total Images\n"+str(images))
        self.lbl_total_video.config(text="Total Videos\n"+str(videos))
        self.lbl_total_audio.config(text="Total Audios\n"+str(audios))
        self.lbl_total_doc.config(text="Total Documents\n"+str(documents))
        self.lbl_total_other.config(text="Other Files\n"+str(others))
        self.lbl_total_files.config(text="Total Files: "+str(self.count))


    def browse_fn(self):
        op=filedialog.askdirectory(title="SELECT THE FOLDER FOR SORTING")
        if op!=None:
            #print(op)---just to check if it was working
            self.var_foldername.set(str(op))
            self.directory = self.var_foldername.get() 
            self.other_name = "Others"
            self.rename_folder()

            self.all_file=os.listdir(self.directory)
            length=len(self.all_file)
            count=1
            self.Total_count()
            self.btn_start.config(state=NORMAL)
            #print(self.all_file)
            # for i in self.all_file:
                #if os.path.isfile(os.path.join(self.directory,i))==True:
                    # self.create_move(i.split(".")[-1],i)
                   # pass
                # print(f"Total Files: {length}| Done: {count}| Left: {length-count}")
                # count+=1

    def start_function(self):
        if self.var_foldername.get()!="":
            self.btn_clear.config(state=DISABLED)           
            c=0
            for i in self.all_file:
                if os.path.isfile(os.path.join(self.directory,i))==True:
                    c+=1
                    self.create_move(i.split(".")[-1],i)
                    self.lbl_st_total.config(text="TOTAL: "+str(self.count))
                    self.lbl_st_move.config(text="MOVED: "+str(c))
                    self.lbl_st_left.config(text="REMAINING: "+str(self.count-c))

                    self.lbl_st_total.update()
                    self.lbl_st_move.update()
                    self.lbl_st_left.update()
                
            messagebox.showinfo("Success","All Files have been moved successfully")
            self.btn_start.config(state=DISABLED)
            self.btn_clear.config(state=NORMAL) 
        else:
            messagebox.showerror("Error!","Please select a folder")
    
    def clear(self):
        self.btn_start.config(state=DISABLED)
        self.var_foldername.set("")
        self.lbl_st_total.config(text="")
        self.lbl_st_move.config(text="")
        self.lbl_st_left.config(text="")
        self.lbl_total_image.config(text="")
        self.lbl_total_video.config(text="")
        self.lbl_total_audio.config(text="")
        self.lbl_total_doc.config(text="")
        self.lbl_total_other.config(text="")
        self.lbl_total_files.config(text="Total Files: ")
        


    def rename_folder(self):
            for folder in os.listdir(self.directory):
                if os.path.isdir(os.path.join(self.directory,folder))==True:
                    os.rename(os.path.join(self.directory,folder),os.path.join(self.directory,folder.lower()))


    def create_move(self,ext,file_name):
        find=False
        for folder_name in self.folder:
            if "."+ext in self.folder[folder_name]:
                if folder_name not in os.listdir(self.directory):
                    os.mkdir(os.path.join(self.directory,folder_name))
                shutil.move(os.path.join(self.directory,file_name),os.path.join(self.directory,folder_name))
                find=True
                #print('found',folder_name)
                break
        if find!=True:
            if self.other_name not in os.listdir(self.directory):
                os.mkdir(os.path.join(self.directory,self.other_name))
            shutil.move(os.path.join(self.directory,file_name),os.path.join(self.directory,self.other_name))
root.mainloop()   
root = Tk()
obj = Sorting_App(root)
root.mainloop()

