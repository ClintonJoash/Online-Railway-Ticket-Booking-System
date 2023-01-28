from tkinter import *
from PIL import Image, ImageTk
import json
import tkinter.font as tkFont
from tkinter import ttk
import datetime
from tkcalendar import DateEntry
from datetime import date
import tkinter.messagebox as m

import re

import cx_Oracle
con = cx_Oracle.connect('YOUR ORACLE LOGIN AND PASSWORD')
cursor = con.cursor()

Login_tracker=0
past={}
try:
    fd=open("hist.json")
    rec=json.load(fd)
except:
    rec={}
#print(rec)
#to open the dataset
# f=open("hist.json")
# rec=json.load(f)
fd=open("trainslarge.json")
dct=json.load(fd)

#home window
mainWindow = Tk() #initialize
mainWindow.title("Login")
mainWindow.geometry("4500x3000")
canvas=Canvas(mainWindow, width=4500, height=3000,bg="white")
canvas.place(x=0,y=0)

#applying image of train
image1 = Image.open("tain2.jpg")
image1 = image1.resize((930,495), Image.ANTIALIAS)
test1 = ImageTk.PhotoImage(image1)
label1 = Label(image=test1)
label1.image = test1
label1.place(x = 698, y = 192)

#logo 
image2 = Image.open("IRTBS (1).png")
image2 = image2.resize((190,188), Image.ANTIALIAS)
test2 = ImageTk.PhotoImage(image2)
label2 = Label(image=test2)
label2.image = test2
label2.place(x = 0, y = 0)

#making 2 rectangles for sched background
canvas.create_rectangle(190,120,2000,60,fill="red")
canvas.create_rectangle(190,190,2000,120,fill="light blue")

#heading
white=Label(text="               INDIAN RAILWAYS TICKET BOOKING SYSTEM                 ",fg='black',bg="white",font=("Times New Roman", 32, "bold",'underline'))
white.place(x=192,y=10)

