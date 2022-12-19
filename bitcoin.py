from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import requests
import json

col1="white"
col2="#333333"
col3="black"
window=Tk()
window.title(' ')
window.geometry('320x350')
window.configure(bg=col1)

def info():
    api_link="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CINR%2CCAD"
    r=requests.get(api_link)
    dic=r.json()
    
    
    usd_value=float(dic["USD"])
    usd_formatted_value="${:,.3f}".format(usd_value)
    usd["text"]=usd_formatted_value

    euros_value=float(dic["EUR"])
    euros_formatted_value="{:,.3f}".format(euros_value)
    euros["text"]="Europe : €"+euros_formatted_value

    cad_value=float(dic["CAD"])
    cad_formatted_value="{:,.3f}".format(cad_value)
    cad["text"]="Canada : Can$"+cad_formatted_value    

    inr_value=float(dic["INR"])
    inr_formatted_value="{:,.3f}".format(inr_value)
    inr["text"]="India    : ₹"+inr_formatted_value    

    frame_body.after(1000,info)


frame_head=Frame(window,width=320,height=50,bg=col1)
frame_head.grid(row=1,column=0)

frame_body=Frame(window,width=320,height=300,bg=col2)
frame_body.grid(row=2,column=0)



image1=Image.open("./bitcoin-icon.png")
image1=image1.resize((30,30))
image1=ImageTk.PhotoImage(image1)
icon1=Label(frame_head,image=image1)
icon1.place(x=10,y=10)



name=Label(frame_head,padx="0",text="Bitcoin Price Tracker",bg=col1,fg=col3,width=16,height=1,anchor="center",font="Poppins 18")
name.place(x=50,y=11)


usd=Label(frame_body,text="$0000",width=14,height=1,font="Arial 30 bold",bg=col2,fg=col1,anchor="center")
usd.place(x=0,y=28)


euros=Label(frame_body,text="$0000",height=1,font="Arial 15 bold",bg=col2,fg=col1,anchor="center")
euros.place(x=10,y=130)


cad=Label(frame_body,text="$0000",height=1,font="Arial 15 bold",bg=col2,fg=col1,anchor="center")
cad.place(x=10,y=170)


inr=Label(frame_body,text="$0000",height=1,font="Arial 15 bold",bg=col2,fg=col1,anchor="center")
inr.place(x=10,y=210)

info()


window.mainloop()