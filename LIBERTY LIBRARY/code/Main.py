from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkcalendar import * 
from tkinter import ttk
import mysql.connector

#root things
root=Tk()
root.title("Liberty Library")
root.geometry("1536x864")
root.iconphoto(False,ImageTk.PhotoImage(file='pics\librarylogo.png'))
root.resizable(False,False)



def click_login():
    #destroying
    start_window_label.pack_forget()
    signup_button.place_forget()
    login_button.place_forget()
    dummy_loginbutton_button.place_forget()
    dummy_signupbutton_button.place_forget()
    dummy_start_window_label.pack_forget()
    dummy_if_your_admin_button.place_forget()
    if_your_admin_Button.place_forget()
    #putting label
    login_window_label.pack()

    #putting entry
    login_username_entry.place(x=650,y=370)
    login_password_entry.place(x=650,y=520)
    #putting buttons
    login_continue_button.place(x=550,y=610)
    back_button.place(x=0,y=1)


#login

def go_to_mainpage():
    new_username=login_username_entry.get()
    new_pass=login_password_entry.get()
    myconnector = mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()

    if new_username == '' or new_pass == '':
        messagebox.showwarning('Liberty Library','Dont Leave fields Empty')
    else:
        mycursor.execute(f"select count(*) from account_details where username='{new_username}'")
        result=mycursor.fetchone()
        if int(result[0])==0:
            messagebox.showwarning('Liberty Library','This Username Does Not Exist !')
            login_username_entry.delete(0,END)
            login_password_entry.delete(0,END)
        else:
            mycursor.execute(f"select* from account_details where username='{new_username}'")
            result=mycursor.fetchone()
            if result[2]==new_pass:
                myconnector.close()
                login_window_label.pack_forget()
                login_username_entry.place_forget()
                login_password_entry.place_forget()
                login_continue_button.place_forget()
                back_button.place_forget()
                borrwer_mainpage_label.pack()
                global hi_user_label
                hi_user_label=Label(root,text='Hi '+ new_username+' welcome to Liberty Library',background="#191926",fg='white',font=("Heveltica",20,"bold"),justify=LEFT,width=30,height=5)
                hi_user_label.place(x=640,y=200)
                viewbooks_button.place(x=10,y=160)
                searchbook_button.place(x=10,y=250)
                logout_borrower_button.place(x=10,y=340)
                login_username_entry.delete(0,END)
                login_password_entry.delete(0,END)
            else:
                messagebox.showwarning('Liberty Library','Wrong Password ! Please Enter Correct Password !')
                login_password_entry.delete(0,END)
     
#creating acct
def go_to_start():
    new_signup_username=signup_username_entry.get()
    new_signup_password=signup_password_entry.get()
    new_confirm_password=signup_re_password_entry.get()

    if new_signup_password=="" or new_signup_username=="" or new_confirm_password=="":
        messagebox.showwarning("Liberty Library",'Dont Leave fields Empty')
    else:
        is_username=True
        is_password=True
        if len(new_signup_password)>20 or len(new_signup_username)>30:
            is_password=False
            is_username=False
            messagebox.showwarning("Liberty Library",'Username or Password should not exceed 20 characters!')
        if new_signup_password!=new_confirm_password:
            messagebox.showwarning("Liberty Library",'Your password didn\'t match')
        else:
            if is_password and is_username:

                myconnector=mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
                mycursor=myconnector.cursor()
                mycursor.execute(f"select count(*) from account_details where username ='{new_signup_username}'")
                result=mycursor.fetchone()
                if int(result[0])>0:
                    messagebox.showwarning("Liberty Library",'Username already exist')
                    signup_username_entry.delete(0,END)
                    signup_password_entry.delete(0,END)
                    signup_re_password_entry.delete(0,END)
                else:
                    mycursor.execute(f"INSERT INTO account_details(username,password) VALUES('{new_signup_username}','{new_signup_password}')")
                    myconnector.commit()
                    myconnector.close()

                    signup_password_entry.delete(0,END)
                    signup_username_entry.delete(0,END)
                    signup_re_password_entry.delete(0,END)

                    signup_password_entry.place_forget()
                    signup_username_entry.place_forget()
                    signup_re_password_entry.place_forget()
                    signup_window_label.pack_forget()
                    creating_account_continue_button.place_forget()

                    dummy_start_window_label.pack()
                    dummy_loginbutton_button.place(x=525,y=490)
                    dummy_signupbutton_button.place(x=525,y=625)
                    dummy_if_your_admin_button.place(x=580,y=740)

                    messagebox.showinfo("Liberty Library","New account created")

                    


    
def if_your_admin_page():
    start_window_label.pack_forget()
    signup_button.place_forget()
    login_button.place_forget()
    dummy_start_window_label.pack_forget()
    dummy_signupbutton_button.place_forget()
    dummy_loginbutton_button.place_forget()
    if_your_admin_Button.place_forget()
    dummy_if_your_admin_button.place_forget()

    if_your_admin_loginpage_label.pack()
    back_button.place(x=0,y=1)
    admin_password_entry.place(x=650,y=520)
    admin_username_entry.place(x=650,y=370)
    continue_if_your_admin_button.place(x=550,y=610)

    
def admin_main_page():
    new_admin_username=admin_username_entry.get()
    new_admin_password=admin_password_entry.get()

    myconnector=mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()
    
    if new_admin_password== "" or new_admin_username== "":
        messagebox.showwarning('Liberty Library','Dont Leave fields Empty')

    
    else:
        mycursor.execute(f"select count(*) from admin_deltails where admin_username='{new_admin_username}'")
        result=mycursor.fetchone()
         
        if int(result[0])==0:
            messagebox.showwarning('Liberty Library','This Username Does Not Exist !')
            admin_password_entry.delete(0,END)
            admin_username_entry.delete(0,END)
        else:
            mycursor.execute(f"select* from admin_deltails where admin_username='{new_admin_username}'")
            result=mycursor.fetchone()
            if result[2]==new_admin_password:
                myconnector.close()
                login_window_label.pack_forget()
                login_username_entry.place_forget()
                login_password_entry.place_forget()
                login_continue_button.place_forget()
                back_button.place_forget()
                if_your_admin_loginpage_label.pack_forget()
                admin_password_entry.place_forget()
                admin_username_entry.place_forget()
                continue_if_your_admin_button.place_forget()
                mainpage_window_label.pack()
                dashboard_mainpage_button.place(x=10,y=200)
                issue_mainpage_button.place(x=10,y=290)
                returnbook_mainpage_button.place(x=10,y=380)
                addremove_mainpage_button.place(x=10,y=470)
                detail_mainpage_button.place(x=10,y=560)
                report_mainpage_button.place(x=10,y=650)
                logout_mainpage_button.place(x=10,y=740)
                aboutus_mainpage_button.place(x=760,y=182)
                admin_username_entry.delete(0,END)
                admin_password_entry.delete(0,END)

            else:
                messagebox.showwarning('Liberty Library','Wrong Password ! Please Enter Correct Password !')
                admin_password_entry.delete(0,END)


        




def go_to_dashboard():
    dashboard_mainpage_button.place(x=10,y=200)
    issue_mainpage_button.place(x=10,y=290)
    returnbook_mainpage_button.place(x=10,y=380)
    report_mainpage_button.place(x=10,y=650)
    logout_mainpage_button.place(x=10,y=740)
    
    aboutus_mainpage_button.place(x=760,y=182)
    detail_mainpage_button.place(x=10,y=560)
    addremove_mainpage_button.place(x=10,y=470)

def go_to_issue(user):
    mainpage_window_label.pack_forget()
    dashboard_mainpage_button.place_forget()
    issue_mainpage_button.place_forget()
    returnbook_mainpage_button.place_forget()
    report_mainpage_button.place_forget()
    logout_mainpage_button.place_forget()
    aboutus_mainpage_button.place_forget()
    addremove_mainpage_button.place_forget()
    detail_mainpage_button.place_forget()
    viewbooks_button.place_forget()
    searchbook_button.place_forget()
    borrwer_mainpage_label.pack_forget()
    
    logout_borrower_button.place_forget()
    

    issuepage_label.pack()
    
    
    
    
    
    
    fiction_book1_label.place(x=70,y=260)
    fiction_book2_label.place(x=600,y=260)
    fiction_book3_label.place(x=1130,y=260)

    
    if user=="admin":
        lend_fic1_button.place(x=150,y=770)
        lend_fic2_button.place(x=690,y=770)
        lend_fic3_button.place(x=1230,y=770)
        back_button_admin_issue_to_mainpage_button.place(x=20,y=20)
        fiction_admin_issuepage_button.place(x=10,y=160)
        thriller_admin_issuepage_button.place(x=200,y=160)
        fantasy_admin_issuepage_button.place(x=390,y=160)
        horror_admin_issuepage_button.place(x=580,y=160)
        adventure_admin_issuepage_button.place(x=740,y=160)
        popular_admin_issuepage_button.place(x=980,y=160)
    else:
        hi_user_label.place_forget()
        view_fic1_button.place(x=150,y=770)
        view_fic2_button.place(x=690,y=770)
        view_fic3_button.place(x=1230,y=770)  
        back_button_bor_issue_to_mainpage_button.place(x=15,y=10)  
        fiction_bor_issuepage_button.place(x=10,y=160)
        thriller_bor_issuepage_button.place(x=200,y=160)
        fantasy_bor_issuepage_button.place(x=390,y=160)
        horror_bor_issuepage_button.place(x=580,y=160)
        adventure_bor_issuepage_button.place(x=740,y=160)
        popular_bor_issuepage_button.place(x=980,y=160)




    
def go_to_addremovebook():
    mainpage_window_label.pack_forget()
    dashboard_mainpage_button.place_forget()
    issue_mainpage_button.place_forget()
    returnbook_mainpage_button.place_forget()
    report_mainpage_button.place_forget()
    logout_mainpage_button.place_forget()
    aboutus_mainpage_button.place_forget()
    addremove_mainpage_button.place_forget()
    detail_mainpage_button.place_forget()




    book_det_table.place(relx=0.05,rely=0.22,width=1300,height=500)
    scrollbary1.place(relx=0.934,rely=0.22,width=22,height=432)
    scrollbarx1.place(relx=0.08,rely=0.830,width=1000,height=22)
    myconnector=mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()
    mycursor.execute("select count(*) from book_info")
    result=mycursor.fetchone()
    n=result[0]
    k=1
    for i in range(0,n):
        mycursor.execute(f"select* from book_info")
        result1=mycursor.fetchall()
        book_det_table.insert(parent='',index=k,values=result1[i])
        k=k+1
    chumma_label.pack()
    addbook_button.place(x=1220,y=700)
    remove_book_button.place(x=30,y=750)
    back_addbookpage_to_mainpage_button.place(x=20,y=20)





def go_to_returnbook():
    mainpage_window_label.pack_forget()
    dashboard_mainpage_button.place_forget()
    issue_mainpage_button.place_forget()
    returnbook_mainpage_button.place_forget()
    report_mainpage_button.place_forget()
    logout_mainpage_button.place_forget()
    aboutus_mainpage_button.place_forget()
    addremove_mainpage_button.place_forget()
    detail_mainpage_button.place_forget()



    return_bor_name_entry.config(state="normal")
    return_bor_id_entry.config(state="normal")
    return_book_code_entry.config(state="normal")
    return_book_name_entry.config(state="normal")
    return_bor_name_entry.delete(0,END)
    return_bor_id_entry.delete(0,END)
    return_book_code_entry.delete(0,END)
    return_book_name_entry.delete(0,END)
    return_bor_name_entry.config(state="disabled")
    return_book_code_entry.config(state="disabled")
    return_book_name_entry.config(state="disabled")
    return_bor_id_entry.place(x=480,y=250)
    return_book_name_entry.place(x=480,y=510)
    return_book_code_entry.place(x=480,y=660)

    return_page_label.pack()
    return_bor_name_entry.place(x=480,y=380)
    return_bor_id_entry.place(x=480,y=250)
    return_book_name_entry.place(x=480,y=510)
    return_book_code_entry.place(x=480,y=660)
    return_button.place(x=1200,y=690)
    get_info_Button.place(x=850,y=230)
    back_return_to_mainpage_button.place(x=20,y=20)

def go_to_detail():
    mainpage_window_label.pack_forget()
    dashboard_mainpage_button.place_forget()
    issue_mainpage_button.place_forget()
    returnbook_mainpage_button.place_forget()
    report_mainpage_button.place_forget()
    logout_mainpage_button.place_forget()
    aboutus_mainpage_button.place_forget()
    addremove_mainpage_button.place_forget()
    detail_mainpage_button.place_forget()
    chumma_label.pack()
    back_button_det_to_mainpage_button.place(x=20,y=20)


    borrower_det_table.place(relx=0.01,rely=0.22,width=1400,height=600)
    scrollbary.place(relx=0.934,rely=0.22,width=22,height=432)
    scrollbarx.place(relx=0.002,rely=0.922,width=651,height=22)
    myconnector=mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()
    myanothercursor=myconnector.cursor()
    myanothercursor.execute("select count(*) from borrower_info")
    num=myanothercursor.fetchone()
    n=num[0]
    k=1
    for i in range(0,n):
        mycursor.execute(f"select* from borrower_info ")
        result=mycursor.fetchall()
        borrower_det_table.insert(parent='',index=k,values=result[i])
        k=k+1
    


