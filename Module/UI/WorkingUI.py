from tkinter import*
import tkinter.messagebox
from tkinter import ttk

def main():
    root = Tk()
    app = PMLogin(root)

# Login window ============================================
class WindowPMLogin:
    def __init__(self, master):
        self.master = master
        self.master.title("Parking Management : Login")
        self.master.geometry("351x304+477+130")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()
        
        self.LabelTitle = Label(self.frame, text = 'Parking Management System', font = ('arial', 50, 'bold'), bd = 20)
        self.LabelTitle.grid(row=0, column=0, columnspan =1, pady =40)

        # self.Loginframe = LabelFrame(self.frame, width = 1010, height = 600, font = ('srial', 20, 'bold'), relief = 'ridge')
        # self.Loginframe.grid(row=1, column = 0)

        # self.Loginframe = LabelFrame(self.frame, width = 1010, height = 600, font = ('srial', 20, 'bold'), relief = 'ridge')
        # self.Loginframe.grid(row=1, column = 0)

        # self.Loginframe = LabelFrame(self.frame, width = 1010, height = 600, font = ('srial', 20, 'bold'), relief = 'ridge')
        # self.Loginframe.grid(row=1, column = 0)

        self.Loginframe = LabelFrame(self.frame)
        self.Loginframe.place(relx=0.028, rely=0.033, relheight=0.938, relwidth=0.94)
        self.Loginframe.configure(relief='groove')
        self.Loginframe.configure(foreground="black")
        self.Loginframe.configure(text='''Login : Parking Management''')
        self.Loginframe.configure(background="#d9d9d9")
        self.Loginframe.configure(width=330)

        self.LabelLoginUsername = Label(self.Loginframe)
        self.LabelLoginUsername.place(relx=0.061, rely=0.175, height=21, width=65, bordermode='ignore')
        self.LabelLoginUsername.configure(background="#d9d9d9")
        self.LabelLoginUsername.configure(disabledforeground="#a3a3a3")
        self.LabelLoginUsername.configure(foreground="#000000")
        self.LabelLoginUsername.configure(text='''Username :''')

        self.LabelLoginPassword = Label(self.Loginframe)
        self.LabelLoginPassword.place(relx=0.061, rely=0.316, height=21, width=62, bordermode='ignore')
        self.LabelLoginPassword.configure(background="#d9d9d9")
        self.LabelLoginPassword.configure(disabledforeground="#a3a3a3")
        self.LabelLoginPassword.configure(foreground="#000000")
        self.LabelLoginPassword.configure(text='''Password :''')

        self.EntryUsername = Entry(self.Loginframe, textvariable = self.Username)
        self.EntryUsername.place(relx=0.273, rely=0.175, height=20, relwidth=0.679, bordermode='ignore')

        self.EntryPassword = Entry(self.Loginframe, show = '*', textvariable = self.Password)
        self.EntryPassword.place(relx=0.273, rely=0.316, height=20, relwidth=0.679, bordermode='ignore')

        
        self.btnLogin = Button(self.Loginframe, text = "Login", command = self.System_Login)
        self.btnLogin.place(relx=0.576, rely=0.491, height=24, width=121, bordermode='ignore')
        
        self.btnCancelLogin = Button(self.Loginframe,  text = "Cancel", command = self.cancelLogin) 
        self.btnCancelLogin.place(relx=0.303, rely=0.491, height=24, width=67, bordermode='ignore')
    

    def System_Login(self):
        Username_login = (self.Username.get())
        Password_login = (self.Password.get())

        # if (Username_login == str("user")) and (Password_login == str("password")):
        if (Username_login == str("")) and (Password_login == str("")):
            self.btnLogin.config(state = DISABLED)
            self.new_window_main()
            # self.master.withdraw()
        else:
            self.Username.set("")
            self.Password.set("")
            # self.new_window_report()
            # messagebox.showinfo("Login Error!", "Invalid Login Credentials!")
            tkinter.messagebox.showerror("Login Error!", "Invalid Login Credentials!")
            self.EntryUsername.focus()

    def cancelLogin(self):
        msg = tkinter.messagebox.askyesno("Login", "Are you sure you want to exit?")
        if (msg):
            self.master.destroy()
            # exit()

    def new_window_main(self):
        self.newWindow = Toplevel(self.master)
        self.app = WindowPMMain(self.newWindow)
        
    def new_window_report(self):
        self.newWindow = Toplevel(self.master)
        self.app = WindowPMReport(self.newWindow)
        

# Main window ============================================ 
class WindowPMMain:
    def __init__(self, master):
        self.master = master
        self.master.title("Parking Management")
        self.master.geometry("1366x715+-199+62")
        # self.master.state("zoomed")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.LabelTitleMain = Label(self.frame, text = 'Parking Management System', font = ('arial', 20, 'bold'), bd = 5)
        self.LabelTitleMain.grid(row=0, column=0, columnspan =1, pady =40)
        # # self.LabelTitleMain.place(relx=-0.044, rely=0.028)


        self.Frame_SysInfo = Frame(self.frame)
        self.Frame_SysInfo.place(relx=0.505, rely=0.014, relheight=0.077, relwidth=0.487)
        self.Frame_SysInfo.configure(relief='groove')
        self.Frame_SysInfo.configure(borderwidth="2")
        self.Frame_SysInfo.configure(relief='groove')
        self.Frame_SysInfo.configure(background="#d9d9d9")
        self.Frame_SysInfo.configure(width=665)

        self.Frame_Info = Frame(self.frame)
        self.Frame_Info.place(relx=0.007, rely=0.098, relheight=0.888, relwidth=0.487)
        self.Frame_Info.configure(relief='groove')
        self.Frame_Info.configure(borderwidth="2")
        self.Frame_Info.configure(relief='groove')
        self.Frame_Info.configure(background="#d9d9d9")
        self.Frame_Info.configure(highlightbackground="#d9d9d9")
        self.Frame_Info.configure(highlightcolor="black")
        self.Frame_Info.configure(width=665)

        self.Frame_Video = Frame(self.frame)
        self.Frame_Video.place(relx=0.505, rely=0.098, relheight=0.888, relwidth=0.487)
        self.Frame_Video.configure(relief='groove')
        self.Frame_Video.configure(borderwidth="2")
        self.Frame_Video.configure(relief='groove')
        self.Frame_Video.configure(background="#d9d9d9")
        self.Frame_Video.configure(highlightbackground="#d9d9d9")
        self.Frame_Video.configure(highlightcolor="black")
        self.Frame_Video.configure(width=665)
       


                

# Report window ============================================
class WindowPMReport:
    def __init__(self, master):
        self.master = master
        self.master.title("Parking Management : Report")
        self.master.geometry("351x304+477+130")
        self.frame = Frame(self.master)
        self.frame.pack()
        


if __name__ == '__main__':
    root = Tk()
    b = WindowPMLogin(root)
    root.mainloop()
#     main()