#registration page
def Reg():
    def get_reg_info():
        EMAIL=eemail.get()
        USERNAME=euser.get()
        FNAME=ef_name.get()
        LNAME=el_name.get()
        PASSWORD=epassword.get()
        CONFIRMPASS=econfirm.get()
        AADHAR=eaadhar.get()
        PHONE=ephno.get()
        if(len(AADHAR) != 12):
            reg.withdraw()
            m.showerror(message="Please enter a valid aadhar number")
            reg.deiconify()
            return
        
        if(len(PHONE) != 10):
            reg.withdraw()
            m.showerror(message="Please enter a valid phone number")
            reg.deiconify()
            return

        pattern="[a-zA-z0-9]+@[a-zA-z]+\.(com|edu|net|co.in)"
        if(not(re.search(pattern,EMAIL))):
            reg.withdraw()
            m.showerror(message="Please enter a valid email")
            reg.deiconify()
            return
        if(not (FNAME.isalpha() and LNAME.isalpha())):
            reg.withdraw()
            m.showerror(message="Name should contain only alphabets")
            reg.deiconify()
            return 
        
        try:
            if(PASSWORD==CONFIRMPASS):
                con = cx_Oracle.connect('YOUR ORACLE LOGIN AND PASSWORD')
                cursor = con.cursor()
                cursor.execute("insert into register(email, username, f_name, l_name,password) values(:1,:2,:3,:4,:5)",(EMAIL,USERNAME,FNAME,LNAME,PASSWORD))
                print("entry made")
                m.showinfo(message="Registration successful please login to continue")
                reg.destroy()
                cursor.close()
                con.commit()
                con.close()
            else:
                reg.withdraw()
                m.showerror(message="Password does not match! ")
                reg.deiconify()
                euser.delete(0,END)
                epassword.delete(0,END)
                ef_name.delete(0,END)
                el_name.delete(0,END)
                econfirm.delete(0,END)
                eemail.delete(0,END)
                reg_done=Button(reg, text="DONE",font=("Times New Roman", 28, "bold"),bg='black',fg="white",command=get_reg_info)
                reg_done.place(x=190,y=500)
        except cx_Oracle.DatabaseError as e:
            e1=str(e)
            #print(e1)
            if (e1=="ORA-00001: unique constraint (USERNAME.PK) violated"):
                #print('yes')
                reg.withdraw()
                m.showerror(message="Email already exists please select another one")
                reg.deiconify()

            if(e1=="ORA-00001: unique constraint (USERNAME.UNI) violated"):
                reg.withdraw()
                m.showerror(message="Username already exists please select another one")
                reg.deiconify()

             
            


    reg=Tk()
    reg.title("Registration")
    reg.geometry("600x700+500+80")
    #reg.eval('tk::PlaceWindow . center')
    reg.config(bg="white")
    user_name=Label(reg, text="Username ",bg="white",fg="black",font=("Times New Roman", 18, "bold"))
    email=Label(reg, text="Email id  ",bg="white",fg="black",font=("Times New Roman", 18, "bold"))
    f_name=Label(reg, text="First Name ",bg="white",fg="black",font=("Times New Roman", 18, "bold"))
    l_name=Label(reg, text="Last Name ",bg="white",fg="black",font=("Times New Roman", 18, "bold"))
    password=Label(reg, text="Password ",bg="white",fg="black",font=("Times New Roman", 18, "bold"))
    confirmpassword=Label(reg, text="Confirm Password ",bg="white",fg="black",font=("Times New Roman", 18, "bold"))
    aadhar=Label(reg, text="Aadhar number ",bg="white",fg="black",font=("Times New Roman", 18, "bold"))
    phno=Label(reg, text="Contact number ",bg="white",fg="black",font=("Times New Roman", 18, "bold"))
    user_name.place(x=80,y=50)
    email.place(x=80,y=100)
    f_name.place(x=80,y=150)
    l_name.place(x=80,y=200)
    password.place(x=80,y=250)
    confirmpassword.place(x=80,y=300)
    aadhar.place(x=80,y=350)
    phno.place(x=80,y=400)

    euser=Entry(reg,font=18)
    eemail=Entry(reg,font=18)
    ef_name=Entry(reg,font=18)
    el_name=Entry(reg,font=18)
    epassword=Entry(reg,font=18)
    econfirm=Entry(reg,font=18)
    eaadhar=Entry(reg,font=18)
    ephno=Entry(reg,font=18)
    euser.place(x=300,y=50)
    eemail.place(x=300,y=100)
    ef_name.place(x=300,y=150)
    el_name.place(x=300,y=200)
    epassword.place(x=300,y=250)
    econfirm.place(x=300,y=300)
    eaadhar.place(x=300,y=350)
    ephno.place(x=300,y=400)
    reg_done=Button(reg, text="Register",font=("Times New Roman", 25, "bold"),bg='red',fg="white",command=get_reg_info)
    reg_done.place(x=190,y=600)

#login page
def Log():
    def get_log_info():
        PASSWORD=epassword.get()
        global USERNAME
        USERNAME=euser.get()
        #print(USERNAME,PASSWORD)
        con1 = cx_Oracle.connect('YOUR ORACLE LOGIN AND PASSWORD')
        cursor1 = con1.cursor()
        con2 = cx_Oracle.connect('YOUR ORACLE LOGIN AND PASSWORD')
        cursor2 = con2.cursor()
        cursor1.execute("select username from register")
        cursor2.execute("select password from register")
        e = []
        p = []
        #print(cursor2)
        for i in cursor1:
            
           
            #print(i)
            e.extend(i)
        for j in cursor2:
            
           

            #print(j)
            p.extend(j)
        #print(e)
        #print(e,p)
        k = len(e)
        i = 0
        while i<k:
            ##print("88",e[i],p[i])
            if e[i] == USERNAME and p[i] == PASSWORD:
                print("Login Is Done")
                global Login_tracker
                Login_tracker=1
                log.destroy()
                m.showinfo(message="Login successful")
                #After_log(USERNAME)
                return 
                
            i += 1
        else:
            #print("77",e[i-1],p[i-1])
            print("Something went wrong")
            log.withdraw()
            m.showerror(message="Username and password don't match")
            log.deiconify()
            euser.delete(0,END)
            epassword.delete(0,END)
            return 



    log=Tk()
    log.title("Login")
    log.geometry("500x400+500+250")
    #reg.eval('tk::PlaceWindow . center')
    log.config(bg="white")
    user_name=Label(log, text="Username ",bg="white",fg="black",font=("Times New Roman", 18, "bold"))    
    password=Label(log, text="Password ",bg="white",fg="black",font=("Times New Roman", 18, "bold"))
    password.place(x=30,y=200)
    user_name.place(x=30,y=100)    
    epassword=Entry(log,font=18,show="*")
    epassword.place(x=250,y=200)
    euser=Entry(log,font=18)
    euser.place(x=250,y=100)
    LOG_done=Button(log, text="Login",font=("Times New Roman", 25, "bold"),bg='red',fg="white",command=get_log_info)
    LOG_done.place(x=160,y=300)