def go_to_defaulter():
    mainpage_window_label.pack_forget()
    dashboard_mainpage_button.place_forget()
    issue_mainpage_button.place_forget()
    returnbook_mainpage_button.place_forget()
    report_mainpage_button.place_forget()
    logout_mainpage_button.place_forget()
    aboutus_mainpage_button.place_forget()
    detail_mainpage_button.place_forget()
    addremove_mainpage_button.place_forget()
    
    defaulters_det_table.place(relx=0.05,rely=0.22,width=1300,height=500)
    scrollbary2.place(relx=0.934,rely=0.22,width=22,height=432)
    scrollbarx2.place(relx=0.08,rely=0.830,width=1000,height=22)
    chumma_label.pack()
    back_defaulter_to_mainpage_button.place(x=20,y=20)


    myconnector=mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()
    mycursor.execute("select count(*) from borrower_info where return_date<curdate()")
    result=mycursor.fetchone()
    n=result[0]
    k=1
    for i in range(0,n):
        mycursor.execute(f"select* from borrower_info where return_date<curdate()")
        result1=mycursor.fetchall()
        defaulters_det_table.insert(parent='',index=k,values=result1[i])
        k=k+1
      
    
    

    

    
def go_to_logout(user):
    if user=="admin":
        logout_mainpage_button.place_forget()
        mainpage_window_label.pack_forget()
        dashboard_mainpage_button.place_forget()
        issue_mainpage_button.place_forget()
        returnbook_mainpage_button.place_forget()
        report_mainpage_button.place_forget()
        logout_mainpage_button.place_forget()
        aboutus_mainpage_button.place_forget()
        addremove_mainpage_button.place_forget()
        detail_mainpage_button.place_forget()
        
    
    if user=="bor":
        hi_user_label.place_forget()
        viewbooks_button.place_forget()
        searchbook_button.place_forget()
        logout_borrower_button.place_forget()
        borrwer_mainpage_label.pack_forget()
    dummy_start_window_label.pack()
    dummy_signupbutton_button.place(x=525,y=625)
    dummy_loginbutton_button.place(x=525,y=490)
    dummy_if_your_admin_button.place(x=580,y=740) 
   
    


def go_to_aboutus():
    mainpage_window_label.pack_forget()
    dashboard_mainpage_button.place_forget()
    issue_mainpage_button.place_forget()
    returnbook_mainpage_button.place_forget()
    report_mainpage_button.place_forget()
    logout_mainpage_button.place_forget()
    aboutus_mainpage_button.place_forget()
    detail_mainpage_button.place_forget()
    addremove_mainpage_button.place_forget()

    aboutus_page_label.pack()
    back_aboutus_to_mainpage_button.place(x=20,y=20)

def go_to_signup_page():
    
    start_window_label.pack_forget()
    signup_button.place_forget()
    login_button.place_forget()
    dummy_signupbutton_button.place_forget()
    dummy_loginbutton_button.place_forget()
    dummy_start_window_label.pack_forget()
    dummy_if_your_admin_button.place_forget()
    if_your_admin_Button.place_forget()


    signup_username_entry.place(x=650,y=282)
    signup_password_entry.place(x=650,y=382)
    signup_re_password_entry.place(x=650,y=530)
    signup_window_label.pack()
    creating_account_continue_button.place(x=600,y=600)
    back_button.place(x=0,y=1)
    
def borrow_pick_date(event):
    global borrow_cal,borrow_date_window
    borrow_date_window=Toplevel()
    borrow_date_window.grab_set()
    borrow_date_window.title("Choose Borrow Date")
    borrow_date_window.geometry("250x220+590+370")
    borrow_cal=Calendar(borrow_date_window,selectmode="day",date_pattern="y/mm/d")
    borrow_cal.place(x=0,y=0)
    borrow_submit_button=Button(borrow_date_window, text="submit",command=borrow_grab_date)
    borrow_submit_button.place(x=90,y=190)


def borrow_grab_date():
    borrow_date_entry.delete(0,END)
    borrow_date_entry.insert(0,borrow_cal.get_date())
    borrow_date_window.destroy()

def return_pick_date(event):
    global return_cal,return_date_window
    return_date_window=Toplevel()
    return_date_window.grab_set()
    return_date_window.title("Choose Borrow Date")
    return_date_window.geometry("250x220+590+370")
    return_cal=Calendar(return_date_window,selectmode="day",date_pattern="y/mm/d")
    return_cal.place(x=0,y=0)
    return_submit_button=Button(return_date_window, text="submit",command=return_grab_date)
    return_submit_button.place(x=90,y=190)


def return_grab_date():
    return_date_entry.delete(0,END)
    return_date_entry.insert(0,return_cal.get_date())
    return_date_window.destroy()



def return_book():
    new_bor_id=return_bor_id_entry.get()
    new_book_code=return_book_code_entry.get()
    myconnector=mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()
    mycursor1=myconnector.cursor()
    mycursor2=myconnector.cursor()
    mycursor.execute(f"select*from book_info where isbn_code={new_bor_id}")
    result=mycursor.fetchone()
    copies=result[-1]
    mycursor1.execute(f"update book_info set copies={1+int(copies)} where isbn_code={new_book_code}")
    mycursor2.execute(f"delete from borrower_info where bor_id={new_bor_id}")
    myconnector.commit()
    myconnector.close()
    messagebox.showinfo("Liberty Library","succesfully returned book")
    return_bor_id_entry.delete(0,END)
    return_book_code_entry.delete(0,END)
    return_bor_name_entry.delete(0,END)
    return_book_name_entry.delete(0,END)

    
def get_return_info():
    new_bor_id=return_bor_id_entry.get()
    myconnector=mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()
    mycursor.execute(f"select * from borrower_info where bor_id={new_bor_id}")
    result=mycursor.fetchone()
    return_bor_name_entry.config(state="normal")
    return_book_name_entry.config(state="normal")
    return_book_code_entry.config(state="normal")
    return_book_code_entry.insert(0,result[6])
    return_book_name_entry.insert(0,result[5])
    return_bor_name_entry.insert(0,result[1])
    return_bor_name_entry.config(state="disabled")
    return_book_name_entry.config(state="disabled")
    return_book_code_entry.config(state="disabled")
    return_bor_id_entry.config(state="disabled")

def go_to_addbook_page():
    book_det_table.place_forget()
    chumma_label.pack_forget()
    scrollbarx1.place_forget()
    scrollbary1.place_forget()
    addbook_button.place_forget()
    remove_book_button.place_forget()
    back_addbookpage_to_mainpage_button.place_forget()
    addbook_book_name_entry.place(x=400,y=220)
    addbook_book_id_entry.place(x=1300,y=220)
    addbook_author_entry.place(x=400,y=350)
    addbook_rating_entry.place(x=400,y=460)
    addbook_genre_entry.place(x=400,y=570)
    addbook_num_of_copies_entry.place(x=600,y=710)
    add_book_another_button.place(x=1200,y=710)
    back_addpage_to_addbookpage_button.place(x=20,y=20)
    
    addbook_page_label.pack()

def addbook_to_library():
    new_book_id=addbook_book_id_entry.get()
    new_book_name=addbook_book_name_entry.get()
    new_author=addbook_author_entry.get()
    new_rating=addbook_rating_entry.get()
    new_genre=addbook_genre_entry.get()
    new_num_copies=addbook_num_of_copies_entry.get()
    myconnector=mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()
    mycursor.execute(f"insert into book_info(isbn_code,book_name,author,edition,rating,genre,copies) values({new_book_id},'{new_book_name}','{new_author}','second',{new_rating},'{new_genre}',{new_num_copies})")
    myconnector.commit()
    messagebox.showinfo("Liberty Library","Added book")

    addbook_book_id_entry.delete(0,END)
    addbook_book_name_entry.delete(0,END)
    addbook_author_entry.delete(0,END)
    addbook_rating_entry.delete(0,END)
    addbook_genre_entry.delete(0,END)
    addbook_num_of_copies_entry.delete(0,END)

    addbook_book_id_entry.place_forget()
    addbook_book_name_entry.place_forget()
    addbook_author_entry.place_forget()
    addbook_rating_entry.place_forget()
    addbook_genre_entry.place_forget()
    addbook_num_of_copies_entry.place_forget()
    add_book_another_button.place_forget()
    back_addpage_to_addbookpage_button.place_forget()
    addbook_page_label.pack_forget()

    book_det_table.place(relx=0.05,rely=0.22,width=1300,height=500)
    scrollbary1.place(relx=0.934,rely=0.22,width=22,height=432)
    scrollbarx1.place(relx=0.08,rely=0.830,width=1000,height=22)
    chumma_label.pack()
    addbook_button.place(x=1220,y=700)
    back_addbookpage_to_mainpage_button.place(x=20,y=20)


def remove_book_from_lib():
    item=book_det_table.selection()
    for i in item:
        book_code=book_det_table.item(i,'values')[0]
    book_det_table.delete(item)
    
    myconnector=mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()
    mycursor.execute(f"update book_info set copies=0 where isbn_code={book_code}")
    myconnector.commit()
    myconnector.close()
    messagebox.showinfo("Liberty Library","Removed book")


def go_to_searchpage():
    borrwer_mainpage_label.pack_forget()
    logout_borrower_button.place_forget()
    searchbook_button.place_forget()
    viewbooks_button.place_forget()
    hi_user_label.place_forget()
    search_page_label.pack()



    search_table.place(relx=0.05,rely=0.5,width=1300,height=300)
    scrollbary3.place(relx=0.914,rely=0.6,width=22,height=200)
    scrollbarx3.place(relx=0.08,rely=0.870,width=1000,height=22)
    bookname_search_entry.place(x=300,y=220)
    Authorname_search_entry.place(x=1090,y=220)
    search_actual_button.place(x=660,y=300)
    back_search_to_mainpage_button.place(x=20,y=20)


def search():
    for item in search_table.get_children():
            search_table.delete(item)
    new_bookname=bookname_search_entry.get()
    new_authorname=Authorname_search_entry.get()
    myconnector=mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()
    if new_bookname=="" and new_authorname=="":
        messagebox.showwarning("Liberty Library","Enter the Book or Author name to search")
    if new_authorname=="":

        mycursor.execute(f"select  count(*) from book_info where book_name='{new_bookname}'")
        num=mycursor.fetchone()
        n=num[0]
        if n==0:
            messagebox.showwarning("Liberty Library","Book not available")
        k=1
        for i in range(0,n):
            mycursor.execute(f"select * from book_info where book_name= '{new_bookname}'")
            result=mycursor.fetchall()
            search_table.insert(parent='',index=k,values=result[i])
            k=k+1
    if new_bookname=="": 
        mycursor.execute(f"select count(*) from book_info where author='{new_authorname}'")
        num=mycursor.fetchone()
        n=num[0]
        if n==0:
            messagebox.showwarning("Liberty Library","Book not available")
        k=1
        for i in range(0,n):
            mycursor.execute(f"select * from book_info where author='{new_authorname}'")
            result1=mycursor.fetchall()
            search_table.insert(parent='',index=k,values=result1[i])
            k=k+1

    

#lend page
def lendfic_page(a):
    global num_of_book_avail_label,num_of_book_avail_label,book_id
    book_id=a
    issuepage_label.pack_forget()
    lend_fic1_button.place_forget()
    lend_fic2_button.place_forget()
    lend_fic3_button.place_forget()
    fiction_book1_label.place_forget()
    fiction_book2_label.place_forget()
    fiction_book3_label.place_forget()
    fiction_admin_issuepage_button.place_forget()
    fantasy_admin_issuepage_button.place_forget()
    popular_admin_issuepage_button.place_forget()
    horror_admin_issuepage_button.place_forget()

    adventure_admin_issuepage_button.place_forget()
    thriller_admin_issuepage_button.place_forget()
    back_button_admin_issue_to_mainpage_button.place_forget()

    lendpage_label.pack()
    lend_bor_name_entry.place(x=370,y=170)
    borrow_date_entry.place(x=370,y=250)
    return_date_entry.place(x=370,y=350)
    lend_phone_num_entry.place(x=370,y=470)
    lend_book_name_entry.place(x=370,y=550)
    lend_isbn_code_entry.place(x=370,y=640)
    lend_address_entry.place(x=370,y=740)
    lend_button.place(x=1200,y=700)
    back_but_lend_to_mainpage_button.place(x=20,y=20)
    borrow_date_entry.delete(0,END)
    return_date_entry.delete(0,END)
    lend_phone_num_entry.delete(0,END)
    lend_isbn_code_entry.delete(0,END)
    lend_address_entry.delete(0,END)
    lend_book_name_entry.delete(0,END)
    copies_wanted.delete(0,END)
    
   
    myconnector = mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()
    
    
    mycursor.execute(f"select * from book_info where isbn_code={a}")
    result=mycursor.fetchone()
    bookname=result[1]
    num_of_book_avail_label=Label(root,text=result[-1],background="#191926",fg="white",font=("Heveltica",20,"bold"),width=5,pady=5)
    num_of_book_avail_label.place(x=1350,y=190)
    copies_wanted.place(x=1350,y=280)
    lend_book_name_entry.insert(0,bookname)
    lend_isbn_code_entry.insert(0,result[0])
    

