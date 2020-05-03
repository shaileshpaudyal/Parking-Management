from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import cv2
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename
import numpy as np
import cv2
import pandas as pd
import sqlite3

video_source = 0
carscrossedup = 0
carscrosseddown = 0
totalparkspace = 50

# ((totalparkspace - carscrosseddown) + carscrossedup)

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
        
        with sqlite3.connect("Quiz.db") as db:
            cursor = db.cursor()
        
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        
        cursor.execute(find_user, [(Username_login), (Password_login)])
        results = cursor.fetchall()

        if results:
            self.btnLogin.config(state = DISABLED)
            self.new_window_main()
            self.master.withdraw()
        else:
            self.Username.set("")
            self.Password.set("")
            # self.new_window_report()
            # messagebox.showinfo("Login Error!", "Invalid Login Credentials!")
            tkinter.messagebox.showerror("Login Error!", "Invalid Login Credentials!")
            self.EntryUsername.focus()
        
        # if (Username_login == str("user")) and (Password_login == str("password")):
#         if (Username_login == str("")) and (Password_login == str("")):
#             self.btnLogin.config(state = DISABLED)
#             self.new_window_main()
# #             self.master.withdraw()
#         else:
#             self.Username.set("")
#             self.Password.set("")
#             # self.new_window_report()
#             # messagebox.showinfo("Login Error!", "Invalid Login Credentials!")
#             tkinter.messagebox.showerror("Login Error!", "Invalid Login Credentials!")
#             self.EntryUsername.focus()

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
        self.master.title("Parking Management : Main")
        self.master.geometry("550x304+477+130")
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.master.protocol("WM_DELETE_WINDOW", self.on_exit)

        self.OptionValue = IntVar()
        
        self.LabelTitle = Label(self.frame, text = 'Parking Management System', font = ('arial', 30, 'bold')).pack()
#         self.LabelTitle.place(relx=0.028, rely=0.033, relheight=0.938, relwidth=0.94)
        

        self.OptionTitle = Label(self.frame, text="Choose a Source", font = ('arial', 15, 'bold')).pack(anchor=W)
#         self.OptionTitle.place(relx=0.028, rely=0.033, relheight=0.938, relwidth=0.94)
        self.RadioLive = Radiobutton(self.frame, text="Live Video", variable=self.OptionValue, value=1).pack(anchor=W)
#         self.RadioLive.place(relx=0.028, rely=0.033, relheight=0.938, relwidth=0.94)
        self.RadioVideo = Radiobutton(self.frame, text="Archive Video", variable=self.OptionValue, value=2).pack(anchor=W)
#         self.RadioVideo.place(relx=0.028, rely=0.033, relheight=0.938, relwidth=0.94)
        
#         self.LabelTitle = Label(self.frame, text = video_source).pack()
        
        self.btnGo = Button(self.frame, text = "Go", height=2, width=10, command = self.VideoSelection).pack()
      

    def VideoSelection(self):
        global video_source
        source = self.OptionValue.get()
        if source == 1:
            video_source = 0
            #print(video_source)
#             self.LabelTitle = Label(self.frame, text = video_source).pack()
            self.opennew()
        else:
            video_source = str(askopenfilename())
            #print(video_source)
#             self.LabelTitle = Label(self.frame, text = video_source).pack()
            self.opennew()
        
        return video_source
    
    def on_exit(self):
#         if self.messagebox.askyesno("Exit", "Do you want to quit the application?"):
        root.destroy()

    def opennew(self):
        self.PMTracker()
            
#         self.newWindow = Toplevel(self.master)
#         self.app = WindowPMReport(self.newWindow)
        

        
        