def schedule():

    tname=[]
    tserial=[]
    for k in range(len(dct)):
        dic=dct[k]
        try:
            tname.append(dic["trainName"])
            tserial.append(dic["trainNumber"])
        except:
            continue
    tname=list(set(tname))
    tname.sort()
    tserial=list(set(tserial))
    tserial.sort()

    def filter_no(event):
        name=[]
        global train_no
        #print(event.char)
        train_no=train_no+event.char
        if("keysym=BackSpace" in str(event)):
            train_no=train_no[0:-2]
        for stat in tserial:
            if( stat.startswith(train_no.upper())):
                name.append(stat)
        Train_num['values']=tuple(name)
        Train_num.place(x=250,y=150)

    def filter_train(event):
        name_train=[]
        global train
        train=train+event.char
        #print(train)
        if("keysym=BackSpace" in str(event)):
            train=train[0:-2]
        for stat in tname:
            if(train.upper() in stat):
                name_train.append(stat)
        train_naming['values']=tuple(name_train)
        train_naming.place(x=250,y=50)
    def sel_name(e):
        for k in range(len(dct)):
            dic=dct[k]
            try:
                #print(Train_num.get())
                if(Train_num.get()==dic["trainNumber"]):
                    #print("meow")
                    nam=dic["trainName"]
                    #print(nam)
                    names=[nam]
                    train_naming.config(value=names)
                    train_naming.current(0)
            except: continue
    def sel_num(e):
        for k in range(len(dct)):
            dic=dct[k]
            try:
                #print(dic["trainName"])
                if(train_naming.get()==dic["trainName"]):
                    num=dic["trainNumber"]
                    #print(num)
                    numb=[num]
                    Train_num.config(value=numb)
                    Train_num.current(0)
            except: continue

    def tell_sched():
        
        number=Train_num.get()
        name=train_naming.get()
        sched.destroy()
        for k in range(len(dct)):
            dic=dct[k]
            try:
                #print(dic["trainNumber"])
                if( name==dic["trainName"] and number==dic["trainNumber"]):
                    
                    lst=dic["stationList"]
                    #print("meow")
                    train_info=Tk()
                    train_info.geometry("800x700+350+70")
                    train_info.title(name+ " Train schedule")

                    #creating a page with scrollbar
                    main_frame=Frame(train_info)
                    main_frame.pack(fill=BOTH,expand=1)
                    my_canvas=Canvas(main_frame,bg="white")
                    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
                    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
                    my_scrollbar.pack(side=RIGHT,fill=Y)
                    my_canvas.configure(yscrollcommand=my_scrollbar.set)
                    my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                    second_frame=Frame(my_canvas,bg="white")
                    my_canvas.create_window((0,0),window=second_frame,anchor='nw',height=len(lst)*200+200,width=700)
                    
                    n=1
                    c=0
                    can=Canvas(second_frame,bg='white',width=700,height=len(lst)*200+200)
                    can.place(x=0,y=0)
                    trainHeading=Label(second_frame,text="Train : "+name,bg="white",fg="black",font=("Times New Roman",23,'bold')).place(x=30,y=20)
                    for i in lst:
                        try:
                            
                            dept=int(i["departureTime"][0:2])
                            arr=int(i["arrivalTime"][0:2])
                            
                            
                            #print("o")
                            can.create_line(0,80+c,700,80+c,width=3)
                            #print("o")
                            stno=Label(second_frame,text=("Station number : %(n)s"%{'n':n}),bg='white',fg='black',font=("Times New Roman",18,'bold')).place(x=30,y=100+c)
                            #print("o")
                            stcode=Label(second_frame,text=("Station code: "+i["stationCode"]),bg='white',fg='black',font=("Times New Roman",18,'bold')).place(x=30,y=140+c)
                            stname=Label(second_frame,text=("Station name: "+i["stationName"]),bg='white',fg='black',font=("Times New Roman",18,'bold')).place(x=330,y=140+c)
                            dept_time=Label(second_frame,text=("Departure time: "+i["departureTime"]),bg='white',fg='black',font=("Times New Roman",18,'bold')).place(x=30,y=180+c)
                            arr_time=Label(second_frame,text=("Arrival time: "+i["arrivalTime"]),bg='white',fg='black',font=("Times New Roman",18,'bold')).place(x=330,y=180+c)
                            dc=Label(second_frame,text=("Day count: "+i["dayCount"]),bg='white',fg='black',font=("Times New Roman",18,'bold')).place(x=30,y=220+c)
                            
                            #print("o")
                            c=c+210
                            n=n+1
                        except Exception as e : 
                            #print(e)
                            continue

            
            except: continue



        
            
    sched=Tk()
    sched.title("Train Schedule")
    sched.geometry("500x400+500+250")
    sched.config(bg="white")
    bigfont = tkFont.Font(family="Helvetica",size=18)
    sched.option_add("*TCombobox*Listbox*Font", bigfont)
    train_naming=ttk.Combobox(sched,width = 15,height=12,font=("Times New Roman", 18, "bold"))
    train_naming['values']=tuple(tname)
    train_naming.place(x=250,y=50)
    global train
    train=""
    train_naming.bind("<Key>",filter_train)
    Train_num=ttk.Combobox(sched,width = 15,height=12,font=("Times New Roman", 18, "bold"))
    Train_num['values']=tuple(tserial)
    Train_num.place(x=250,y=150)
    global train_no
    train_no=""
    Train_num.bind("<Key>",filter_no)
    Train_name=Label(sched,text="TRAIN NAME",fg="black",bg="white",font=("Times New Roman", 18, "bold"))
    Train_name.place(x=30,y=50)
    Train_no=Label(sched,text="TRAIN NUMBER",fg="black",bg="white",font=("Times New Roman", 18, "bold"))
    Train_no.place(x=30,y=150)
    Train_num.bind('<<ComboboxSelected>>',sel_name)
    train_naming.bind('<<ComboboxSelected>>',sel_num)
    
    check_sched=Button(sched,width=15,text="CHECK",fg="white",bg="RED",font=("Times New Roman",14,'bold'),command=tell_sched)
    check_sched.place(x=250,y=300)