def lendthrill_page(a):
    global num_of_book_avail_label, book_id
    book_id=a
    lendpage_label.pack()
    issuepage_label.pack_forget()
    lend_thrill1_button.place_forget()
    lend_thrill2_button.place_forget()
    lend_thrill3_button.place_forget()
    thriller_book1_label.place_forget()
    thriller_book2_label.place_forget()
    thriller_book3_label.place_forget()
    fiction_admin_issuepage_button.place_forget()
    fantasy_admin_issuepage_button.place_forget()
    popular_admin_issuepage_button.place_forget()
    horror_admin_issuepage_button.place_forget()
    
    adventure_admin_issuepage_button.place_forget()
    thriller_admin_issuepage_button.place_forget()
    back_button_admin_issue_to_mainpage_button.place_forget()

    lendpage_label.pack()
    lend_bor_name_entry.place(x=370,y=170)
    borrow_date_entry.place(x=370,y=250)
    return_date_entry.place(x=370,y=350)
    lend_phone_num_entry.place(x=370,y=470)
    lend_book_name_entry.place(x=370,y=550)
    lend_isbn_code_entry.place(x=370,y=640)
    lend_address_entry.place(x=370,y=740)
    lend_button.place(x=1200,y=700)
    back_but_lend_to_mainpage_button.place(x=20,y=20)
    borrow_date_entry.delete(0,END)
    return_date_entry.delete(0,END)
    lend_phone_num_entry.delete(0,END)
    lend_isbn_code_entry.delete(0,END)
    lend_address_entry.delete(0,END)
    lend_book_name_entry.delete(0,END)
    copies_wanted.delete(0,END)

    myconnector = mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()

    
    mycursor.execute(f"select * from book_info where isbn_code={a}")
    result=mycursor.fetchone()
    bookname=result[1]
    num_of_book_avail_label=Label(root,text=result[-1],background="#191926",fg="white",font=("Heveltica",20,"bold"),width=5,pady=5)
    num_of_book_avail_label.place(x=1350,y=190)
    copies_wanted.place(x=1350,y=280)
    lend_book_name_entry.insert(0,bookname)
    lend_isbn_code_entry.insert(0,result[0])



def lendfantasy_page(a):
    global num_of_book_avail_label, book_id
    book_id=a
    lendpage_label.pack()
    lendpage_label.pack()
    issuepage_label.pack_forget()
    lend_fantasy1_button.place_forget()
    lend_fantasy2_button.place_forget()
    lend_fantasy3_button.place_forget()
    fantasy_book1_label.place_forget()
    fantasy_book2_label.place_forget()
    fantasy_book3_label.place_forget()
    fiction_admin_issuepage_button.place_forget()
    fantasy_admin_issuepage_button.place_forget()
    popular_admin_issuepage_button.place_forget()
    horror_admin_issuepage_button.place_forget()

    adventure_admin_issuepage_button.place_forget()
    thriller_admin_issuepage_button.place_forget()
    back_button_admin_issue_to_mainpage_button.place_forget()

    lendpage_label.pack()
    lend_bor_name_entry.place(x=370,y=170)
    borrow_date_entry.place(x=370,y=250)
    return_date_entry.place(x=370,y=350)
    lend_phone_num_entry.place(x=370,y=470)
    lend_book_name_entry.place(x=370,y=550)
    lend_isbn_code_entry.place(x=370,y=640)
    lend_address_entry.place(x=370,y=740)
    lend_button.place(x=1200,y=700)
    back_but_lend_to_mainpage_button.place(x=20,y=20)
    borrow_date_entry.delete(0,END)
    return_date_entry.delete(0,END)
    lend_phone_num_entry.delete(0,END)
    lend_isbn_code_entry.delete(0,END)
    lend_address_entry.delete(0,END)
    lend_book_name_entry.delete(0,END)
    copies_wanted.delete(0,END)

    myconnector = mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()

    
    mycursor.execute(f"select * from book_info where isbn_code={a}")
    result=mycursor.fetchone()
    bookname=result[1]
    num_of_book_avail_label=Label(root,text=result[-1],background="#191926",fg="white",font=("Heveltica",20,"bold"),width=5,pady=5)
    num_of_book_avail_label.place(x=1350,y=190)
    copies_wanted.place(x=1350,y=280)
    lend_book_name_entry.insert(0,bookname)
    lend_isbn_code_entry.insert(0,result[0])



def lendhorror_page(a):
    global num_of_book_avail_label, book_id
    book_id=a
    lendpage_label.pack()
    lendpage_label.pack()
    lendpage_label.pack()
    issuepage_label.pack_forget()
    lend_horror1_button.place_forget()
    lend_horror2_button.place_forget()
    lend_horror3_button.place_forget()
    horror_book1_label.place_forget()
    horror_book2_label.place_forget()
    horror_book3_label.place_forget()
    fiction_admin_issuepage_button.place_forget()
    fantasy_admin_issuepage_button.place_forget()
    popular_admin_issuepage_button.place_forget()
    horror_admin_issuepage_button.place_forget()
    
    adventure_admin_issuepage_button.place_forget()
    thriller_admin_issuepage_button.place_forget()
    back_button_admin_issue_to_mainpage_button.place_forget()

    lendpage_label.pack()
    lend_bor_name_entry.place(x=370,y=170)
    borrow_date_entry.place(x=370,y=250)
    return_date_entry.place(x=370,y=350)
    lend_phone_num_entry.place(x=370,y=470)
    lend_book_name_entry.place(x=370,y=550)
    lend_isbn_code_entry.place(x=370,y=640)
    lend_address_entry.place(x=370,y=740)
    lend_button.place(x=1200,y=700)
    back_but_lend_to_mainpage_button.place(x=20,y=20)
    borrow_date_entry.delete(0,END)
    return_date_entry.delete(0,END)
    lend_phone_num_entry.delete(0,END)
    lend_isbn_code_entry.delete(0,END)
    lend_address_entry.delete(0,END)
    lend_book_name_entry.delete(0,END)
    copies_wanted.delete(0,END)

    myconnector = mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()

    
    mycursor.execute(f"select * from book_info where isbn_code={a}")
    result=mycursor.fetchone()
    bookname=result[1]
    num_of_book_avail_label=Label(root,text=result[-1],background="#191926",fg="white",font=("Heveltica",20,"bold"),width=5,pady=5)
    num_of_book_avail_label.place(x=1350,y=190)
    copies_wanted.place(x=1350,y=280)
    lend_book_name_entry.insert(0,bookname)
    lend_isbn_code_entry.insert(0,result[0])




def lendadventure_page(a):
    global num_of_book_avail_label,book_id
    book_id=a
    lendpage_label.pack()
    lendpage_label.pack()
    lendpage_label.pack()
    lendpage_label.pack()
    issuepage_label.pack_forget()
    lend_adventure1_button.place_forget()
    lend_adventure2_button.place_forget()
    lend_adventure3_button.place_forget()
    adventure_book1_label.place_forget()
    adventure_book2_label.place_forget()
    adventure_book3_label.place_forget()
    fiction_admin_issuepage_button.place_forget()
    fantasy_admin_issuepage_button.place_forget()
    popular_admin_issuepage_button.place_forget()
    horror_admin_issuepage_button.place_forget()
    
    adventure_admin_issuepage_button.place_forget()
    thriller_admin_issuepage_button.place_forget()
    back_button_admin_issue_to_mainpage_button.place_forget()

    lendpage_label.pack()
    lend_bor_name_entry.place(x=370,y=170)
    borrow_date_entry.place(x=370,y=250)
    return_date_entry.place(x=370,y=350)
    lend_phone_num_entry.place(x=370,y=470)
    lend_book_name_entry.place(x=370,y=550)
    lend_isbn_code_entry.place(x=370,y=640)
    lend_address_entry.place(x=370,y=740)
    lend_button.place(x=1200,y=700)
    back_but_lend_to_mainpage_button.place(x=20,y=20)
    borrow_date_entry.delete(0,END)
    return_date_entry.delete(0,END)
    lend_phone_num_entry.delete(0,END)
    lend_isbn_code_entry.delete(0,END)
    lend_address_entry.delete(0,END)
    lend_book_name_entry.delete(0,END)
    copies_wanted.delete(0,END)

    myconnector = mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()

    
    mycursor.execute(f"select * from book_info where isbn_code={a}")
    result=mycursor.fetchone()
    bookname=result[1]
    num_of_book_avail_label=Label(root,text=result[-1],background="#191926",fg="white",font=("Heveltica",20,"bold"),width=5,pady=5)
    num_of_book_avail_label.place(x=1350,y=190)
    copies_wanted.place(x=1350,y=280)
    lend_book_name_entry.insert(0,bookname)
    lend_isbn_code_entry.insert(0,result[0])




def lendpopular_page(a):
    global num_of_book_avail_label,book_id
    book_id=a
    lendpage_label.pack()
    issuepage_label.pack_forget()
    lend_popular1_button.place_forget()
    lend_popular2_button.place_forget()
    lend_popular3_button.place_forget()
    popular_book1_label.place_forget()
    popular_book2_label.place_forget()
    popular_book3_label.place_forget()
    fiction_admin_issuepage_button.place_forget()
    fantasy_admin_issuepage_button.place_forget()
    popular_admin_issuepage_button.place_forget()
    horror_admin_issuepage_button.place_forget()
    
    adventure_admin_issuepage_button.place_forget()
    thriller_admin_issuepage_button.place_forget()
    back_button_admin_issue_to_mainpage_button.place_forget()

    lendpage_label.pack()
    lend_bor_name_entry.place(x=370,y=170)
    borrow_date_entry.place(x=370,y=250)
    return_date_entry.place(x=370,y=350)
    lend_phone_num_entry.place(x=370,y=470)
    lend_book_name_entry.place(x=370,y=550)
    lend_isbn_code_entry.place(x=370,y=640)
    lend_address_entry.place(x=370,y=740)
    lend_button.place(x=1200,y=700)
    back_but_lend_to_mainpage_button.place(x=20,y=20)
    borrow_date_entry.delete(0,END)
    return_date_entry.delete(0,END)
    lend_phone_num_entry.delete(0,END)
    lend_isbn_code_entry.delete(0,END)
    lend_address_entry.delete(0,END)
    lend_book_name_entry.delete(0,END)
    copies_wanted.delete(0,END)

    myconnector = mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()

    
    mycursor.execute(f"select * from book_info where isbn_code={a}")
    result=mycursor.fetchone()
    bookname=result[1]
    num_of_book_avail_label=Label(root,text=result[-1],background="#191926",fg="white",font=("Heveltica",20,"bold"),width=5,pady=5)
    num_of_book_avail_label.place(x=1350,y=190)
    copies_wanted.place(x=1350,y=280)
    lend_book_name_entry.insert(0,bookname)
    lend_isbn_code_entry.insert(0,result[0])



def viewfic_page(b):
    global available_label
    issuepage_label.pack_forget()
    back_button_bor_issue_to_mainpage_button.place_forget()
    fiction_bor_issuepage_button.place_forget()
    fantasy_bor_issuepage_button.place_forget()
    thriller_bor_issuepage_button.place_forget()
    horror_bor_issuepage_button.place_forget()
    adventure_bor_issuepage_button.place_forget()
    popular_bor_issuepage_button.place_forget()

    fiction_book1_label.place_forget()
    fiction_book2_label.place_forget()
    fiction_book3_label.place_forget()
    view_fic1_button.place_forget()
    view_fic2_button.place_forget()
    view_fic3_button.place_forget()
    back_about_to_issue_button.place(x=10,y=10)
    if b==1:
        about_fic1_Label.pack()
        bookcode=1
    if b==2:
        about_fic2_Label.pack()
        bookcode=2
    if b==3:
        about_fic3_Label.pack()
        bookcode=3
    myconnector = mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()
    mycursor.execute(f"select * from book_info where isbn_code={bookcode}")
    result=mycursor.fetchone()
    available_label=Label(root,text=result[-1],background="#191926",fg="white",font=("Heveltica",20,"bold"),width=5,pady=5)
    available_label.place(x=370,y=730)
    if result[-1]<=0:
        no_label.place(x=200,y=660)

    else:
        yes_label.place(x=200,y=660)



def viewthrill_page(b):
    global available_label
    issuepage_label.pack_forget()
    back_button_bor_issue_to_mainpage_button.place_forget()
    fiction_bor_issuepage_button.place_forget()
    fantasy_bor_issuepage_button.place_forget()
    thriller_bor_issuepage_button.place_forget()
    horror_bor_issuepage_button.place_forget()
    adventure_bor_issuepage_button.place_forget()
    popular_bor_issuepage_button.place_forget()
    
    thriller_book1_label.place_forget()
    thriller_book2_label.place_forget()
    thriller_book3_label.place_forget()
    view_thrill1_button.place_forget()
    view_thrill2_button.place_forget()
    view_thrill3_button.place_forget()
    back_about_to_issue_button.place(x=10,y=10)
    
    if b==1:
        about_thrill1_Label.pack()
        bookcode=4
    if b==2:
        about_thrill2_Label.pack()
        bookcode=6
    if b==3:
        about_thrill3_Label.pack()
        bookcode=5
    myconnector = mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()
    mycursor.execute(f"select * from book_info where isbn_code={bookcode}")
    result=mycursor.fetchone()
    available_label=Label(root,text=result[-1],background="#191926",fg="white",font=("Heveltica",20,"bold"),width=5,pady=5)
    available_label.place(x=370,y=730)
    if result[-1]<=0:
        no_label.place(x=200,y=660)

    else:
        yes_label.place(x=200,y=660)




