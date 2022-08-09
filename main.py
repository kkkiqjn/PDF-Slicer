# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 17:05:36 2022

@author: Vikas Reddy karkala
"""
# from PIL import Image, ImageTk
from tkinter import Toplevel,Label,PhotoImage,Text,Scrollbar,RIGHT,Y,Listbox,LEFT,BOTH,Button
import PyPDF2

def SlicePdf():
    
    Srcfile=src.get(1.0,"end-1c")
    Desfile=des.get(1.0,"end-1c")
    startno=int(endpage.get(1.0,"end-1c"))
    endno=int(startpage.get(1.0,"end-1c"))
    pdfsrc=open(r""+Srcfile,"rb")
    pdfreader=PyPDF2.PdfFileReader(pdfsrc)
    pdfwriter=PyPDF2.PdfFileWriter()
    for i in range(startno-1,endno):
        pageobj=pdfreader.getPage(i)
        pdfwriter.addPage(pageobj)
    writefile=open(Desfile,"wb")
    pdfwriter.write(writefile) 
    pdfsrc.close()
    writefile.close() 
    
root=Toplevel()
root.title("A automated PDF slicer")
root.attributes("-fullscreen",False)
root.config(bg="#FCFFE7")
img=PhotoImage(file="pylogo.gif")
IMG=Label(root,image=img,background="#7DCE13",borderwidth=0)
IMG.pack()
msg=Label(root,text="Welcome to Python GUI of PDF slicer")
msg.config(font=("callibri",24))
msg.pack()


    

srcmsg=Label(root,text="Enter source PDF file path")
srcmsg.config(font=("callibri",12))
srcmsg.pack(pady=20)
src=Text(root,height=1,width=40)
src.pack(pady=10)

desmsg=Label(root,text="Enter destination file name")
desmsg.config(font=("callibri",12))
desmsg.pack(pady=20)
des=Text(root,height=1,width=40)
des.pack(pady=10)

end=Label(root,text="Start page No(cover page no is 1)")
end.config(font=("callibri",12))
end.pack(pady=20)
endpage=Text(root,height=1,width=40)
endpage.pack(pady=10)


start=Label(root,text="end page no")
start.config(font=("callibri",12))
start.pack(pady=20)
startpage=Text(root,height=1,width=40)
startpage.pack(pady=10)

but=Button(root,text="Slice",command=SlicePdf)
but.pack()     
root.mainloop()