def book1():
    def travelhist(past):
        def re_book(details):
            def done():
                conf.destroy()
                m.showinfo(message="BOOKING CONFIRMED")
            pasth.destroy()
            conf=Tk()
            conf.geometry("900x500")
            conf.configure(bg='white')
            c=0
            for i in details:
                det=Label(conf,text=str(i)+" : "+str(details[i]),fg='black',bg='white',font=("Times New Roman",18,'bold')).place(x=10,y=10+c)
                c=c+60
            confirmbook=Button(conf,text="BOOK",font=("Times New Roman",18,'bold'),fg='white',bg='red',command=done).place(x=700,y=400)


            

        pasth=Tk()
        pasth.geometry("4500x3000")
        canvas=Canvas(pasth,width=4500,height=3000,bg='white')
        canvas.place(x=0,y=0)
        c=0
        col=["TRAIN NUMBER","TRAIN NAME","STATION TO","STATION FROM","ARRIVES","DEPARTS",'DAYS COUNT','''LAST TRAVEL DATE''']

        main_frame=Frame(pasth)
        main_frame.pack(fill=BOTH,expand=1)
        my_canvas=Canvas(main_frame,bg="white")
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
        my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        second_frame=Frame(my_canvas,bg="white")
        my_canvas.create_window((0,0),window=second_frame,anchor='nw',height=len(past)*200+200,width=4500)
        can3=Canvas(second_frame,width=4500,height=len(past)*200+200,bg='white')
        can3.place(x=0,y=0)
        det=rec[USERNAME]
        for i in det.values():
            #print(i))
            for k in i:
                #print('ohno',k)
                
                label=Label(second_frame,text=(k+" : "+str(i[k])),bg='white',font=("Times New Roman",18,'bold'))
                #print(i)
                if(k in ["TRAIN NUMBER", "STATION TO","ARRIVES","DAYS COUNT"]):
                    label.place(x=520,y=10+c)
                    
                else:
                    label.place(x=10,y=10+c)
                    c=c+50
            datelab=Label(second_frame,text='NEW DATE : ', bg='white',fg='black',font=("Times New Roman",18,'bold')).place(x=900,y=c-40)
            cal = DateEntry(second_frame, width=15,height=12,font=18, background='light green', foreground='black', borderwidth=2,mindate=today,date_pattern='dd/mm/yyyy')
            cal.place(x=1050, y=c-40)
            rebook=Button(second_frame,text='REBOOK',fg='white',bg='red',font=('Times New Roman',18,'bold'),command=lambda i=i: re_book(i)).place(x=1300,y=c-50)
            can3.create_line(0,c,4500,c)
            print((i["TRAIN NAME"]))

    if(Login_tracker==0):
            Log()
    else:
        travelhist(past)


    