def viewfan_page(b):
    global available_label
    issuepage_label.pack_forget()
    back_button_bor_issue_to_mainpage_button.place_forget()
    fiction_bor_issuepage_button.place_forget()
    fantasy_bor_issuepage_button.place_forget()
    thriller_bor_issuepage_button.place_forget()
    horror_bor_issuepage_button.place_forget()
    adventure_bor_issuepage_button.place_forget()
    popular_bor_issuepage_button.place_forget()
    
    fantasy_book1_label.place_forget()
    fantasy_book2_label.place_forget()
    fantasy_book3_label.place_forget()
    view_fan1_button.place_forget()
    view_fan2_button.place_forget()
    view_fan3_button.place_forget()
    back_about_to_issue_button.place(x=10,y=10)
    if b==1:
        about_fan1_Label.pack()
        bookcode=8
    if b==2:
        about_fan2_Label.pack()
        bookcode=9
    if b==3:
        about_fan3_Label.pack()
        bookcode=7
    myconnector = mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()
    mycursor.execute(f"select * from book_info where isbn_code={bookcode}")
    result=mycursor.fetchone()
    available_label=Label(root,text=result[-1],background="#191926",fg="white",font=("Heveltica",20,"bold"),width=5,pady=5)
    available_label.place(x=370,y=730)

    if result[-1]<=0:
        no_label.place(x=200,y=660)

    else:
        yes_label.place(x=200,y=660)

    

def viewhor_page(b):
    global available_label
    issuepage_label.pack_forget()
    back_button_bor_issue_to_mainpage_button.place_forget()
    fiction_bor_issuepage_button.place_forget()
    fantasy_bor_issuepage_button.place_forget()
    thriller_bor_issuepage_button.place_forget()
    horror_bor_issuepage_button.place_forget()
    adventure_bor_issuepage_button.place_forget()
    popular_bor_issuepage_button.place_forget()
    
    horror_book1_label.place_forget()
    horror_book2_label.place_forget()
    horror_book3_label.place_forget()
    view_hor1_button.place_forget()
    view_hor2_button.place_forget()
    view_hor3_button.place_forget()
    back_about_to_issue_button.place(x=10,y=10)
    if b==1:
        about_hor1_label.pack()
        bookcode=10
    if b==2:
        about_hor2_label.pack()
        bookcode=12
    if b==3:
        about_hor3_label.pack()
        bookcode=11
    myconnector = mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()
    mycursor.execute(f"select * from book_info where isbn_code={bookcode}")
    result=mycursor.fetchone()
    available_label=Label(root,text=result[-1],background="#191926",fg="white",font=("Heveltica",20,"bold"),width=5,pady=5)
    available_label.place(x=370,y=730)

    if result[-1]<=0:
        no_label.place(x=200,y=660)

    else:
        yes_label.place(x=200,y=660)



def viewadv_page(b):
    global available_label
    issuepage_label.pack_forget()
    back_button_bor_issue_to_mainpage_button.place_forget()
    fiction_bor_issuepage_button.place_forget()
    fantasy_bor_issuepage_button.place_forget()
    thriller_bor_issuepage_button.place_forget()
    horror_bor_issuepage_button.place_forget()
    adventure_bor_issuepage_button.place_forget()
    popular_bor_issuepage_button.place_forget()
    
    adventure_book1_label.place_forget()
    adventure_book2_label.place_forget()
    adventure_book3_label.place_forget()
    view_adv1_button.place_forget()
    view_adv2_button.place_forget()
    view_adv3_button.place_forget()
    back_about_to_issue_button.place(x=10,y=10)
    if b==1:
        about_adv1_label.pack()
        bookcode=15
    if b==2:
        about_adv2_label.pack()
        bookcode=13
    if b==3:
        about_adv3_label.pack()
        bookcode=14
    myconnector = mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()
    mycursor.execute(f"select * from book_info where isbn_code={bookcode}")
    result=mycursor.fetchone()
    available_label=Label(root,text=result[-1],background="#191926",fg="white",font=("Heveltica",20,"bold"),width=5,pady=5)
    available_label.place(x=370,y=730)

    if result[-1]<=0:
        no_label.place(x=200,y=660)

    else:
        yes_label.place(x=200,y=660)





def viewpop_page(b):
    global available_label
    issuepage_label.pack_forget()
    back_button_bor_issue_to_mainpage_button.place_forget()
    fiction_bor_issuepage_button.place_forget()
    fantasy_bor_issuepage_button.place_forget()
    thriller_bor_issuepage_button.place_forget()
    horror_bor_issuepage_button.place_forget()
    adventure_bor_issuepage_button.place_forget()
    popular_bor_issuepage_button.place_forget()

    popular_book1_label.place_forget()
    popular_book2_label.place_forget()
    popular_book3_label.place_forget()
    view_pop1_button.place_forget()
    view_pop2_button.place_forget()
    view_pop3_button.place_forget()
    back_about_to_issue_button.place(x=10,y=10)
    if b==1:
        about_pop1_label.pack()
        bookcode=16
    if b==2:
        about_pop2_label.pack()
        bookcode=18
    if b==3:
        about_pop3_label.pack()
        bookcode=17
    

    myconnector = mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()
    mycursor.execute(f"select * from book_info where isbn_code={bookcode}")
    result=mycursor.fetchone()
    available_label=Label(root,text=result[-1],background="#191926",fg="white",font=("Heveltica",20,"bold"),width=5,pady=5)
    available_label.place(x=370,y=730)

    if result[-1]<=0:
        no_label.place(x=200,y=660)

    else:
        yes_label.place(x=200,y=660)





def fiction_click(user):
    thriller_book1_label.place_forget()
    thriller_book2_label.place_forget()
    thriller_book3_label.place_forget()
    fantasy_book1_label.place_forget()
    fantasy_book2_label.place_forget()
    fantasy_book3_label.place_forget()
    horror_book1_label.place_forget()
    horror_book2_label.place_forget()
    horror_book3_label.place_forget()
    adventure_book1_label.place_forget()
    adventure_book2_label.place_forget()
    adventure_book3_label.place_forget()
    popular_book1_label.place_forget()
    popular_book2_label.place_forget()
    popular_book3_label.place_forget()
    view_thrill1_button.place_forget()
    view_thrill2_button.place_forget()
    view_thrill3_button.place_forget()
    view_fan1_button.place_forget()
    view_fan2_button.place_forget()
    view_fan3_button.place_forget()
    view_hor1_button.place_forget()
    view_hor2_button.place_forget()
    view_hor3_button.place_forget()
    view_adv1_button.place_forget()
    view_adv2_button.place_forget()
    view_adv3_button.place_forget()
    view_pop1_button.place_forget()
    view_pop2_button.place_forget()
    view_pop3_button.place_forget()   
    lend_thrill1_button.place_forget()
    lend_thrill2_button.place_forget()
    lend_thrill3_button.place_forget()
    lend_fantasy1_button.place_forget()
    lend_fantasy2_button.place_forget()
    lend_fantasy3_button.place_forget()
    lend_horror1_button.place_forget()
    lend_horror2_button.place_forget()
    lend_horror3_button.place_forget()
    lend_adventure1_button.place_forget()
    lend_adventure2_button.place_forget()
    lend_adventure3_button.place_forget()
    lend_popular1_button.place_forget()
    lend_popular2_button.place_forget()
    lend_popular3_button.place_forget()
    
    

    fiction_book1_label.place(x=70,y=260)
    fiction_book2_label.place(x=600,y=260)
    fiction_book3_label.place(x=1130,y=260)
    if user=='admin':
        lend_fic1_button.place(x=150,y=770)
        lend_fic2_button.place(x=690,y=770)
        lend_fic3_button.place(x=1230,y=770)
    else:
        view_fic1_button.place(x=150,y=770)
        view_fic2_button.place(x=690,y=770)
        view_fic3_button.place(x=1230,y=770)
        

def thriller_section(user):
    fiction_book1_label.place_forget()
    fiction_book2_label.place_forget()
    fiction_book3_label.place_forget()
    fantasy_book1_label.place_forget()
    fantasy_book2_label.place_forget()
    fantasy_book3_label.place_forget()
    horror_book1_label.place_forget()
    horror_book2_label.place_forget()
    horror_book3_label.place_forget()
    adventure_book1_label.place_forget()
    adventure_book2_label.place_forget()
    adventure_book3_label.place_forget()
    popular_book1_label.place_forget()
    popular_book2_label.place_forget()
    popular_book3_label.place_forget()
    view_fic1_button.place_forget()
    view_fic2_button.place_forget()
    view_fic3_button.place_forget()
    view_fan1_button.place_forget()
    view_fan2_button.place_forget()
    view_fan3_button.place_forget()
    view_hor1_button.place_forget()
    view_hor2_button.place_forget()
    view_hor3_button.place_forget()
    view_adv1_button.place_forget()
    view_adv2_button.place_forget()
    view_adv3_button.place_forget()
    view_pop1_button.place_forget()
    view_pop2_button.place_forget()
    view_pop3_button.place_forget()
    lend_fic1_button.place_forget()
    lend_fic2_button.place_forget()
    lend_fic3_button.place_forget()
    lend_fantasy1_button.place_forget()
    lend_fantasy2_button.place_forget()
    lend_fantasy3_button.place_forget()
    lend_horror1_button.place_forget()
    lend_horror2_button.place_forget()
    lend_horror3_button.place_forget()
    lend_adventure1_button.place_forget()
    lend_adventure2_button.place_forget()
    lend_adventure3_button.place_forget()
    lend_popular1_button.place_forget()
    lend_popular2_button.place_forget()
    lend_popular3_button.place_forget()       
    
    


    thriller_book1_label.place(x=70,y=260)
    thriller_book2_label.place(x=600,y=260)
    thriller_book3_label.place(x=1130,y=260)
    if user=='admin':
        lend_thrill1_button.place(x=150,y=770)
        lend_thrill2_button.place(x=690,y=770)
        lend_thrill3_button.place(x=1230,y=770)
    else:
        view_thrill1_button.place(x=150,y=770)
        view_thrill2_button.place(x=690,y=770)
        view_thrill3_button.place(x=1230,y=770)

        


def fantasy_section(user):
    thriller_book1_label.place_forget()
    thriller_book2_label.place_forget()
    thriller_book3_label.place_forget()
    fiction_book1_label.place_forget()
    fiction_book2_label.place_forget()
    fiction_book3_label.place_forget()
    horror_book1_label.place_forget()
    horror_book2_label.place_forget()
    horror_book3_label.place_forget()
    adventure_book1_label.place_forget()
    adventure_book2_label.place_forget()
    adventure_book3_label.place_forget()
    popular_book1_label.place_forget()
    popular_book2_label.place_forget()
    popular_book3_label.place_forget()
    view_fic1_button.place_forget()
    view_fic2_button.place_forget()
    view_fic3_button.place_forget()
    view_thrill1_button.place_forget()
    view_thrill2_button.place_forget()
    view_thrill3_button.place_forget()
    view_hor1_button.place_forget()
    view_hor2_button.place_forget()
    view_hor3_button.place_forget()
    view_adv1_button.place_forget()
    view_adv2_button.place_forget()
    view_adv3_button.place_forget()
    view_pop1_button.place_forget()
    view_pop2_button.place_forget()
    view_pop3_button.place_forget()
    lend_fic1_button.place_forget()
    lend_fic2_button.place_forget()
    lend_fic3_button.place_forget()
    lend_thrill1_button.place_forget()
    lend_thrill2_button.place_forget()
    lend_thrill3_button.place_forget()  
    lend_horror1_button.place_forget()
    lend_horror2_button.place_forget()
    lend_horror3_button.place_forget()
    lend_adventure1_button.place_forget()
    lend_adventure2_button.place_forget()
    lend_adventure3_button.place_forget()
    lend_popular1_button.place_forget()
    lend_popular2_button.place_forget()
    lend_popular3_button.place_forget()
    

    fantasy_book1_label.place(x=70,y=260)
    fantasy_book2_label.place(x=600,y=260)
    fantasy_book3_label.place(x=1130,y=260)
    if user=="admin":
        lend_fantasy1_button.place(x=150,y=770)
        lend_fantasy2_button.place(x=690,y=770)
        lend_fantasy3_button.place(x=1230,y=770)
    else:
        view_fan1_button.place(x=150,y=770)
        view_fan2_button.place(x=690,y=770)
        view_fan3_button.place(x=1230,y=770)

def horror_section(user):
    thriller_book1_label.place_forget()
    thriller_book2_label.place_forget()
    thriller_book3_label.place_forget()
    fiction_book1_label.place_forget()
    fiction_book2_label.place_forget()
    fiction_book3_label.place_forget()
    fantasy_book1_label.place_forget()
    fantasy_book2_label.place_forget()
    fantasy_book3_label.place_forget()
    adventure_book1_label.place_forget()
    adventure_book2_label.place_forget()
    adventure_book3_label.place_forget()
    popular_book1_label.place_forget()
    popular_book2_label.place_forget()
    popular_book3_label.place_forget()
    view_fic1_button.place_forget()
    view_fic2_button.place_forget()
    view_fic3_button.place_forget()
    view_thrill1_button.place_forget()
    view_thrill2_button.place_forget()
    view_thrill3_button.place_forget()
    view_fan1_button.place_forget()
    view_fan2_button.place_forget()
    view_fan3_button.place_forget()
    view_adv1_button.place_forget()
    view_adv2_button.place_forget()
    view_adv3_button.place_forget()
    view_pop1_button.place_forget()
    view_pop2_button.place_forget()
    view_pop3_button.place_forget()
    lend_fic1_button.place_forget()
    lend_fic2_button.place_forget()
    lend_fic3_button.place_forget()
    lend_thrill1_button.place_forget()
    lend_thrill2_button.place_forget()
    lend_thrill3_button.place_forget()
    lend_fantasy1_button.place_forget()
    lend_fantasy2_button.place_forget()
    lend_fantasy3_button.place_forget()
    lend_adventure1_button.place_forget()
    lend_adventure2_button.place_forget()
    lend_adventure3_button.place_forget()
    lend_popular1_button.place_forget()
    lend_popular2_button.place_forget()
    lend_popular3_button.place_forget()

    horror_book1_label.place(x=70,y=260)
    horror_book2_label.place(x=600,y=260)
    horror_book3_label.place(x=1130,y=260)
    if user=="admin":
        lend_horror1_button.place(x=150,y=770)
        lend_horror2_button.place(x=690,y=770)
        lend_horror3_button.place(x=1230,y=770)
    else:
        view_hor1_button.place(x=150,y=770)
        view_hor2_button.place(x=690,y=770)
        view_hor3_button.place(x=1230,y=770)
    
