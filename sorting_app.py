from tkinter import*
from tkinter import ttk, filedialog
import os,shutil
class Sorting_App:
    def __init__(self,root):
        self.root=root
        self.root.title("RiNAZ")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="white")
        self.logo_icon=PhotoImage(file="C:\\Users\\Andrew Gardner\\Desktop\\Rinaz\\output-onlinepngtools.png")
        title=Label(self.root,text="RiNAZ",padx=10, image=self.logo_icon, compound=LEFT, font=("times new roman",50,"bold"),bg="#023548",fg="white",anchor="w").place(x=0,y=0,relwidth=1)

        #-------------A---------------
        self.var_foldername=StringVar()
        lbl_select_folder=Label(self.root,text="Select Folder",font=("times new roman", 25,), bg="white").place(x=50,y=100)
        text_folder_name=Entry(self.root,textvariable=self.var_foldername,font=("times new roman", 15,),state='readonly', bg="lightgrey").place(x=250,y=100,height=40,width=600)
        btn_browse=Button(self.root,command=self.browse_fn,text="Browse",font=("times new roman", 15,"bold"),bg="grey",fg="white",activebackground="grey",cursor="hand2", activeforeground="white").place(x=900,y=95,height=45,width=150)
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


        lbl_sup_ext=Label(self.root,text="Supported Extensions",font=("times new roman", 25,), bg="white").place(x=50,y=175)
        #Image
        self.image_box=ttk.Combobox(self.root,values=self.image_extensions,font=("times new roman",15,'bold'),state='readonly',justify=CENTER)
        self.image_box.place(x=60,y=230,width=270,height=35)
        self.image_box.current(0)

        #Video
        self.video_box=ttk.Combobox(self.root,values=self.video_extensions,font=("times new roman",15,'bold'),state='readonly',justify=CENTER)
        self.video_box.place(x=400,y=230,width=270,height=35)
        self.video_box.current(0)

        #Audio
        self.audio_box=ttk.Combobox(self.root,values=self.audio_extensions,font=("times new roman",15,'bold'),state='readonly',justify=CENTER)
        self.audio_box.place(x=740,y=230,width=270,height=35)
        self.audio_box.current(0)

        #Documents
        self.doc_box=ttk.Combobox(self.root,values=self.doc_extensions,font=("times new roman",15,'bold'),state='readonly',justify=CENTER)
        self.doc_box.place(x=1090,y=230,width=270,height=35)
        self.doc_box.current(0)

        #-------------C---------------
        self.image_icon=PhotoImage(file="C:\\Users\\Andrew Gardner\\Desktop\\Rinaz\\image.png")
        self.video_icon=PhotoImage(file="C:\\Users\\Andrew Gardner\\Desktop\\Rinaz\\video.png")
        self.audio_icon=PhotoImage(file="C:\\Users\\Andrew Gardner\\Desktop\\Rinaz\\audio.png")
        self.document_icon=PhotoImage(file="C:\\Users\\Andrew Gardner\\Desktop\\Rinaz\\doc.png")
        self.other_icon=PhotoImage(file="C:\\Users\\Andrew Gardner\\Desktop\\Rinaz\\other.png")

        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=50,y=285,width=1750,height=300)
        self.lbl_total_files=Label(Frame1,text="Total Files: ",font=("times new roman", 20,), bg="white")
        self.lbl_total_files.place(x=10,y=10)
         
        #i have input numbers myself just for reference
        
        self.lbl_total_image=Label(Frame1,bd=2,relief=RAISED,text="Total Images\n250",image=self.image_icon,compound=TOP,font=("times new roman",20,"bold"),bg="lightblue")
        self.lbl_total_image.place(x=10,y=65,width=230,height=200)

        self.lbl_total_video=Label(Frame1,bd=2,relief=RAISED,text="Total Audios\n250",image=self.video_icon,compound=TOP,font=("times new roman",20,"bold"),bg="lightblue")
        self.lbl_total_video.place(x=260,y=65,width=230,height=200)

        self.lbl_total_audio=Label(Frame1,bd=2,relief=RAISED,text="Total Videos\n250",image=self.audio_icon,compound=TOP,font=("times new roman",20,"bold"),bg="lightblue")
        self.lbl_total_audio.place(x=510,y=65,width=230,height=200)

        self.lbl_total_doc=Label(Frame1,bd=2,relief=RAISED,text="Total Documents\n250",image=self.document_icon,compound=TOP,font=("times new roman",20,"bold"),bg="lightblue")
        self.lbl_total_doc.place(x=760,y=65,width=230,height=200)

        self.lbl_total_other=Label(Frame1,bd=2,relief=RAISED,text="Total Extra Files\n250",image=self.other_icon,compound=TOP,font=("times new roman",20,"bold"),bg="lightblue")
        self.lbl_total_other.place(x=1010,y=65,width=230,height=200)
        

        #-------------D---------------

        lbl_status=Label(self.root,text="STATUS",font=("times new roman", 25,), bg="white").place(x=50,y=600)
        self.lbl_st_total=Label(self.root,text="TOTAL: 250",font=("times new roman", 19,), bg="white",fg="green")
        self.lbl_st_total.place(x=300,y=605)

        self.lbl_st_move=Label(self.root,text="MOVED: 200",font=("times new roman", 19,), bg="white",fg="green")
        self.lbl_st_move.place(x=500,y=605)

        self.lbl_st_left=Label(self.root,text="REMAINING: 50",font=("times new roman", 19,), bg="white",fg="red")
        self.lbl_st_left.place(x=700,y=605)


        #------Button-----


        self.btn_clear=Button(self.root,text="Clear",font=("times new roman", 15,"bold"),bg="grey",fg="white",activebackground="grey",cursor="hand2", activeforeground="white")
        self.btn_clear.place(x=950,y=600,height=45,width=150)
        self.btn_start=Button(self.root,text="Start",font=("times new roman", 15,"bold"),bg="green",fg="white",activebackground="grey",cursor="hand2", activeforeground="white")
        self.btn_start.place(x=1150,y=600,height=45,width=150)
    

    def browse_fn(self):
        op=filedialog.askdirectory(title="SELECT THE FOLDER FOR SORTING")
        if op!=None:
            #print(op)---just to check if it was working
            self.var_foldername.set(str(op))
    

root = Tk()
obj = Sorting_App(root)
root.mainloop()