def book(old_new,hist):
    def done():
        conf.destroy()
        #train_list.withdraw()
        m.showinfo(message="BOOKING CONFIRMED")
        #train_list.deiconify()
        
    if(Login_tracker==0):
        Log()
    if(Login_tracker==1):
        #print(44,old_new)

        
        try:
            
            past[len(past)+1]=hist
            rec[USERNAME][len(rec[USERNAME])+1]=hist
        except:
            past[1]=hist
            rec[USERNAME]={1:hist}

            
        
        # print(rec)
        fs=json.dumps(rec)
        ff=open('hist.json','w') #writing the new record back in file
        ff.write(fs)
        ff.close()
        conf=Tk()
        conf.geometry("900x500")
        conf.configure(bg='white')
        c=0
        for i in hist:
            det=Label(conf,text=str(i)+" : "+str(hist[i]),fg='black',bg='white',font=("Times New Roman",18,'bold')).place(x=10,y=10+c)
            c=c+60
        confirmbook=Button(conf,text="BOOK",font=("Times New Roman",18,'bold'),fg='white',bg='red',command=done).place(x=700,y=400)

    
    
    

#red tab
login = Button(text="LOGIN", fg='white', bg='red',relief="flat",cursor='hand2',font=("Times New Roman", 19, "bold",'underline'),command=Log)
login.place(x=1050,y=68)
register= Button(text="REGISTER", fg='white', bg='red',relief="flat",cursor='hand2',font=("Times New Roman", 19, "bold",'underline'),command=Reg)
register.place(x=1300,y=68)
home = Button(text="HOME", fg='white', bg='red',relief="flat",cursor='hand2',font=("Times New Roman", 19, "bold",'underline'))
home.place(x=250,y=68)
grievance = Button(text="GRIEVANCE", fg='white', bg='red',relief="flat",cursor='hand2',font=("Times New Roman", 19, "bold",'underline'))
grievance.place(x=450,y=68)
about= Button(text="ABOUT US", fg='white', bg='red',relief="flat",cursor='hand2',font=("Times New Roman", 19, "bold",'underline'))
about.place(x=740,y=68)


#blue tab
trainSchedule= Button(text="TRAIN SCHEDULE", fg='black', bg='light blue',relief="flat",cursor='hand2',font=("Times New Roman", 19, "bold",'underline'),command=schedule)
trainSchedule.place(x=250,y=130)
aboutIR= Button(text="ABOUT INDIAN RAILWAYS", fg='black', bg='light blue',relief="flat",cursor='hand2',font=("Times New Roman", 19, "bold",'underline'))
aboutIR.place(x=650,y=130)
old_new=0
pastTravel= Button(text="TRAVELLING HISTORY", fg='black', bg='light blue',relief="flat",cursor='hand2',font=("Times New Roman", 19, "bold",'underline'),command=lambda old_new=old_new: book1())
pastTravel.place(x=1150,y=130)


#from and to box
canvas.create_rectangle(0,690,700,190,fill='light green')
canvas.create_rectangle(70,680,600,200,fill='white')

heading=Label(text='CHECK AVAILABLE TRAINS',fg='black',bg='white',font=("Times New Roman", 23, "bold"))
heading.place(x=110,y=220)
names=[]
for l in range(len(dct)):
    dic=dct[l]
    try:
        lst=dic["stationList"]
        for i in lst:
            if(i['stationName'] not in names):
                names.append(i['stationName'])
            else:
                continue
    except:
        continue