def adventure_section(user):
    thriller_book1_label.place_forget()
    thriller_book2_label.place_forget()
    thriller_book3_label.place_forget()
    fiction_book1_label.place_forget()
    fiction_book2_label.place_forget()
    fiction_book3_label.place_forget()
    fantasy_book1_label.place_forget()
    fantasy_book2_label.place_forget()
    fantasy_book3_label.place_forget()
    horror_book1_label.place_forget()
    horror_book2_label.place_forget()
    horror_book3_label.place_forget()
    popular_book1_label.place_forget()
    popular_book2_label.place_forget()
    popular_book3_label.place_forget()
    view_fic1_button.place_forget()
    view_fic2_button.place_forget()
    view_fic3_button.place_forget()
    view_thrill1_button.place_forget()
    view_thrill2_button.place_forget()
    view_thrill3_button.place_forget()
    view_fan1_button.place_forget()
    view_fan2_button.place_forget()
    view_fan3_button.place_forget()
    view_hor1_button.place_forget()
    view_hor2_button.place_forget()
    view_hor3_button.place_forget()
    view_pop1_button.place_forget()
    view_pop2_button.place_forget()
    view_pop3_button.place_forget()
    lend_fic1_button.place_forget()
    lend_fic2_button.place_forget()
    lend_fic3_button.place_forget()
    lend_thrill1_button.place_forget()
    lend_thrill2_button.place_forget()
    lend_thrill3_button.place_forget()
    lend_fantasy1_button.place_forget()
    lend_fantasy2_button.place_forget()
    lend_fantasy3_button.place_forget()
    lend_horror1_button.place_forget()
    lend_horror2_button.place_forget()
    lend_horror3_button.place_forget()
    lend_popular1_button.place_forget()
    lend_popular2_button.place_forget()
    lend_popular3_button.place_forget()

    adventure_book1_label.place(x=70,y=260)
    adventure_book2_label.place(x=600,y=260)
    adventure_book3_label.place(x=1130,y=260)
    if user=="admin":
        lend_adventure1_button.place(x=150,y=770)
        lend_adventure2_button.place(x=690,y=770)
        lend_adventure3_button.place(x=1230,y=770)
    else:
        view_adv1_button.place(x=150,y=770)
        view_adv2_button.place(x=690,y=770)
        view_adv3_button.place(x=1230,y=770)





def popular_section(user):
    thriller_book1_label.place_forget()
    thriller_book2_label.place_forget()
    thriller_book3_label.place_forget()
    fiction_book1_label.place_forget()
    fiction_book2_label.place_forget()
    fiction_book3_label.place_forget()
    fantasy_book1_label.place_forget()
    fantasy_book2_label.place_forget()
    fantasy_book3_label.place_forget()
    horror_book1_label.place_forget()
    horror_book2_label.place_forget()
    horror_book3_label.place_forget()
    adventure_book1_label.place_forget()
    adventure_book2_label.place_forget()
    adventure_book3_label.place_forget()
    view_fic1_button.place_forget()
    view_fic2_button.place_forget()
    view_fic3_button.place_forget()
    view_thrill1_button.place_forget()
    view_thrill2_button.place_forget()
    view_thrill3_button.place_forget()
    view_fan1_button.place_forget()
    view_fan2_button.place_forget()
    view_fan3_button.place_forget()
    view_hor1_button.place_forget()
    view_hor2_button.place_forget()
    view_hor3_button.place_forget()
    view_adv1_button.place_forget()
    view_adv2_button.place_forget()
    view_adv3_button.place_forget()
    lend_fic1_button.place_forget()
    lend_fic2_button.place_forget()
    lend_fic3_button.place_forget()
    lend_thrill1_button.place_forget()
    lend_thrill2_button.place_forget()
    lend_thrill3_button.place_forget()
    lend_fantasy1_button.place_forget()
    lend_fantasy2_button.place_forget()
    lend_fantasy3_button.place_forget()
    lend_horror1_button.place_forget()
    lend_horror2_button.place_forget()
    lend_horror3_button.place_forget()
    lend_adventure1_button.place_forget()
    lend_adventure2_button.place_forget()
    lend_adventure3_button.place_forget()
        
        
    popular_book1_label.place(x=70,y=260)
    popular_book2_label.place(x=600,y=260)
    popular_book3_label.place(x=1130,y=260)
    if user=="admin":
        lend_popular1_button.place(x=150,y=770)
        lend_popular2_button.place(x=690,y=770)
        lend_popular3_button.place(x=1230,y=770)

    else:
        view_pop1_button.place(x=150,y=770)
        view_pop2_button.place(x=690,y=770)
        view_pop3_button.place(x=1230,y=770)

    

   
def lend_borrower_info():
    new_bor_name=lend_bor_name_entry.get()
    new_borrow_date=borrow_date_entry.get()
    new_return_date=return_date_entry.get()
    new_phone_num=lend_phone_num_entry.get()
    new_address=lend_address_entry.get()
    new_book_code=lend_isbn_code_entry.get()
    new_book_name=lend_book_name_entry.get()
    new_copies_wanted=copies_wanted.get()

    myconnector=mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
    mycursor=myconnector.cursor()

    mycursor.execute(f"select * from book_info where isbn_code={book_id}")
    result=mycursor.fetchone()

    if new_bor_name==""or new_borrow_date==""or new_return_date==""or new_phone_num==""or new_address==""or new_book_code==""or new_copies_wanted==""or new_book_name=="":
         messagebox.showwarning('Liberty Library','Dont Leave fields Empty')

    else:
        is_phonenum=True
        is_newcopies=True
        if len(new_phone_num)!=10:
            messagebox.showwarning("Liberty Library","Enter the correct phone number")
            is_phonenum=False
            lend_phone_num_entry.delete(0,END)

        if int(new_copies_wanted)>int(result[-1]):
            messagebox.showwarning("Liberty Library","These many copies not available")
            is_newcopies=False
            new_copies_wanted.delete(0,END)
        
        if result[-1]<=0:
            messagebox.showwarning("Liberty Library",'This book is not available')


        else:
            if is_phonenum and is_newcopies:
                myconnector=mysql.connector.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")
                mycursor=myconnector.cursor()
                mycursor.execute(f"insert into borrower_info(bor_name,borrow_date,return_date,phone_num,book_name,isbn_code,no_of_copies,bor_address) values('{new_bor_name}','{str(new_borrow_date)}','{str(new_return_date)}',{int(new_phone_num)},'{str(new_book_name)}',{int(new_book_code)},{int(new_copies_wanted)},'{new_address}')")
                copies_left=int(result[-1])-int(new_copies_wanted)
                mycursor.execute(f"update book_info set copies={copies_left} where isbn_code={new_book_code}")
                myconnector.commit()
                myconnector.close()


                
                lend_bor_name_entry.delete(0,END)
                borrow_date_entry.delete(0,END)
                return_date_entry.delete(0,END)
                lend_phone_num_entry.delete(0,END)
                lend_address_entry.delete(0,END)
                lend_isbn_code_entry.delete(0,END)
                lend_book_name_entry.delete(0,END)
                copies_wanted.delete(0,END)

                lendpage_label.pack_forget()
                num_of_book_avail_label.place_forget()
                copies_wanted.place_forget()
                back_but_lend_to_mainpage_button.place_forget()
                lend_bor_name_entry.place_forget()
                borrow_date_entry.place_forget()
                return_date_entry.place_forget()
                lend_phone_num_entry.place_forget()
                lend_address_entry.place_forget()
                lend_isbn_code_entry.place_forget()
                lend_book_name_entry.place_forget()
                copies_wanted.place_forget()
                lend_button.place_forget()

                go_to_issue("admin")
                messagebox.showinfo("Liberty Library","Successfuly lended")

    








 #-----------------------------------------------------
#defining back
def back(here_to_there):

    login_window_label.pack_forget()
    login_username_entry.place_forget()
    login_password_entry.place_forget()
    login_continue_button.place_forget()
    back_button.place_forget()
    if_your_admin_loginpage_label.pack_forget()
    admin_username_entry.place_forget()
    admin_password_entry.place_forget()
    continue_if_your_admin_button.place_forget()
    signup_password_entry.place_forget()
    signup_username_entry.place_forget()
    signup_re_password_entry.place_forget()
    creating_account_continue_button.place_forget()
    
    dummy_start_window_label.pack()
    dummy_signupbutton_button.place(x=525,y=625)
    dummy_loginbutton_button.place(x=525,y=490)
    dummy_if_your_admin_button.place(x=580,y=740) 

    if here_to_there=='login_to_start':
        signup_window_label.pack_forget()
    
def backbutton(here_to_there):
    if here_to_there=='bor_issue_to_mainpage':
        issuepage_label.pack_forget()
        back_button_bor_issue_to_mainpage_button.place_forget()
        view_fic1_button.place_forget()
        view_fic2_button.place_forget()
        view_fic3_button.place_forget()
        view_thrill1_button.place_forget()
        view_thrill2_button.place_forget()
        view_thrill3_button.place_forget()
        view_fan1_button.place_forget()
        view_fan2_button.place_forget()
        view_fan3_button.place_forget()
        view_hor1_button.place_forget()
        view_hor2_button.place_forget()
        view_hor3_button.place_forget()
        view_adv1_button.place_forget()
        view_adv2_button.place_forget()
        view_adv3_button.place_forget()
        view_pop1_button.place_forget()
        view_pop2_button.place_forget()
        view_pop3_button.place_forget()
        fiction_book1_label.place_forget()
        fiction_book2_label.place_forget()
        fiction_book3_label.place_forget()
        thriller_book1_label.place_forget()
        thriller_book2_label.place_forget()
        thriller_book3_label.place_forget()
        fantasy_book1_label.place_forget()
        fantasy_book2_label.place_forget()
        fantasy_book3_label.place_forget()
        horror_book1_label.place_forget()
        horror_book2_label.place_forget()
        horror_book3_label.place_forget()
        adventure_book1_label.place_forget()
        adventure_book2_label.place_forget()
        adventure_book3_label.place_forget()
        popular_book1_label.place_forget()
        popular_book2_label.place_forget()
        popular_book3_label.place_forget()
        fiction_bor_issuepage_button.place_forget()
        fantasy_bor_issuepage_button.place_forget()
        thriller_bor_issuepage_button.place_forget()
        popular_bor_issuepage_button.place_forget()
        adventure_bor_issuepage_button.place_forget()
        horror_bor_issuepage_button.place_forget()
        
       
        
        
        
        

        hi_user_label.place(x=640,y=200)
        viewbooks_button.place(x=10,y=160)
        searchbook_button.place(x=10,y=250)
        logout_borrower_button.place(x=10,y=340)
        borrwer_mainpage_label.pack()

    if here_to_there=='admin_issue_to_mainpage':
        issuepage_label.pack_forget()
        back_button_admin_issue_to_mainpage_button.place_forget()
        lend_fic1_button.place_forget()
        lend_fic2_button.place_forget()
        lend_fic3_button.place_forget()
        lend_thrill1_button.place_forget()
        lend_thrill2_button.place_forget()
        lend_thrill3_button.place_forget()
        lend_fantasy1_button.place_forget()
        lend_fantasy2_button.place_forget()
        lend_fantasy3_button.place_forget()
        lend_horror1_button.place_forget()
        lend_horror2_button.place_forget()
        lend_horror3_button.place_forget()
        lend_adventure1_button.place_forget()
        lend_adventure2_button.place_forget()
        lend_adventure3_button.place_forget()
        lend_popular1_button.place_forget()
        lend_popular2_button.place_forget()
        lend_popular3_button.place_forget()
        thriller_book1_label.place_forget()
        thriller_book2_label.place_forget()
        thriller_book3_label.place_forget()
        fiction_book1_label.place_forget()
        fiction_book2_label.place_forget()
        fiction_book3_label.place_forget()
        fantasy_book1_label.place_forget()
        fantasy_book2_label.place_forget()
        fantasy_book3_label.place_forget()
        horror_book1_label.place_forget()
        horror_book2_label.place_forget()
        horror_book3_label.place_forget()
        adventure_book1_label.place_forget()
        adventure_book2_label.place_forget()
        adventure_book3_label.place_forget()
        popular_book1_label.place_forget()
        popular_book2_label.place_forget()
        popular_book3_label.place_forget()
        fiction_admin_issuepage_button.place_forget()
        fantasy_admin_issuepage_button.place_forget()
        thriller_admin_issuepage_button.place_forget()
        popular_admin_issuepage_button.place_forget()
        adventure_admin_issuepage_button.place_forget()
        horror_admin_issuepage_button.place_forget()
        




        mainpage_window_label.pack()
        dashboard_mainpage_button.place(x=10,y=200)
        issue_mainpage_button.place(x=10,y=290)
        returnbook_mainpage_button.place(x=10,y=380)
        addremove_mainpage_button.place(x=10,y=470)
        detail_mainpage_button.place(x=10,y=560)
        report_mainpage_button.place(x=10,y=650)
        logout_mainpage_button.place(x=10,y=740)
        aboutus_mainpage_button.place(x=760,y=182)


    if here_to_there=="about_to_issue":
        go_to_issue("borrower")
        about_fic1_Label.pack_forget()
        about_fic2_Label.pack_forget()
        about_fic3_Label.pack_forget()
        about_fan1_Label.pack_forget()
        about_fan2_Label.pack_forget()
        about_fan3_Label.pack_forget()
        about_adv1_label.pack_forget()
        about_adv2_label.pack_forget()
        about_adv3_label.pack_forget()
        about_hor1_label.pack_forget()
        about_hor2_label.pack_forget()
        about_hor3_label.pack_forget()
        about_thrill1_Label.pack_forget()
        about_thrill2_Label.pack_forget()
        about_thrill3_Label.pack_forget()
        about_pop1_label.pack_forget()
        about_pop2_label.pack_forget()
        about_pop3_label.pack_forget()
        available_label.place_forget()
        back_about_to_issue_button.place_forget()
        yes_label.place_forget()
        no_label.place_forget()

        issuepage_label.pack()