# Vehicle Tracking ==============================================================================
    def PMTracker(self):
    #class PMTracker:
        global video_source, carscrossedup, carscrosseddown, totalparkspace
        vs = video_source
        #print(vs)
        cap = cv2.VideoCapture(vs)
        # cap = cv2.VideoCapture(0) 
        
        if vs == 0:
            frames_count = 1000000
            fps = 26.830043291280184
        else:
            frames_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            fps = cap.get(cv2.CAP_PROP_FPS)
        
        # frames_count = 1000000
        # fps = 26.830043291280184
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # creates a pandas data frame with the number of rows the same length as frame count
        df = pd.DataFrame(index=range(int(frames_count)))
        df.index.name = "Frames"

        framenumber = 0  # keeps track of current frame
        carscrossedup = 0  # keeps track of cars that crossed up
        carscrosseddown = 0  # keeps track of cars that crossed down
        carids = []  # blank list to add car ids
        caridscrossed = []  # blank list to add car ids that have crossed
        totalcars = 0  # keeps track of total cars
        availablespace = totalparkspace

        fgbg = cv2.createBackgroundSubtractorMOG2()  # create background subtractor

        ret, frame = cap.read()  # import image
        ratio = 1  # resize ratio
        image = cv2.resize(frame, (0, 0), None, ratio, ratio)  # resize image

        while True:

            ret, frame = cap.read()  # import image

            if ret:  # if there is a frame continue with code

                image = cv2.resize(frame, (0, 0), None, ratio, ratio)  # resize image

                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # converts image to gray

                fgmask = fgbg.apply(gray)  # uses the background subtraction
                
                counterbkg = cv2.imread('white.jpg')

                # applies different thresholds to fgmask to try and isolate cars
                # just have to keep playing around with settings until cars are easily identifiable
                kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # kernel to apply to the morphology
                closing = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
                opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
                dilation = cv2.dilate(opening, kernel)
                retvalbin, bins = cv2.threshold(dilation, 220, 255, cv2.THRESH_BINARY)  # removes the shadows

                # creates contours
                contours, hierarchy = cv2.findContours(bins, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                # use convex hull to create polygon around contours
                hull = [cv2.convexHull(c) for c in contours]

                # draw contours
                cv2.drawContours(image, hull, -1, (0, 255, 0), 1)

                # line created to stop counting contours, needed as cars in distance become one big contour
                lineypos = 225
                cv2.line(image, (0, lineypos), (width, lineypos), (255, 0, 0), 2)

                # line y position created to count contours
                lineypos2 = 250
                cv2.line(image, (0, lineypos2), (width, lineypos2), (0, 255, 0), 2)

                # min area for contours in case a bunch of small noise contours are created
                minarea = 300

                # max area for contours, can be quite large for buses
                maxarea = 50000

                # vectors for the x and y locations of contour centroids in current frame
                cxx = np.zeros(len(contours))
                cyy = np.zeros(len(contours))

                for i in range(len(contours)):  # cycles through all contours in current frame

                    if hierarchy[0, i, 3] == -1:  # using hierarchy to only count parent contours (contours not within others)

                        area = cv2.contourArea(contours[i])  # area of contour

                        if minarea < area < maxarea:  # area threshold for contour

                            # calculating centroids of contours
                            cnt = contours[i]
                            M = cv2.moments(cnt)
                            cx = int(M['m10'] / M['m00'])
                            cy = int(M['m01'] / M['m00'])

                            if cy > lineypos:  # filters out contours that are above line (y starts at top)

                                # gets bounding points of contour to create rectangle
                                # x,y is top left corner and w,h is width and height
                                x, y, w, h = cv2.boundingRect(cnt)

                                # creates a rectangle around contour
                                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

                                # adds centroids that passed previous criteria to centroid list
                                cxx[i] = cx
                                cyy[i] = cy

                # eliminates zero entries (centroids that were not added)
                cxx = cxx[cxx != 0]
                cyy = cyy[cyy != 0]

                # empty list to later check which centroid indices were added to dataframe
                minx_index2 = []
                miny_index2 = []

                # maximum allowable radius for current frame centroid to be considered the same centroid from previous frame
                maxrad = 25

                # The section below keeps track of the centroids and assigns them to old carids or new carids

                if len(cxx):  # if there are centroids in the specified area

                    if not carids:  # if carids is empty

                        for i in range(len(cxx)):  # loops through all centroids

                            carids.append(i)  # adds a car id to the empty list carids
                            df[str(carids[i])] = ""  # adds a column to the dataframe corresponding to a carid

                            # assigns the centroid values to the current frame (row) and carid (column)
        #                     df.at[int(framenumber), str(carids[i])] = [cxx[i], cyy[i]]
                            df.at[framenumber, str(carids[i])] = [cxx[i], cyy[i]]

                            totalcars = carids[i] + 1  # adds one count to total cars

                    else:  # if there are already car ids

                        dx = np.zeros((len(cxx), len(carids)))  # new arrays to calculate deltas
                        dy = np.zeros((len(cyy), len(carids)))  # new arrays to calculate deltas

                        for i in range(len(cxx)):  # loops through all centroids

                            for j in range(len(carids)):  # loops through all recorded car ids

                                # acquires centroid from previous frame for specific carid
        #                         oldcxcy = df.iloc[int(framenumber - 1)][str(carids[j])]
                                oldcxcy = df.iloc[(framenumber - 1)][str(carids[j])]

                                # acquires current frame centroid that doesn't necessarily line up with previous frame centroid
                                curcxcy = np.array([cxx[i], cyy[i]])

                                if not oldcxcy:  # checks if old centroid is empty in case car leaves screen and new car shows

                                    continue  # continue to next carid

                                else:  # calculate centroid deltas to compare to current frame position later

                                    dx[i, j] = oldcxcy[0] - curcxcy[0]
                                    dy[i, j] = oldcxcy[1] - curcxcy[1]

                        for j in range(len(carids)):  # loops through all current car ids

                            sumsum = np.abs(dx[:, j]) + np.abs(dy[:, j])  # sums the deltas wrt to car ids

                            # finds which index carid had the min difference and this is true index
                            correctindextrue = np.argmin(np.abs(sumsum))
                            minx_index = correctindextrue
                            miny_index = correctindextrue

                            # acquires delta values of the minimum deltas in order to check if it is within radius later on
                            mindx = dx[minx_index, j]
                            mindy = dy[miny_index, j]

                            if mindx == 0 and mindy == 0 and np.all(dx[:, j] == 0) and np.all(dy[:, j] == 0):
                                # checks if minimum value is 0 and checks if all deltas are zero since this is empty set
                                # delta could be zero if centroid didn't move

                                continue  # continue to next carid

                            else:

                                # if delta values are less than maximum radius then add that centroid to that specific carid
                                if np.abs(mindx) < maxrad and np.abs(mindy) < maxrad:

                                    # adds centroid to corresponding previously existing carid
                                    df.at[framenumber, str(carids[j])] = [cxx[minx_index], cyy[miny_index]]
                                    minx_index2.append(minx_index)  # appends all the indices that were added to previous carids
                                    miny_index2.append(miny_index)

                        for i in range(len(cxx)):  # loops through all centroids

                            # if centroid is not in the minindex list then another car needs to be added
                            if i not in minx_index2 and miny_index2:

                                df[str(totalcars)] = ""  # create another column with total cars
                                totalcars = totalcars + 1  # adds another total car the count
                                t = totalcars - 1  # t is a placeholder to total cars
                                carids.append(t)  # append to list of car ids
                                df.at[framenumber, str(t)] = [cxx[i], cyy[i]]  # add centroid to the new car id

                            elif curcxcy[0] and not oldcxcy and not minx_index2 and not miny_index2:
                                # checks if current centroid exists but previous centroid does not
                                # new car to be added in case minx_index2 is empty

                                df[str(totalcars)] = ""  # create another column with total cars
                                totalcars = totalcars + 1  # adds another total car the count
                                t = totalcars - 1  # t is a placeholder to total cars
                                carids.append(t)  # append to list of car ids
                                df.at[framenumber, str(t)] = [cxx[i], cyy[i]]  # add centroid to the new car id

                # The section below labels the centroids on screen

                currentcars = 0  # current cars on screen
                currentcarsindex = []  # current cars on screen carid index

                for i in range(len(carids)):  # loops through all carids

                    if df.at[framenumber, str(carids[i])] != '':
                        # checks the current frame to see which car ids are active
                        # by checking in centroid exists on current frame for certain car id

                        currentcars = currentcars + 1  # adds another to current cars on screen
                        currentcarsindex.append(i)  # adds car ids to current cars on screen

                for i in range(currentcars):  # loops through all current car ids on screen

        #             print(framenumber)
                    # grabs centroid of certain carid for current frame
                    curcent = df.iloc[framenumber][str(carids[currentcarsindex[i]])]

                    # grabs centroid of certain carid for previous frame
                    oldcent = df.iloc[(framenumber - 1)][str(carids[currentcarsindex[i]])]

                    if curcent:  # if there is a current centroid
                        if oldcent:  # checks if old centroid exists
                            # adds radius box from previous centroid to current centroid for visualization
                            xstart = oldcent[0] - maxrad
                            ystart = oldcent[1] - maxrad
                            xwidth = oldcent[0] + maxrad
                            yheight = oldcent[1] + maxrad
                            cv2.rectangle(image, (int(xstart), int(ystart)), (int(xwidth), int(yheight)), (0, 125, 0), 1)

                            # checks if old centroid is on or below line and curcent is on or above line
                            # to count cars and that car hasn't been counted yet
                            if oldcent[1] >= lineypos2 and curcent[1] <= lineypos2 and carids[
                                currentcarsindex[i]] not in caridscrossed:

                                carscrossedup = carscrossedup + 1
                                cv2.line(image, (0, lineypos2), (width, lineypos2), (0, 0, 255), 5)
                                caridscrossed.append(
                                    currentcarsindex[i])  # adds car id to list of count cars to prevent double counting

                            # checks if old centroid is on or above line and curcent is on or below line
                            # to count cars and that car hasn't been counted yet
                            elif oldcent[1] <= lineypos2 and curcent[1] >= lineypos2 and carids[
                                currentcarsindex[i]] not in caridscrossed:

                                carscrosseddown = carscrosseddown + 1
                                cv2.line(image, (0, lineypos2), (width, lineypos2), (0, 0, 125), 5)
                                caridscrossed.append(currentcarsindex[i])



                cv2.putText(image, "Cars out: " + str(carscrossedup), (0, 30), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 170, 0), 1)
                cv2.putText(image, "Cars in: " + str(carscrosseddown), (0, 45), cv2.FONT_HERSHEY_DUPLEX, 0.5,(0, 170, 0), 1)
                if ((totalparkspace - carscrosseddown) + carscrossedup) > totalparkspace:
                    availablespace = totalparkspace
                else:
                    availablespace = ((totalparkspace - carscrosseddown) + carscrossedup)
                cv2.putText(counterbkg, str(availablespace), (1, 250), cv2.FONT_HERSHEY_DUPLEX, 10,(0, 0, 0), 20)