names.sort()

#to filter station names
def filter_to(event):
            name=[]
            global enter
            enter=enter+event.char
            if("keysym=BackSpace" in str(event)):
                enter=enter[0:-2]
            for stat in names:
                if(enter.upper() in stat):
                    name.append(stat)
            #print(name)
            Station_to['values']=tuple(name)
            Station_to.place(x=300,y=430)

#to filter station name
def filter_from(event):
    name=[]
    global entered
    entered=entered+event.char
    if("keysym=BackSpace" in str(event)):
        entered=entered[0:-2]
    for stat in names:
        if(entered.upper() in stat):
            name.append(stat)
    Station_from['values']=tuple(name)
    Station_from.place(x=300,y=340)
bigfont = tkFont.Font(family="Helvetica",size=17)
mainWindow.option_add("*TCombobox*Listbox*Font", bigfont)
Station_from=ttk.Combobox(width = 15,height=12,font=("Times New Roman", 17, "bold"))
Station_from['values']=tuple(names)
Station_from.place(x=300,y=340)
entered=""
Station_from.bind("<Key>",filter_from)
Station_to=ttk.Combobox(width = 15,height=12,font=("Times New Roman", 17,"bold"))
Station_to['values']=tuple(names)
Station_to.place(x=300,y=430)
enter=""
Station_to.bind("<Key>",filter_to)
FROM=Label(text="FROM: ",fg="black",bg="white",font=("Times New Roman", 20,'bold'))
FROM.place(x=180,y=335)
TO=Label(text="TO: ",fg="black",bg="white",font=("Times New Roman", 20,'bold'))
TO.place(x=180,y=425)
Date=Label(text="DATE: ",fg="black",bg="white",font=("Times New Roman", 20, "bold"))
Date.place(x=180,y=515)
today=date.today()
cal = DateEntry(mainWindow, width=15,height=12,font=18, background='light green', foreground='black', borderwidth=2,mindate=today,date_pattern='dd/mm/yyyy')
cal.place(x=300, y=515)
flexdate=Checkbutton(text='Date Flexible',fg="black",bg="white",font="Poppins 16 underline",height=2,width=10)
flexdate.place(x=100,y=600)