#from the details we get to lend page
    if here_to_there=="lend_to_main":
        lendpage_label.pack_forget()
        lend_bor_name_entry.place_forget()
        borrow_date_entry.place_forget()
        return_date_entry.place_forget()
        lend_phone_num_entry.place_forget()
        lend_isbn_code_entry.place_forget()
        lend_address_entry.place_forget()
        lend_book_name_entry.place_forget()
        num_of_book_avail_label.place_forget()
        copies_wanted.place_forget()
        lend_button.place_forget()
        back_but_lend_to_mainpage_button.place_forget()

        
        
        go_to_issue("admin")
        
    if here_to_there=="det to mainpage": 
        scrollbarx.place_forget()
        scrollbary.place_forget()
        chumma_label.pack_forget()
        back_button_det_to_mainpage_button.place_forget()
        for item in borrower_det_table.get_children():
            borrower_det_table.delete(item)
        borrower_det_table.place_forget()

        mainpage_window_label.pack()
        dashboard_mainpage_button.place(x=10,y=200)
        issue_mainpage_button.place(x=10,y=290)
        returnbook_mainpage_button.place(x=10,y=380)
        addremove_mainpage_button.place(x=10,y=470)
        detail_mainpage_button.place(x=10,y=560)
        report_mainpage_button.place(x=10,y=650)
        logout_mainpage_button.place(x=10,y=740)
        aboutus_mainpage_button.place(x=760,y=182)

    if here_to_there=="return_to_main":
        return_book_name_entry.place_forget()
        return_book_code_entry.place_forget()
        return_bor_id_entry.place_forget()
        return_button.place_forget()
        return_bor_name_entry.place_forget()
        back_return_to_mainpage_button.place_forget()
        return_page_label.pack_forget()
        get_info_Button.place_forget()
        return_book_code_entry.delete(0,END)
        return_book_name_entry.delete(0,END)
        return_bor_id_entry.delete(0,END)
        return_bor_name_entry.delete(0,END)
        return_book_name_entry.config(state="disabled")
        return_book_code_entry.config(state="disabled")
        return_bor_name_entry.config(state="disabled")





        mainpage_window_label.pack()
        dashboard_mainpage_button.place(x=10,y=200)
        issue_mainpage_button.place(x=10,y=290)
        returnbook_mainpage_button.place(x=10,y=380)
        addremove_mainpage_button.place(x=10,y=470)
        detail_mainpage_button.place(x=10,y=560)
        report_mainpage_button.place(x=10,y=650)
        logout_mainpage_button.place(x=10,y=740)
        aboutus_mainpage_button.place(x=760,y=182)

    
    if here_to_there=='addpage_to_addbook':
        addbook_book_name_entry.place_forget()
        addbook_book_id_entry.place_forget()
        addbook_author_entry.place_forget()
        addbook_rating_entry.place_forget()
        addbook_genre_entry.place_forget()
        addbook_num_of_copies_entry.place_forget()
        add_book_another_button.place_forget()
        addbook_page_label.pack_forget()
        back_addpage_to_addbookpage_button.place_forget()


        book_det_table.place(relx=0.05,rely=0.22,width=1300,height=500)
        scrollbary1.place(relx=0.934,rely=0.22,width=22,height=432)
        scrollbarx1.place(relx=0.08,rely=0.830,width=1000,height=22)
        chumma_label.pack()
        addbook_button.place(x=1220,y=700)
        remove_book_button.place(x=30,y=750)
        back_addbookpage_to_mainpage_button.place(x=20,y=20)

    if here_to_there=='addbookpage_to_mainpage':
        book_det_table.place_forget()
        scrollbarx1.place_forget()
        scrollbary1.place_forget()
        addbook_button.place_forget()
        remove_book_button.place_forget()
        back_addbookpage_to_mainpage_button.place_forget()
        chumma_label.pack_forget()

        mainpage_window_label.pack()
        dashboard_mainpage_button.place(x=10,y=200)
        issue_mainpage_button.place(x=10,y=290)
        returnbook_mainpage_button.place(x=10,y=380)
        addremove_mainpage_button.place(x=10,y=470)
        detail_mainpage_button.place(x=10,y=560)
        report_mainpage_button.place(x=10,y=650)
        logout_mainpage_button.place(x=10,y=740)
        aboutus_mainpage_button.place(x=760,y=182)
        for item in book_det_table.get_children():
            book_det_table.delete(item)
        book_det_table.place_forget()


    if here_to_there=="defaulter_to_mainpage":
        
        scrollbarx2.place_forget()
        scrollbary2.place_forget()
        chumma_label.pack_forget()
        back_defaulter_to_mainpage_button.place_forget()

        mainpage_window_label.pack()
        dashboard_mainpage_button.place(x=10,y=200)
        issue_mainpage_button.place(x=10,y=290)
        returnbook_mainpage_button.place(x=10,y=380)
        addremove_mainpage_button.place(x=10,y=470)
        detail_mainpage_button.place(x=10,y=560)
        report_mainpage_button.place(x=10,y=650)
        logout_mainpage_button.place(x=10,y=740)
        aboutus_mainpage_button.place(x=760,y=182)
        for item in defaulters_det_table.get_children():
            defaulters_det_table.delete(item)
        defaulters_det_table.place_forget()

    if here_to_there=="search_to_mainpage":
        back_search_to_mainpage_button.place_forget()
        search_table.place_forget()
        scrollbarx3.place_forget()
        scrollbary3.place_forget()
        search_actual_button.place_forget()
        bookname_search_entry.place_forget()
        Authorname_search_entry.place_forget()
        search_page_label.pack_forget()

            
        hi_user_label.place(x=640,y=200)
        viewbooks_button.place(x=10,y=160)
        searchbook_button.place(x=10,y=250)
        logout_borrower_button.place(x=10,y=340)
        borrwer_mainpage_label.pack()
        for item in search_table.get_children():
            search_table.delete(item)

    if here_to_there=="aboutus_to_mainpage":
        aboutus_page_label.pack_forget()
        back_aboutus_to_mainpage_button.place_forget()
        mainpage_window_label.pack()
        dashboard_mainpage_button.place(x=10,y=200)
        issue_mainpage_button.place(x=10,y=290)
        returnbook_mainpage_button.place(x=10,y=380)
        addremove_mainpage_button.place(x=10,y=470)
        detail_mainpage_button.place(x=10,y=560)
        report_mainpage_button.place(x=10,y=650)
        logout_mainpage_button.place(x=10,y=740)
        aboutus_mainpage_button.place(x=760,y=182)

    
#Image
start_window_Image=ImageTk.PhotoImage(file="pics\starting page\START  WINDOW BG (1).png")
start_window_label=Label(root,image=start_window_Image)
start_window_label.pack() 

dummy_start_window_Image=ImageTk.PhotoImage(file="pics\starting page\START  WINDOW BG (1).png")
dummy_start_window_label=Label(root,image=dummy_start_window_Image)

login_window_image=ImageTk.PhotoImage(file='pics\login page\login window.png')
login_window_label=Label(root,image=login_window_image)

if_your_admin_loginpage_image=ImageTk.PhotoImage(file='pics\login page\login window.png')
if_your_admin_loginpage_label=Label(root,image=if_your_admin_loginpage_image)

mainpage_window_image=ImageTk.PhotoImage(file="pics\Mainpage (1).png")
mainpage_window_label=Label(root,image=mainpage_window_image)

signup_window_image=ImageTk.PhotoImage(file="pics\sign up page\sign up page.png")
signup_window_label=Label(root,image=signup_window_image)


issuepage_image=ImageTk.PhotoImage(file="pics\Issue_return fol\issue page (1).png")
issuepage_label=Label(root,image=issuepage_image)

lendpage_image=ImageTk.PhotoImage(file="pics\lend page new.png")
lendpage_label=Label(root,image=lendpage_image)


borrower_mainpage_image=ImageTk.PhotoImage(file="pics\Borrower mainpagae\Borrower mainpage.png")
borrwer_mainpage_label=Label(root,image=borrower_mainpage_image)





#book label

fiction_book1_image=ImageTk.PhotoImage(file="pics\Books\All\Fiction\harry potter.png")
fiction_book1_label=Label(root,image=fiction_book1_image)

fiction_book2_image=ImageTk.PhotoImage(file="pics\Books\All\Fiction\Book fic2.png")
fiction_book2_label=Label(root,image=fiction_book2_image)

fiction_book3_image=ImageTk.PhotoImage(file="pics\Books\All\Fiction\Book fic3.png")
fiction_book3_label=Label(root,image=fiction_book3_image)

thriller_book1_image=ImageTk.PhotoImage(file='pics\Books\All\Thriller\Thrill1.png')
thriller_book1_label=Label(root,image=thriller_book1_image)

thriller_book2_image=ImageTk.PhotoImage(file='pics\Books\All\Thriller\Thrill2.png')
thriller_book2_label=Label(root,image=thriller_book2_image)

thriller_book3_image=ImageTk.PhotoImage(file='pics\Books\All\Thriller\Thrill3.png')
thriller_book3_label=Label(root,image=thriller_book3_image)

fantasy_book1_image=ImageTk.PhotoImage(file='pics\Books\All\Fantasy\Fan1.png')
fantasy_book1_label=Label(root,image=fantasy_book1_image)

fantasy_book2_image=ImageTk.PhotoImage(file='pics\Books\All\Fantasy\Fan2.png')
fantasy_book2_label=Label(root,image=fantasy_book2_image)

fantasy_book3_image=ImageTk.PhotoImage(file='pics\Books\All\Fantasy\Fan3.png')
fantasy_book3_label=Label(root,image=fantasy_book3_image)

horror_book1_image=ImageTk.PhotoImage(file='pics\Books\All\Horror\Hor1.png')
horror_book1_label=Label(root,image=horror_book1_image)

horror_book2_image=ImageTk.PhotoImage(file='pics\Books\All\Horror\Hor2.png')
horror_book2_label=Label(root,image=horror_book2_image)

horror_book3_image=ImageTk.PhotoImage(file='pics\Books\All\Horror\Hor3.png')
horror_book3_label=Label(root,image=horror_book3_image)

adventure_book1_image=ImageTk.PhotoImage(file='pics\Books\All\Adventure\Adv1.png')
adventure_book1_label=Label(root,image=adventure_book1_image)

adventure_book2_image=ImageTk.PhotoImage(file='pics\Books\All\Adventure\Adv2.png')
adventure_book2_label=Label(root,image=adventure_book2_image)

adventure_book3_image=ImageTk.PhotoImage(file='pics\Books\All\Adventure\Adv3.png')
adventure_book3_label=Label(root,image=adventure_book3_image)

popular_book1_image=ImageTk.PhotoImage(file='pics\Books\All\Popular\Pop1.png')
popular_book1_label=Label(root,image=popular_book1_image)

popular_book2_image=ImageTk.PhotoImage(file='pics\Books\All\Popular\Pop2.png')
popular_book2_label=Label(root,image=popular_book2_image)

popular_book3_image=ImageTk.PhotoImage(file='pics\Books\All\Popular\Pop3.png')
popular_book3_label=Label(root,image=popular_book3_image)

#about books
about_fic1_image=ImageTk.PhotoImage(file="pics\Books\All\Fiction\Fic1.png")
about_fic1_Label=Label(root,image=about_fic1_image)

about_fic2_image=ImageTk.PhotoImage(file="pics\Books\All\Fiction\Fic2.png")
about_fic2_Label=Label(root,image=about_fic2_image)

about_fic3_image=ImageTk.PhotoImage(file="pics\Books\All\Fiction\Fic3.png")
about_fic3_Label=Label(root,image=about_fic3_image)

about_thrill1_image=ImageTk.PhotoImage(file="pics\Books\All\Thriller\Aboutthrill1.png")
about_thrill1_Label=Label(root,image=about_thrill1_image)

about_thrill2_image=ImageTk.PhotoImage(file="pics\Books\All\Thriller\Aboutthrill2.png")
about_thrill2_Label=Label(root,image=about_thrill2_image)