#                 cv2.putText(counterbkg, "Cars out: " + str(carscrossedup), (0, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 170, 0), 1)

                cv2.imshow('Available Parking', counterbkg)
                cv2.moveWindow('Resized Window', 200,200)                
                
#                 print("Cars out: ", carscrossedup)
#                 print("Cars in: ", carscrosseddown)
#                 print("Available space: ", ((totalparkspace - carscrosseddown) + carscrossedup))


                # displays images and transformations
                cv2.imshow("Parking Management: Live Feed", image)
                cv2.moveWindow("countours", 0, 0)

#                 cv2.imshow("Background Subtracted", fgmask)
#                 cv2.moveWindow("fgmask", int(width * ratio), 0)

        #         cv2.imshow("Closing Morphology", closing)
        #         cv2.moveWindow("closing", width, 0)

        #         cv2.imshow("Opening Morphology", opening)
        #         cv2.moveWindow("opening", 0, 0)

        #         cv2.imshow("Dilation", dilation)
        #         cv2.moveWindow("dilation", 0, 0)

        #         cv2.imshow("Binary Thresholding", bins)
        #         cv2.moveWindow("binary", 0, 0)

                # adds to framecount
                framenumber = framenumber + 1

                k = cv2.waitKey(int(1000/fps)) & 0xff
                if k == 27:
                    break

            else:  # if video is finished then break loop

                break

        cap.release()
        cv2.destroyAllWindows()    
        

# Report window ============================================
class WindowPMReport:
    def __init__(self, master):
        self.master = master
        self.master.title("Parking Management : Report")
        self.master.geometry("351x304+477+130")
        

if __name__ == '__main__':
    root = Tk()
    b = WindowPMLogin(root)
    root.mainloop()
#     main()