def get_info1():
    

    flag=0
    stationF=Station_from.get()
    stationT=Station_to.get()
    if(stationF==stationT):
        m.showerror(message="Please select different stations ")
        Station_from.delete(0,END)
        Station_to.delete(0,END)
        flag=1
    else:
        #print("meow")
        stationF=Station_from.get()
        stationT=Station_to.get()
        date_dept=cal.get()
        global day,month,year
        day=int(date_dept[0:2])
        month=int(date_dept[3:5])
        year=int(date_dept[6:])

    if(flag==0):
        train_list=Tk()
        train_list.geometry("700x700+400+70")
        train_list.title("Available Trains")

        #creating a page with scrollbar
        main_frame=Frame(train_list)
        main_frame.pack(fill=BOTH,expand=1)
        my_canvas=Canvas(main_frame,bg="white")
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
        my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        second_frame=Frame(my_canvas,bg="white")


        train=[]
        number=[]
        noday=[]
        dept=[]
        arriv=[]
        intDay = datetime.date(year=year, month=month, day=day).weekday()
        days = ["trainRunsOnMon", "trainRunsOnTue", "trainRunsOnWed", "trainRunsOnThu", "trainRunsOnFri", "trainRunsOnSat", "trainRunsOnSun"]
        train_day=(days[intDay])
        for k in range(len(dct)):
            dic=dct[k]
            try:
                if(dic[str(train_day)]=='Y'):
                    #print("meow")

                    lst=dic["stationList"]
                    flag1=0
                    flag2=0
                    for i in lst:
                        if(stationF==i["stationName"]):
                            
                            try:
                                checkdep=int(i["departureTime"][0:2])
                                dep=(i["departureTime"])
                                day1=int(i["dayCount"])
                                
                                flag1=1
                                
                            except: break
                            #print("meow1")
                        if(stationT==i["stationName"]):
                            
                            try:
                                checkarr=int(i["arrivalTime"][0:2])
                                arr=i["arrivalTime"]
                                day2=int(i["dayCount"])
                                
                                flag2=1
                                
                            except: break
                            #print("meow2")
                        if(flag1==1 and flag2==1):
                            
                            try:
                                if(day2-day1>=0):
                                    noday.append(day2-day1)
                                else:
                                    break
                                train.append(dic["trainName"])
                                number.append(dic["trainNumber"])
                                dept.append(dep)
                                arriv.append(arr)
                            except:
                                break
                            break
            except:
                continue
        col=len(train)
        #print(col)
        sort_dic={}
        for l in range(col):
            sort_dic[number[l]]={"train name":train[l],"day count":noday[l],"Departure time":dept[l],"Arrival time":arriv[l]}
        
        sorted_dic=sorted(sort_dic.items(), key=lambda x:x[1]['day count'])
        #print(dict(sorted_dic))
        sorted_dic=dict(sorted_dic)
        arranged_numbers=[]
        for num in sorted_dic.keys():
            arranged_numbers.append(num)


        my_canvas.create_window((0,0),window=second_frame,anchor='nw',height=col*200+200,width=700)

        colour=['light blue','white'] #alternate colouring of boxes
        colno=0
        c=0
        can3=Canvas(second_frame,width=700,height=col*200+200,bg='white')
        can3.place(x=0,y=0)
        sec=Label(second_frame,text='''LIST OF AVAILABLE TRAINS''',bd=0,font=("Times New Roman",25,'bold'),fg='black',bg='white').place(x=100,y=30)
        
        #loop to display all trains in rectangular boxes
        for a in range(col):
            can3.create_rectangle(10,350+c,680,100+c,width=2,fill=colour[colno])
            Name=Label(second_frame,text=("Train name : %(n)s"%{'n':sorted_dic[arranged_numbers[a]]["train name"]}),fg='black',bg=colour[colno],font=("Times New Roman",18))
            Name.place(x=30,y=120+c)
            Number=Label(second_frame,text=("Train number : %(n)s"%{'n':arranged_numbers[a]}),fg='black',bg=colour[colno],font=("Times New Roman",18))
            Number.place(x=30,y=160+c)
            countday=sorted_dic[arranged_numbers[a]]["day count"]
            if(countday==0):
                dispcount= "Same Day"
            else:
                dispcount=str(countday)+" Day"
            numday=Label(second_frame,text=("Number of days required : "+dispcount),fg='black',bg=colour[colno],font=("Times New Roman",18))
            numday.place(x=30,y=200+c)
            Departure=Label(second_frame,text=("Departure time  : %(n)s"%{'n':sorted_dic[arranged_numbers[a]]["Departure time"]}),fg='black',bg=colour[colno],font=("Times New Roman",18))
            Departure.place(x=30,y=240+c)
            Arrival=Label(second_frame,text=("Arrival time : %(n)s"%{'n':sorted_dic[arranged_numbers[a]]["Arrival time"]}),fg='black',bg=colour[colno],font=("Times New Roman",18))
            Arrival.place(x=30,y=280+c)
            old=0
            hist={}
            hist={"TRAIN NUMBER":arranged_numbers[a],"TRAIN NAME":sorted_dic[arranged_numbers[a]]["train name"],"STATION TO":stationT,"STATION FROM":stationF,"ARRIVES":sorted_dic[arranged_numbers[a]]["Arrival time"],"DEPARTS":sorted_dic[arranged_numbers[a]]["Departure time"],'DAYS COUNT':sorted_dic[arranged_numbers[a]]["day count"],'''LAST TRAVEL DATE''':date_dept}
            #print(hist)
            e1 = Button(second_frame,text='Book Ticket',width=10,bg='red', fg='white', font=('Arial', 18, 'bold'),command=lambda hist=hist: book(old,hist))
            e1.place(x=500,y=280+c)

            colno=0 if colno==1 else 1
            #print(train[a])
            c=c+250    
        
       
#flexdate check button
check=Button(text="CHECK",bg='light blue',fg='black',font=("Times New Roman", 20, "bold"),command=get_info1)
check.place(x=450,y=600)

#main page exit button
Exit=Button(text="EXIT",fg="black",bg="light blue",font=("Times New Roman", 21, "bold"),command=mainWindow.destroy)
Exit.place(x=1400,y=720)
mainloop()
