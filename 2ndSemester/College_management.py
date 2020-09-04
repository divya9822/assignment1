def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime('%H:%M:%S')
        addeddate = time.strftime('%d/%m/%Y')
        try:
            strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notifications','ID {} Name {} Added Successfully.. Do you want to clear the form?'.format(id,name),
                                            parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notifications','ID already exist try another ID...',parent=addroot)
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry("800x500+220+200")
    addroot.title('College Management System')
    addroot.config(bg='lightsteelblue')
    #----------------------------------------------------- ADD PLAYERS LABEL
    idlabel = Label(addroot,text='Enter ID:',fg='white',bg='steelblue',font=('arial',20,'bold'),relief=GROOVE,borderwidth=4,
                      width=9,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot,text='Enter Name:',fg='white',bg='steelblue',font=('arial',20,'bold'),relief=GROOVE,borderwidth=4,
                      width=11,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(addroot,text='Enter Mobile:',fg='white',bg='steelblue',font=('arial',20,'bold'),relief=GROOVE,borderwidth=4,
                      width=13,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(addroot,text='Enter Email:',fg='white',bg='steelblue',font=('arial',20,'bold'),relief=GROOVE,borderwidth=4,
                      width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(addroot,text='Enter Address:',fg='white',bg='steelblue',font=('arial',20,'bold'),relief=GROOVE,borderwidth=4,
                      width=14,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(addroot,text='Enter Gender:',fg='white',bg='steelblue',font=('arial',20,'bold'),relief=GROOVE,borderwidth=4,
                      width=13,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(addroot,text='Enter D.O.B:',fg='white',bg='steelblue',font=('arial',20,'bold'),relief=GROOVE,borderwidth=4,
                      width=12,anchor='w')
    doblabel.place(x=10,y=370)

    #-------------------------------------------------------- ADD PLAYERS ENTRY
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()


    identry = Entry(addroot,font=('Arial',15,'bold'),fg='white',bg='steelblue',bd=5,width=27,textvariable=idval)
    identry.place(x=400,y=10)

    nameentry = Entry(addroot,font=('Arial',15,'bold'),fg='white',bg='steelblue',bd=5,width=27,textvariable=nameval)
    nameentry.place(x=400,y=70)

    mobileentry = Entry(addroot,font=('Arial',15,'bold'),fg='white',bg='steelblue',bd=5,width=27,textvariable=mobileval)
    mobileentry.place(x=400,y=130)

    emailentry = Entry(addroot,font=('Arial',15,'bold'),fg='white',bg='steelblue',bd=5,width=27,textvariable=emailval)
    emailentry.place(x=400,y=190)

    addressentry = Entry(addroot,font=('Arial',15,'bold'),fg='white',bg='steelblue',bd=5,width=27,textvariable=addressval)
    addressentry.place(x=400,y=250)

    genderentry = Entry(addroot,font=('Arial',15,'bold'),fg='white',bg='steelblue',bd=5,width=27,textvariable=genderval)
    genderentry.place(x=400,y=310)

    dobentry = Entry(addroot,font=('Arial',15,'bold'),fg='white',bg='steelblue',bd=5,width=27,textvariable=dobval)
    dobentry.place(x=400,y=370)
    #----------------------------------------------------------- ADD SUBMIT BUTTON
    submitbtn = Button(addroot,text="Add Student",font=('arial', 15,'bold'),fg='white',bg='steelblue',width=20,bd=5,
                       activebackground='lightsteelblue',activeforeground='white',
                       command=submitadd)
    submitbtn.place(x=225,y=435)

    addroot.mainloop()

####################################################################################################################################

def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime('%d/%m/%Y')
        if(id != ''):
            strr = 'select * from studentdata where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(name != ''):
            strr = 'select * from studentdata where name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(mobile != ''):
            strr = 'select * from studentdata where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(email != ''):
            strr = 'select * from studentdata where email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(address != ''):
            strr = 'select * from studestudent where address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(gender != ''):
            strr = 'select * from studentdata where gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(dob != ''):
            strr = 'select * from studentdata where dob=%s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(addeddate != ''):
            strr = 'select * from studentdata where addeddate=%s'
            mycursor.execute(strr,(addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry("800x570+220+200")
    searchroot.title('College Management System')
    searchroot.config(bg='lightsteelblue')
    # ----------------------------------------------------- ADD PLAYERS LABEL
    idlabel = Label(searchroot, text='Enter ID:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE, borderwidth=4,
                        width=9, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text='Enter Name:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE,
                          borderwidth=4,
                          width=11, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text='Enter Mobile:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE,
                            borderwidth=4,
                            width=13, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text='Enter Email:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE,
                           borderwidth=4,
                           width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text='Enter Address:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE,
                             borderwidth=4,
                             width=14, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text='Enter Gender:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE,
                            borderwidth=4,
                            width=13, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text='Enter D.O.B:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE,
                         borderwidth=4,
                         width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(searchroot, text='Enter Date:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE,
                         borderwidth=4,
                         width=11, anchor='w')
    datelabel.place(x=10, y=430)

    # -------------------------------------------------------- ADD PLAYERS ENTRY
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=idval)
    identry.place(x=400, y=10)

    nameentry = Entry(searchroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=nameval)
    nameentry.place(x=400, y=70)

    mobileentry = Entry(searchroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=mobileval)
    mobileentry.place(x=400, y=130)

    emailentry = Entry(searchroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=emailval)
    emailentry.place(x=400, y=190)

    addressentry = Entry(searchroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=addressval)
    addressentry.place(x=400, y=250)

    genderentry = Entry(searchroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=genderval)
    genderentry.place(x=400, y=310)

    dobentry = Entry(searchroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=dobval)
    dobentry.place(x=400, y=370)

    dateentry = Entry(searchroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=dateval)
    dateentry.place(x=400, y=430)
    # ----------------------------------------------------------- ADD SUBMIT BUTTON
    submitbtn = Button(searchroot, text="Search", font=('arial', 15,'bold'),fg='white',bg='steelblue', width=20, bd=5, activebackground='grey',
                           activeforeground='white',
                           command=search)
    submitbtn.place(x=225, y=500)

    searchroot.mainloop()

#################################################################################################################################

def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','ID {} is deleted successfully...'.format(pp))
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)

#################################################################################################################################

def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications','ID Updated Sucessfully...'.format(id),parent=updateroot)
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)



    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry("800x610+220+200")
    updateroot.title('College Management System')
    updateroot.config(bg='lightsteelblue')
    # ----------------------------------------------------- ADD PLAYERS LABEL
    idlabel = Label(updateroot, text='Enter ID:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE, borderwidth=4,
                        width=9, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Enter Name:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE,
                          borderwidth=4,
                          width=11, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Enter Mobile:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE,
                            borderwidth=4,
                            width=13, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Enter Email:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE,
                           borderwidth=4,
                           width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text='Enter Address:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE,
                             borderwidth=4,
                             width=14, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text='Enter Gender:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE,
                            borderwidth=4,
                            width=13, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text='Enter D.O.B:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE,
                         borderwidth=4,
                         width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Enter Date:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE,
                         borderwidth=4,
                         width=11, anchor='w')
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text='Enter Time:',fg='white',bg='steelblue', font=('arial', 20,'bold'), relief=GROOVE,
                         borderwidth=4,
                         width=11, anchor='w')
    timelabel.place(x=10, y=490)

    # -------------------------------------------------------- ADD PLAYERS ENTRY
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=idval)
    identry.place(x=400, y=10)

    nameentry = Entry(updateroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=nameval)
    nameentry.place(x=400, y=70)

    mobileentry = Entry(updateroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=mobileval)
    mobileentry.place(x=400, y=130)

    emailentry = Entry(updateroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=emailval)
    emailentry.place(x=400, y=190)

    addressentry = Entry(updateroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=addressval)
    addressentry.place(x=400, y=250)

    genderentry = Entry(updateroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=genderval)
    genderentry.place(x=400, y=310)

    dobentry = Entry(updateroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=dobval)
    dobentry.place(x=400, y=370)

    dateentry = Entry(updateroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=dateval)
    dateentry.place(x=400, y=430)

    timeentry = Entry(updateroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5, width=27, textvariable=timeval)
    timeentry.place(x=400, y=490)
    # ----------------------------------------------------------- ADD SUBMIT BUTTON
    submitbtn = Button(updateroot, text="Update", font=('arial', 15,'bold'),fg='white',bg='steelblue', width=20, bd=5, activebackground='grey',
                           activeforeground='white',
                           command=update)
    submitbtn.place(x=225, y=545)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()

 #################################################################################################################################

def showstudent():
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)

##################################################################################################################################

def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtiime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        dob.append(pp[6]),addeddate.append(pp[7]),addedtiime.append(pp[8])
    dd = ['ID','Name','Mobile','Email','Address','Gender','D.O.B.','Added Date','Added Time']
    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtiime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications','Student Data is Saved {}'.format(paths))

def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you really want to exit?')
    if(res==True):
        root.destroy()

######################################################################################################################## CONNECTION_OF_DATABASE

def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Nottifications','Data is Incorrect please try again',parent=dbroot)
            return
        try:
            strr = 'Create Database collegemanagementsystem'
            mycursor.execute(strr)
            strr = 'Use collegemanagementsystem'
            mycursor.execute(strr)
            strr = 'create table studentdata(id int,name varchar(60),mobile varchar(20),email varchar(30),address varchar(100),gender varchar(50),dob varchar(20),date varchar(20),time varchar(20))'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Database is created, Now you are connected...', parent=dbroot)
        except:
            strr = 'Use collegemanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are Connected to the Database...',parent=dbroot)
            dbroot.destroy()

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('800x250+800+230')
    dbroot.config(bg='lightsteelblue')
    #----------------------------------------------CONNECT_db LABELS
    hostlabel = Label(dbroot,text="Enter Host:",fg='white',bg='steelblue',font=('arial',20,'bold'),relief=GROOVE,borderwidth=4,
                      width=9,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot, text="Enter User:",fg='white',bg='steel blue', font=('arial', 20,'bold'), relief=GROOVE, borderwidth=4,
                    width=9,anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Enter Password:",fg='white',bg='steel blue', font=('arial', 20,'bold'), relief=GROOVE, borderwidth=4,
                    width=13,anchor='w')
    passwordlabel.place(x=10, y=130)

    #-----------------------------------------------CONNECT_db ENTRY
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('Arial',15,'bold'),fg='white',bg='steelblue',bd=5,width=27,textvariable=hostval)
    hostentry.place(x=400,y=10)

    userentry = Entry(dbroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5,width=27, textvariable=userval)
    userentry.place(x=400, y=70)

    passwordentry = Entry(dbroot, font=('Arial', 15,'bold'),fg='white',bg='steelblue', bd=5,width=27, textvariable=passwordval,show='*')
    passwordentry.place(x=400, y=130)

    #-------------------------------------------------CONNECT_db_BUTTON
    submitbutton = Button(dbroot,text="Connect",font=('arial', 15,'bold'),fg='white',bg='steel blue',width=20,bd=5,activebackground='lightsteelblue',
                          activeforeground='white',command=submitdb)
    submitbutton.place(x=225,y=190)
    dbroot.mainloop()