about_thrill3_image=ImageTk.PhotoImage(file="pics\Books\All\Thriller\Aboutthrill3.png")
about_thrill3_Label=Label(root,image=about_thrill3_image)

about_fan1_image=ImageTk.PhotoImage(file="pics\Books\All\Fantasy\Aboutfan1.png")
about_fan1_Label=Label(root,image=about_fan1_image)

about_fan2_image=ImageTk.PhotoImage(file="pics\Books\All\Fantasy\Aboutfan2 (2).png")
about_fan2_Label=Label(root,image=about_fan2_image)

about_fan3_image=ImageTk.PhotoImage(file="pics\Books\All\Fantasy\Aboutfan3 (2).png")
about_fan3_Label=Label(root,image=about_fan3_image)

about_hor1_image=ImageTk.PhotoImage(file="pics\Books\All\Horror\Abouthor1.png")
about_hor1_label=Label(root,image=about_hor1_image)

about_hor2_image=ImageTk.PhotoImage(file="pics\Books\All\Horror\Abouthor2.png")
about_hor2_label=Label(root,image=about_hor2_image)

about_hor3_image=ImageTk.PhotoImage(file="pics\Books\All\Horror\Abouthor3.png")
about_hor3_label=Label(root,image=about_hor3_image)

about_adv1_image=ImageTk.PhotoImage(file="pics\Books\All\Adventure\Aboutadv1.png")
about_adv1_label=Label(root,image=about_adv1_image)

about_adv2_image=ImageTk.PhotoImage(file="pics\Books\All\Adventure\Aboutadv2.png")
about_adv2_label=Label(root,image=about_adv2_image)

about_adv3_image=ImageTk.PhotoImage(file="pics\Books\All\Adventure\Aboutadv3.png")
about_adv3_label=Label(root,image=about_adv3_image)

about_pop1_image=ImageTk.PhotoImage(file="pics\Books\All\Popular\Aboutpop1.png")
about_pop1_label=Label(root,image=about_pop1_image)

about_pop2_image=ImageTk.PhotoImage(file="pics\Books\All\Popular\Aboutpop2.png")
about_pop2_label=Label(root,image=about_pop2_image)

about_pop3_image=ImageTk.PhotoImage(file="pics\Books\All\Popular\Aboutpop3.png")
about_pop3_label=Label(root,image=about_pop3_image)


#yes no label
yes_label_image=ImageTk.PhotoImage(file="pics\Issue_return fol\YES label new.png")
yes_label=Label(root,image=yes_label_image,background="#191926")


no_label_image=ImageTk.PhotoImage(file="pics\Issue_return fol\_NO label new.png")
no_label=Label(root,image=no_label_image,background="#191926")
#chumma
chumma_image=ImageTk.PhotoImage(file="pics\chumma.png")
chumma_label=Label(root,image=chumma_image)

#return page
return_page_image=ImageTk.PhotoImage(file="pics\Issue_return fol\Return page new.png")
return_page_label=Label(root,image=return_page_image)

#Addbook

addbook_page_image=ImageTk.PhotoImage(file="pics\Add book fol\Add book page.png")
addbook_page_label=Label(root,image=addbook_page_image)

#search book

search_page_image=ImageTk.PhotoImage(file="pics\Search page.png")
search_page_label=Label(root,image=search_page_image)

#aboutus
aboutus_page_image=ImageTk.PhotoImage(file="pics\Aboutus page.png")
aboutus_page_label=Label(root,image=aboutus_page_image)






#Buttons




#backbutton
back_button_Image=ImageTk.PhotoImage(file="Back button.png")
back_button=Button(root,image=back_button_Image,background="#191926",borderwidth=0,activebackground="#191926",command=lambda:back('login_to_start'))

back_about_to_issue_image=ImageTk.PhotoImage(file="Back button.png")
back_about_to_issue_button=Button(root,image=back_button_Image,background="#191926",borderwidth=0,activebackground="#191926",command=lambda:backbutton('about_to_issue'))
#Starting window Buttons
signup_button_Image=ImageTk.PhotoImage(file="SIGN UP.png")
signup_button=Button(root,background="#191926",borderwidth=0,image=signup_button_Image,command=go_to_signup_page,activebackground="#191926")
signup_button.place(x=525,y=625)

dummy_signupbutton_Image=ImageTk.PhotoImage(file="SIGN UP copy.png")
dummy_signupbutton_button=Button(root,background="#191926",borderwidth=0,image=dummy_signupbutton_Image,command=go_to_signup_page,activebackground="#191926")

login_button_Image=ImageTk.PhotoImage(file="LOG IN.png")
login_button=Button(root,background="#191926",borderwidth=0,image=login_button_Image,command=click_login,activebackground="#191926")
login_button.place(x=525,y=490)

dummy_loginbutton_image=ImageTk.PhotoImage(file="LOG IN copy.png")
dummy_loginbutton_button=Button(root,background="#191926",borderwidth=0,image=dummy_loginbutton_image,command=click_login,activebackground="#191926")

#if your admin button
if_your_admin_Image=ImageTk.PhotoImage(file="pics\sign up page\if your admin button.png")
if_your_admin_Button=Button(root,image=if_your_admin_Image,background="#191926",borderwidth=0,activebackground="#191926",command=if_your_admin_page)
if_your_admin_Button.place(x=580,y=740)

dummy_if_your_admin_Image=ImageTk.PhotoImage(file="pics\sign up page\if your admin button.png")
dummy_if_your_admin_button=Button(root,image=dummy_if_your_admin_Image,background="#191926",borderwidth=0,activebackground="#191926",command=if_your_admin_page)

continue_if_your_admin_image=ImageTk.PhotoImage(file="pics\login page\loginbutton_continue.png")
continue_if_your_admin_button=Button(root,background="#191926",borderwidth=0,image=continue_if_your_admin_image,command=admin_main_page,activebackground="#191926")
#login window Buttons
login_continue_button_Image=ImageTk.PhotoImage(file="pics\login page\loginbutton_continue.png")
login_continue_button=Button(root,background="#191926",borderwidth=0,image=login_continue_button_Image,command=go_to_mainpage,activebackground="#191926")


#creating account buttons
creating_account_continue_Image=ImageTk.PhotoImage(file="pics\login page\loginbutton_continue.png")
creating_account_continue_button=Button(root,background="#191926",borderwidth=0,image=login_continue_button_Image,command=go_to_start,activebackground="#191926")


#main window Buttons
dashboard_mainpage_image=ImageTk.PhotoImage(file="pics\mainpage\dashboard buttn.png")
dashboard_mainpage_button=Button(root,background="#191926",borderwidth=0,image=dashboard_mainpage_image,activebackground="#191926",command=go_to_dashboard)

issue_mainpage_image=ImageTk.PhotoImage(file="pics\mainpage\Issue button.png")
issue_mainpage_button=Button(root,image=issue_mainpage_image,background="#191926",borderwidth=0,activebackground="#191926",command=lambda:go_to_issue("admin"))
#buttons in issue page

fiction_admin_issuepage_image=ImageTk.PhotoImage(file="pics\Issue_return fol\_fiction button.png")
fiction_admin_issuepage_button=Button(root,image=fiction_admin_issuepage_image,background="#000000",borderwidth=0,activebackground="#000000",command=lambda:fiction_click("admin"))

fiction_bor_issuepage_image=ImageTk.PhotoImage(file="pics\Issue_return fol\_fiction button.png")
fiction_bor_issuepage_button=Button(root,image=fiction_admin_issuepage_image,background="#000000",borderwidth=0,activebackground="#000000",command=lambda:fiction_click("borrower"))

thriller_admin_issuepage_image=ImageTk.PhotoImage(file="pics\Issue_return fol\_thriller button.png")
thriller_admin_issuepage_button=Button(root,image=thriller_admin_issuepage_image,background="#000000",borderwidth=0,activebackground="#000000",command=lambda:thriller_section("admin"))

thriller_bor_issuepage_image=ImageTk.PhotoImage(file="pics\Issue_return fol\_thriller button.png")
thriller_bor_issuepage_button=Button(root,image=thriller_bor_issuepage_image,background="#000000",borderwidth=0,activebackground="#000000",command=lambda:thriller_section("borrower"))

fantasy_admin_issuepage_image=ImageTk.PhotoImage(file="pics\Issue_return fol\_fantasy button.png")
fantasy_admin_issuepage_button=Button(root,image=fantasy_admin_issuepage_image,background="#000000",borderwidth=0,activebackground="#000000",command=lambda:fantasy_section("admin"))

fantasy_bor_issuepage_image=ImageTk.PhotoImage(file="pics\Issue_return fol\_fantasy button.png")
fantasy_bor_issuepage_button=Button(root,image=fantasy_bor_issuepage_image,background="#000000",borderwidth=0,activebackground="#000000",command=lambda:fantasy_section("borrower"))

horror_admin_issuepage_image=ImageTk.PhotoImage(file="pics\Issue_return fol\horror button.png")
horror_admin_issuepage_button=Button(root,image=horror_admin_issuepage_image,background="#000000",borderwidth=0,activebackground="#000000",command=lambda:horror_section("admin"))

horror_bor_issuepage_image=ImageTk.PhotoImage(file="pics\Issue_return fol\horror button.png")
horror_bor_issuepage_button=Button(root,image=horror_bor_issuepage_image,background="#000000",borderwidth=0,activebackground="#000000",command=lambda:horror_section("borrower"))

adventure_admin_issuepage_image=ImageTk.PhotoImage(file="pics\Issue_return fol\_adventure button.png")
adventure_admin_issuepage_button=Button(root,image=adventure_admin_issuepage_image,background="#000000",borderwidth=0,activebackground="#000000",command=lambda:adventure_section("admin"))

adventure_bor_issuepage_image=ImageTk.PhotoImage(file="pics\Issue_return fol\_adventure button.png")
adventure_bor_issuepage_button=Button(root,image=adventure_bor_issuepage_image,background="#000000",borderwidth=0,activebackground="#000000",command=lambda:adventure_section("borrower"))

popular_admin_issuepage_image=ImageTk.PhotoImage(file="pics\Issue_return fol\popular button.png")
popular_admin_issuepage_button=Button(root,image=popular_admin_issuepage_image,background="#000000",borderwidth=0,activebackground="#000000",command=lambda:popular_section("admin"))

popular_bor_issuepage_image=ImageTk.PhotoImage(file="pics\Issue_return fol\popular button.png")
popular_bor_issuepage_button=Button(root,image=popular_bor_issuepage_image,background="#000000",borderwidth=0,activebackground="#000000",command=lambda:popular_section("borrower"))



#lend buttons


lend_fic1_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_fic1_button=Button(root,image=lend_fic1_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendfic_page(1))

lend_fic2_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_fic2_button=Button(root,image=lend_fic2_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendfic_page(2))

lend_fic3_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_fic3_button=Button(root,image=lend_fic3_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendfic_page(3))


lend_thrill1_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_thrill1_button=Button(root,image=lend_thrill1_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendthrill_page(4))

lend_thrill2_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_thrill2_button=Button(root,image=lend_thrill2_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendthrill_page(6))

lend_thrill3_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_thrill3_button=Button(root,image=lend_thrill3_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendthrill_page(5))

lend_fantasy1_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_fantasy1_button=Button(root,image=lend_fantasy1_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendfantasy_page(8))

lend_fantasy2_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_fantasy2_button=Button(root,image=lend_fantasy2_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendfantasy_page(9))

lend_fantasy3_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_fantasy3_button=Button(root,image=lend_fantasy3_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendfantasy_page(7))


lend_horror1_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_horror1_button=Button(root,image=lend_horror1_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendhorror_page(10))

lend_horror2_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_horror2_button=Button(root,image=lend_horror2_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendhorror_page(12))

lend_horror3_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_horror3_button=Button(root,image=lend_horror3_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendhorror_page(11))


lend_adventure1_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_adventure1_button=Button(root,image=lend_adventure1_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendadventure_page(15))

lend_adventure2_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_adventure2_button=Button(root,image=lend_adventure2_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendadventure_page(13))

lend_adventure3_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_adventure3_button=Button(root,image=lend_adventure3_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendadventure_page(14))


lend_popular1_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_popular1_button=Button(root,image=lend_popular1_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendpopular_page(16))

lend_popular2_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_popular2_button=Button(root,image=lend_popular2_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendpopular_page(18))

lend_popular3_image=ImageTk.PhotoImage(file="Lend button (1).png")
lend_popular3_button=Button(root,image=lend_popular2_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:lendpopular_page(17))



#buttons in mainpage

returnbook_mainpage_image=ImageTk.PhotoImage(file="pics\mainpage\_return button.png")
returnbook_mainpage_button=Button(root,image=returnbook_mainpage_image,background="#191926",borderwidth=0,activebackground="#191926",command=go_to_returnbook)

addremove_mainpage_image=ImageTk.PhotoImage(file="pics\_addremove button.png")
addremove_mainpage_button=Button(root,image=addremove_mainpage_image,background="#191926",borderwidth=0,activebackground="#191926",command=go_to_addremovebook)

detail_mainpage_image=ImageTk.PhotoImage(file="pics\mainpage\Details button.png")
detail_mainpage_button=Button(root,image=detail_mainpage_image,background="#191926",borderwidth=0,activebackground="#191926",command=go_to_detail)


report_mainpage_image=ImageTk.PhotoImage(file="pics\mainpage\Defaulters button.png")
report_mainpage_button=Button(root,image=report_mainpage_image,background="#191926",borderwidth=0,activebackground="#191926",command=go_to_defaulter)

logout_mainpage_image=ImageTk.PhotoImage(file="pics\mainpage\Log out button (1).png")
logout_mainpage_button=Button(root,image=logout_mainpage_image,background="#191926",borderwidth=0,activebackground="#191926",command=lambda:go_to_logout("admin"))

aboutus_mainpage_image=ImageTk.PhotoImage(file="pics\mainpage\About us button.png")

aboutus_mainpage_button=Button(root,image=aboutus_mainpage_image,background="#191926",borderwidth=0,activebackground="#191926",command=go_to_aboutus)



#buttons in borrower mainpage
viewbooks_image=ImageTk.PhotoImage(file="pics\Borrower mainpagae\Viewbooks button.png")
viewbooks_button=Button(root,image=viewbooks_image,background="#191926",borderwidth=0,activebackground="#191926",command=lambda:go_to_issue('borrower'))

searchbook_image=ImageTk.PhotoImage(file="pics\Borrower mainpagae\search book.png")
searchbook_button=Button(root,image=searchbook_image,background="#191926",borderwidth=0,activebackground="#191926",command=go_to_searchpage)

logout_borrower_image=ImageTk.PhotoImage(file="pics\mainpage\Log out button (1).png")
logout_borrower_button=Button(root,image=logout_borrower_image,background="#191926",borderwidth=0,activebackground="#191926",command=lambda:go_to_logout("bor"))

#buttons in borrower issuepage
view_fic1_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_fic1_button=Button(root,image=view_fic1_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewfic_page(1))

view_fic2_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_fic2_button=Button(root,image=view_fic2_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewfic_page(2))

view_fic3_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_fic3_button=Button(root,image=view_fic3_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewfic_page(3))



view_thrill1_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_thrill1_button=Button(root,image=view_thrill1_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewthrill_page(1))

view_thrill2_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_thrill2_button=Button(root,image=view_thrill2_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewthrill_page(2))

view_thrill3_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_thrill3_button=Button(root,image=view_thrill3_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewthrill_page(3))

view_fan1_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_fan1_button=Button(root,image=view_fan1_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewfan_page(1))

view_fan2_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_fan2_button=Button(root,image=view_fan2_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewfan_page(2))

view_fan3_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_fan3_button=Button(root,image=view_fan3_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewfan_page(3))

view_hor1_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_hor1_button=Button(root,image=view_hor1_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewhor_page(1))

view_hor2_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_hor2_button=Button(root,image=view_hor2_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewhor_page(2))

view_hor3_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_hor3_button=Button(root,image=view_hor3_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewhor_page(3))

view_adv1_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_adv1_button=Button(root,image=view_adv1_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewadv_page(1))

view_adv2_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_adv2_button=Button(root,image=view_adv2_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewadv_page(2))

view_adv3_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_adv3_button=Button(root,image=view_adv3_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewadv_page(3))

view_pop1_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_pop1_button=Button(root,image=view_pop1_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewpop_page(1))

view_pop2_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_pop2_button=Button(root,image=view_pop2_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewpop_page(2))

view_pop3_image=ImageTk.PhotoImage(file="pics\Issue_return fol\View button.png")
view_pop3_button=Button(root,image=view_pop3_image,background="#191926",borderwidth=0,activebackground="#000000",command=lambda:viewpop_page(3))






lend_button_image=ImageTk.PhotoImage(file="pics\Issue_return fol\lend button new.png")
lend_button=Button(root,image=lend_button_image,background="#191926",borderwidth=0,activebackground="#191926",command=lend_borrower_info)


search_actual_button_image=ImageTk.PhotoImage(file="pics\Search buttom.png")
search_actual_button=Button(root,image=search_actual_button_image,background="#191926",borderwidth=0,activebackground="#191926",command=search)

back_button_bor_issue_to_mainpage_Image=ImageTk.PhotoImage(file="Back button.png")
back_button_bor_issue_to_mainpage_button=Button(root,image=back_button_Image,background="#191926",borderwidth=0,activebackground="#191926",command=lambda:backbutton('bor_issue_to_mainpage'))

back_button_admin_issue_to_mainpage_Image=ImageTk.PhotoImage(file="Back button.png")
back_button_admin_issue_to_mainpage_button=Button(root,image=back_button_Image,background="#191926",borderwidth=0,activebackground="#191926",command=lambda:backbutton('admin_issue_to_mainpage'))

back_button_det_to_mainpage_image=ImageTk.PhotoImage(file="Back button.png")
back_button_det_to_mainpage_button=Button(root,image=back_button_Image,background="#191926",borderwidth=0,activebackground="#191926",command=lambda:backbutton('det to mainpage'))

back_but_lend_to_mainpage_image=ImageTk.PhotoImage(file="Back button.png")
back_but_lend_to_mainpage_button=Button(root,image=back_but_lend_to_mainpage_image,background="#191926",borderwidth=0,activebackground="#191926",command=lambda:backbutton('lend_to_main'))

back_return_to_mainpage_image=ImageTk.PhotoImage(file="Back button.png")
back_return_to_mainpage_button=Button(root,image=back_return_to_mainpage_image,background="#191926",borderwidth=0,activebackground="#191926",command=lambda:backbutton('return_to_main'))

back_addpage_to_addbookpage_image=ImageTk.PhotoImage(file="Back button.png")
back_addpage_to_addbookpage_button=Button(root,image=back_addpage_to_addbookpage_image,background="#191926",borderwidth=0,activebackground="#191926",command=lambda:backbutton('addpage_to_addbook'))

back_addbookpage_to_mainpage_image=ImageTk.PhotoImage(file="Back button.png")
back_addbookpage_to_mainpage_button=Button(root,image=back_addbookpage_to_mainpage_image,background="#191926",borderwidth=0,activebackground="#191926",command=lambda:backbutton('addbookpage_to_mainpage'))

back_defaulter_to_mainpage_image=ImageTk.PhotoImage(file="Back button.png")
back_defaulter_to_mainpage_button=Button(root,image=back_defaulter_to_mainpage_image,background="#191926",borderwidth=0,activebackground="#191926",command=lambda:backbutton('defaulter_to_mainpage'))

back_search_to_mainpage_image=ImageTk.PhotoImage(file="Back button.png")
back_search_to_mainpage_button=Button(root,image=back_search_to_mainpage_image,background="#191926",borderwidth=0,activebackground="#191926",command=lambda:backbutton('search_to_mainpage'))

back_aboutus_to_mainpage_image=ImageTk.PhotoImage(file="Back button.png")
back_aboutus_to_mainpage_button=Button(root,image=back_aboutus_to_mainpage_image,background="#191926",borderwidth=0,activebackground="#191926",command=lambda:backbutton('aboutus_to_mainpage'))

#return page

return_button_image=ImageTk.PhotoImage(file="pics\Issue_return fol\Reutrn button.png")
return_button=Button(root,image=return_button_image,background="#191926",borderwidth=0,activebackground="#191926",command=return_book)

get_info_image=ImageTk.PhotoImage(file="pics\Issue_return fol\Get info button.png")
get_info_Button=Button(root,image=get_info_image,background="#191926",borderwidth=0,activebackground="#191926",command=get_return_info)


#addremove page
addbook_button_image=ImageTk.PhotoImage(file="pics\Add book fol\Add book button.png")
addbook_button=Button(root,image=addbook_button_image,background="#191926",borderwidth=0,activebackground="#191926",command=go_to_addbook_page)

add_book_another_button_image=ImageTk.PhotoImage(file="pics\Add book fol\Add book button.png")
add_book_another_button=Button(root,image=add_book_another_button_image,background="#191926",borderwidth=0,activebackground="#191926",command=addbook_to_library)

remove_book_button_image=ImageTk.PhotoImage(file="pics\Add book fol\Remove button.png")
remove_book_button=Button(root,image=remove_book_button_image,background="#191926",borderwidth=0,activebackground="#191926",command=remove_book_from_lib)
#entries

login_username_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
login_password_entry=Entry(root,width=20,font=("Heveltica",25),bg="white",borderwidth=0,show='•')

signup_username_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
signup_password_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
signup_re_password_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)

admin_username_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
admin_password_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0,show='•')
 

lend_bor_name_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
lend_phone_num_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
lend_book_name_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
lend_isbn_code_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
lend_address_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)

copies_wanted=Entry(root,width=5,font=('Heveltica',25),bg="white",borderwidth=0)

return_bor_name_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
return_bor_id_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
return_book_name_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
return_book_code_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)

return_book_code_entry.config(state="disabled")
return_bor_name_entry.config(state="disabled")
return_book_name_entry.config(state="disabled")

addbook_book_name_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
addbook_author_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
addbook_rating_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
addbook_genre_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
addbook_num_of_copies_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
addbook_book_id_entry=Entry(root,width=5,font=('Heveltica',25),bg="white",borderwidth=0)


bookname_search_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)
Authorname_search_entry=Entry(root,width=20,font=('Heveltica',25),bg="white",borderwidth=0)



#calendar
borrow_date_entry=Entry(root,highlightthickness=0, relief=FLAT,bg="white",borderwidth=0,font=('Heveltica',25))
borrow_date_entry.insert(0,"dd/mm/yyyy")
borrow_date_entry.bind("<1>",borrow_pick_date)

return_date_entry=Entry(root,highlightthickness=0, relief=FLAT,bg="white",borderwidth=0,font=('Heveltica',25))
return_date_entry.insert(0,"dd/mm/yyyy")
return_date_entry.bind("<1>",return_pick_date)

#tables

style=ttk.Style()
style.theme_use("default")
style.configure("Treeview",rowheight=30)


borrower_det_table=ttk.Treeview(root,columns=('Id','Name','Borrow date','Return date','Phone Number','Borrowed book','Book code','Copies borrowed','Address'),show='headings')
borrower_det_table.heading('Id',text='Id')
borrower_det_table.heading('Name',text='Name')
borrower_det_table.heading('Borrow date',text='Borrow date')
borrower_det_table.heading('Return date',text='Return date')
borrower_det_table.heading('Phone Number',text='Phone Number')
borrower_det_table.heading('Borrowed book',text='Borrowed book')
borrower_det_table.heading('Book code',text='Book code')
borrower_det_table.heading('Copies borrowed',text='Copies borrowed')
borrower_det_table.heading('Address',text='Address')

borrower_det_table.column('Id',width=30)



scrollbarx=Scrollbar(root,orient=HORIZONTAL)
scrollbary=Scrollbar(root,orient=VERTICAL)

borrower_det_table.configure(yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
borrower_det_table.configure(selectmode="extended")
scrollbary.configure(command=borrower_det_table.yview)
scrollbarx.configure(command=borrower_det_table.xview)





book_det_table=ttk.Treeview(root,columns=('Book code','Book Name','Author','Edition','Rating','Genre','Copies'),show='headings')
book_det_table.heading('Book code',text='Book code')
book_det_table.heading('Book Name',text='Book Name')
book_det_table.heading('Author',text='Author')
book_det_table.heading('Edition',text='Edition')
book_det_table.heading('Rating',text='Rating')
book_det_table.heading('Genre',text='Genre')
book_det_table.heading('Copies',text='Copies')


scrollbarx1=Scrollbar(root,orient=HORIZONTAL)
scrollbary1=Scrollbar(root,orient=VERTICAL)

book_det_table.configure(yscrollcommand=scrollbary1.set,xscrollcommand=scrollbarx1.set)
book_det_table.configure(selectmode="extended")
scrollbary1.configure(command=book_det_table.yview)
scrollbarx1.configure(command=book_det_table.xview)


defaulters_det_table=ttk.Treeview(root,columns=('Borrower Id','Name','Borrow date','Return date','Phone num','Book name','Copies'),show='headings')
defaulters_det_table.heading('Borrower Id',text='Borrower Id')
defaulters_det_table.heading('Name',text='Name')
defaulters_det_table.heading('Borrow date',text='Borrow date')
defaulters_det_table.heading('Return date',text='Return date')
defaulters_det_table.heading('Phone num',text='Phone num')
defaulters_det_table.heading('Book name',text='Book name')
defaulters_det_table.heading('Copies',text='Copies')


scrollbarx2=Scrollbar(root,orient=HORIZONTAL)
scrollbary2=Scrollbar(root,orient=VERTICAL)

defaulters_det_table.configure(yscrollcommand=scrollbary2.set,xscrollcommand=scrollbarx2.set)
defaulters_det_table.configure(selectmode="extended")
scrollbary2.configure(command=defaulters_det_table.yview)
scrollbarx2.configure(command=defaulters_det_table.xview)


search_table=ttk.Treeview(root,columns=('Book code','Book Name','Author','Edition','Rating','Genre','Copies'),show='headings')
search_table.heading('Book Name',text='Book Name')
search_table.heading('Author',text='Author')
search_table.heading('Book code',text='Book code')
search_table.heading('Edition',text='Edition')
search_table.heading('Rating',text='Rating')
search_table.heading('Genre',text='Genre')
search_table.heading('Copies',text='Copies')

scrollbarx3=Scrollbar(root,orient=HORIZONTAL)
scrollbary3=Scrollbar(root,orient=VERTICAL)


search_table.configure(yscrollcommand=scrollbary3.set,xscrollcommand=scrollbarx3.set)
search_table.configure(selectmode="extended")
scrollbary3.configure(command=search_table.yview)
scrollbarx3.configure(command=search_table.xview)



root.mainloop()