###########################################################################################################################################

def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200,tick)

def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count = -1
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
    count += 1
    SliderLabel.after(200,IntroLabelTick)

##############################################################################################################################################

from tkinter import*
from tkinter import Toplevel,messagebox,filedialog
from tkinter .ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
root = Tk()
root.title('College Management System')
root.config(bg='lightsteelblue')
root.geometry('1400x700+200+50')

###############################################################################################   FRAMES
#------------------------------------------------------------------ DATAENTRY FRAMES

DataEntryFrame = Frame(root,bg='steelblue',relief=RIDGE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
frontlabel = Label(DataEntryFrame,text='Namaste',width=30,font=('arial',30,'bold'),fg='white',bg='steelblue')
frontlabel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text='1. Add Students',width=25,font=('arial',15,'bold'),fg='white',bg='steelblue',bd=6,
                activebackground='lightsteelblue',relief=RIDGE,activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search Students',width=25,font=('arial',15,'bold'),fg='white',bg='steelblue',bd=6,
                activebackground='lightsteelblue',relief=RIDGE,activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='3. Update Students',width=25,font=('arial',15,'bold'),fg='white',bg='steelblue',bd=6,
                activebackground='lightsteelblue',relief=RIDGE,activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='4. Show All Students',width=25,font=('arial',15,'bold'),fg='white',bg='steelblue',bd=6,
                activebackground='lightsteelblue',relief=RIDGE,activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='5. Delete Students',width=25,font=('arial',15,'bold'),fg='white',bg='steelblue',bd=6,
                activebackground='lightsteelblue',relief=RIDGE,activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6. Export Data',width=25,font=('arial',15,'bold'),fg='white',bg='steelblue',bd=6,
                activebackground='lightsteelblue',relief=RIDGE,activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7. Exit',width=25,font=('arial',15,'bold'),fg='white',bg='steelblue',bd=6,
                activebackground='lightsteelblue',relief=RIDGE,activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)

#------------------------------------------------------------------ SHOW DATA FRAMES

ShowDataFrame = Frame(root,bg='steelblue',relief=RIDGE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=835,height=600)

#------------------------------------------------------------------
style =ttk.Style()
style.configure('Treeview.Heading',font=('arial',15,'bold'),foreground='steelblue')
style.configure('Treeview',font=('arial',10,'bold'),foreground='steelblue',background='steelblue',bg='steelblue')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,columns=('Student ID','Name','Mobile No','Email','Address','Gender','D.O.B.','Added Date','Added Time'),
                        yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Student ID',text='Student ID')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B.',text='D.O.B.')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')

studenttable['show'] = 'headings'

studenttable.column('Student ID',width=200)
studenttable.column('Name',width=180)
studenttable.column('Mobile No',width=170)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=120)
studenttable.column('D.O.B.',width=120)
studenttable.column('Added Date',width=200)
studenttable.column('Added Time',width=200)

studenttable.pack(fill=BOTH,expand=1)


###############################################################################################   SLIDER

ss='Welcome To College Management System'
count=0
text=''

###############################################################################################

SliderLabel = Label(root,text=ss,font=('arial',20,'bold'),relief=RIDGE,borderwidth=4,width=35,bg='steelblue',fg='white')
SliderLabel.place(x=280,y=0)
IntroLabelTick()

###############################################################################################   CLOCK

clock = Label(root,font=('arial',14,'bold'),relief=RIDGE,borderwidth=4,bd=6,bg='steelblue',fg='white')
clock.place(x=0,y=0)
tick()

###############################################################################################    CONNECT_TO_DATABASE_BUTTON

connectbutton = Button(root,text='Connect To Database',width=23,font=('arial',15,'bold'),relief=RIDGE,
                       bd=6,borderwidth=4,activebackground='lightsteelblue',activeforeground='white',bg='steelblue',fg='white',command=Connectdb)
connectbutton.place(x=1030,y=0)
root.mainloop()