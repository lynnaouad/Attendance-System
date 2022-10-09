import csv
import sys
import cv2
import os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen, QDesktopWidget, QDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer, QDate
import time
import datetime
import sqlite3
import numpy as np
import face_recognition as face_rec
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        loadUi("splashscreen.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #center splashscreen
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle = self.frameGeometry()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def progress(self):
        for i in range(101):
            time.sleep(0.1)
            self.progressBar.setValue(i)


class LoginScreen(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        loadUi("login.ui", self)

        # hide password
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login.clicked.connect(self.loginfunction)

    def loginfunction(self):
        user = self.usernamefield.text()
        password = self.passwordfield.text()

        if len(user) == 0 or len(password) == 0:
            self.error.setText("Please input all fields.")
        else:
            conn = sqlite3.connect("SystemDB.db")
            cur = conn.cursor()
            print("Connected to database successfully!")

            query = "SELECT password FROM login_info WHERE username=\'"+user+"\'"
            cur.execute(query)

            result_pass = cur.fetchone()[0]

            if result_pass == password:
                print("Successfully logged in.")
                self.error.setText("")

                main = MainScreen()
                widget.addWidget(main)
                widget.setCurrentIndex(widget.currentIndex()+1)

            else:
                self.error.setText("Invalid username or password")


class MainScreen(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        loadUi("main.ui", self)

        self.startVideo()
        print("Video Played")

        # Update time and date
        now = QDate.currentDate()
        current_date = now.toString('ddd dd MMMM yyyy')
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.datelabel.setText(current_date)
        self.timelabel.setText(current_time)

        self.image = None

        # At first, checkout button is desabled
        self.leaveBtn.setChecked(False)
        self.leaveBtn.setEnabled(False)


    def startVideo(self):

        # A function that take parameter the list of students images and will find their encoding and return them as list
        def FindImagesEncodings(images):
            EncodingsList = []

            for img in images:
                # img = resize(img, 0.50)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # convert to the right colors
                ImgEncoding = face_rec.face_encodings(img)[0]  # [0] because it's an image not a video
                EncodingsList.append(ImgEncoding)

            return EncodingsList

        # A function that get all instructors information from database and return them
        def GetAllInstructorsInfo():
            conn = sqlite3.connect("SystemDB.db")
            cur = conn.cursor()
            query = "SELECT * FROM Instructors"
            cur.execute(query)

            result = cur.fetchall()

            instructorsList = []

            for row_number, row_data in enumerate(result):
                line = []
                for column_number, data in enumerate(row_data):
                    line.append(data)

                instructorsList.append({"name": line[0], "email": line[1], "course": line[2]})

            return instructorsList


        # Initialize webcam
        self.video = cv2.VideoCapture(0)  # id = 0

        path = 'Students_Images'

        if not os.path.exists(path):
            os.mkdir(path)

        self.studentsImages = []
        self.studentsNames = []

        self.instructors = GetAllInstructorsInfo()

        self.currentInstructor = []


        # A student can checkin and checkout several times so we need to save them all
        self.TimeList1 = []
        self.TimeList2 = []

        # Get a list containing the names of the files in directory : ['image1.jpg' , 'image2.jpg' , 'image3.jpg' ]
        ImagesList = os.listdir(path)

        # Read the directory and get all images and their names
        for img in ImagesList:
            currentImg = cv2.imread(f'{path}/{img}')
            self.studentsImages.append(currentImg)
            self.studentsNames.append(os.path.splitext(img)[0])  # Remove extension: splitext(img)[0] -> | image1 | .jpg |

        # Get Images Encodings
        self.EncodingsListKnown = FindImagesEncodings(self.studentsImages)
        print('Encoding Complete!')

        # every 10ms we call fonction update_frame
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(10)

    def update_frame(self):
        success, self.image = self.video.read()
        self.displayImage(self.image, self.EncodingsListKnown, self.studentsNames)

    def displayImage(self, image, encode_list, students_names):
        image = cv2.resize(image, (411, 401))

        try:
            image = self.face_rec_function(image, encode_list, students_names)
        except Exception as e:
            print(e)


        qformat = QImage.Format_Indexed8

        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
        outImage = outImage.rgbSwapped()

        self.videoplace.setPixmap(QPixmap.fromImage(outImage))
        self.videoplace.setScaledContents(True)

    def face_rec_function(self, image, encode_list, students_names):

        # A function that take the name of the student as parameter and write it to
        # the Attendance.csv file with the time he entered the class
        def mark_attendance(name):
            if self.joinBtn.isChecked():
                with open('Attendance.csv', 'a') as f:

                    if name != 'unknown':
                        reply = QMessageBox.question(self, '', 'Do you want to join the meeting?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No) #default no

                        if reply == QMessageBox.Yes:
                            self.joinBtn.setChecked(False)
                            self.joinBtn.setEnabled(False)

                            self.leaveBtn.setEnabled(True)

                            # Instructor doesn't need to know when he joined or left the meeting
                            if name != 'Instructor':
                                date_time_string = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
                                f.writelines(f'\n{name},{date_time_string},joined')

                            self.joinBtn.setChecked(False)

                            # fill details
                            self.namelabel.setText(name)
                            self.statuslabel.setText('In the meeting')
                            self.passedtime.setText('Mesuring...')
                    else:
                        QMessageBox.warning(self, '', "You don't have permession to enter the meeting", QMessageBox.Cancel, QMessageBox.Cancel)
                        self.joinBtn.setChecked(False)


            elif self.leaveBtn.isChecked():
                with open('Attendance.csv', 'a') as f:
                    if name != 'unknown':
                        reply = QMessageBox.question(self,'','Do you want to leave the meeting?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                        if reply == QMessageBox.Yes:
                            self.leaveBtn.setChecked(False)
                            self.leaveBtn.setEnabled(False)

                            self.joinBtn.setEnabled(True)

                            # Instructor doesn't need to know when he joined or left the meeting
                            if name != 'Instructor':
                                date_time_string = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
                                f.writelines(f'\n{name},{date_time_string},left')
                            else:
                                # When instructor leaves the meeting the Attendance.csv file is sent to the instructor's email
                                self.sendEmail(self.currentInstructor)

                            self.leaveBtn.setChecked(False)

                            self.namelabel.setText(name)
                            self.statuslabel.setText('Out of the meeting')

                            # fill TimeList1 & TimeList2
                            self.JoinLeftList(name)

                            LastCheckInTime = self.TimeList1[-1]    #last index
                            LastCheckOutTime = self.TimeList2[-1]

                            self.ElapsedHours = (LastCheckInTime - LastCheckOutTime)

                            hours = "{:.0f}".format(abs(self.ElapsedHours.total_seconds() / 60 ** 2)) + 'h'
                            mins = "{:.0f}".format(abs(self.ElapsedHours.total_seconds() / 60) % 60) + 'm'

                            self.passedtime.setText(hours+""+mins)



        # Resize image to help speeding process
        smallerImg = cv2.resize(image, (0, 0), None, 0.25, 0.25)  # scale: 1/4 of the actual size
        smallerImg = cv2.cvtColor(smallerImg, cv2.COLOR_BGR2RGB)

        # Find all faces locations in the frame : returns list of all faces locations (top, right, bottom, left)
        currentFacesLoc = face_rec.face_locations(smallerImg)

        # returns list of all encoded faces
        currentEncodeFaces = face_rec.face_encodings(smallerImg, currentFacesLoc)

        for encodeFace, faceLoc in zip(currentEncodeFaces, currentFacesLoc):
            # Compare each encoded face in the frame to all others encoded images
            # return a list of True/False values ["True","false","false"]
            matches = face_rec.compare_faces(encode_list, encodeFace)

            # Get the distance which tells you how similar the faces are -> the lowest distance : best match!
            faceDistance = face_rec.face_distance(encode_list, encodeFace)

            matchIndex = np.argmin(faceDistance)

            if matches[matchIndex]:

                #check if Instructor
                if(len(self.currentInstructor) == 0):
                    for instructor in self.instructors:
                            if instructor['name'] == students_names[matchIndex]:
                                self.currentInstructor.append(instructor['name'])
                                self.currentInstructor.append(instructor['email'])
                                self.currentInstructor.append(instructor['course'])

                if self.currentInstructor:
                    name = "Instructor"
                else:
                    name = students_names[matchIndex].upper()

            else:
                name = "unknown"

            y1, x2, y2, x1 = faceLoc

            # Because image is scaled down to 1/4 -> multiply by 4 to get initial location
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(image, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(image, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

            mark_attendance(name)

        return image

    def JoinLeftList(self, name):
        with open('Attendance.csv', "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 2

            # initialize variables to format time
            Time1 = datetime.datetime.now()
            Time2 = datetime.datetime.now()

            for row in csv_reader:
                for field in row:
                    if field in row:
                        if field == 'joined':
                            if row[0] == name:
                                # fill all the times that this student joined the meeting in TimeList1
                                Time1 = (datetime.datetime.strptime(row[1], '%y/%m/%d %H:%M:%S'))
                                self.TimeList1.append(Time1)
                        if field == 'left':
                            if row[0] == name:
                                # fill all the times that this student left the meeting in TimeList2
                                Time2 = (datetime.datetime.strptime(row[1], '%y/%m/%d %H:%M:%S'))
                                self.TimeList2.append(Time2)

    def sendEmail(self, instructorInfo):
        from_email = ''
        from_password = ''

        to_email = instructorInfo[1]

        today = datetime.datetime.now().date()
        today = str(today)
        subject = instructorInfo[2] + ' attendance - ' + today

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        body = instructorInfo[2] + ' attendance - ' + today
        msg.attach(MIMEText(body, 'plain'))

        filename = 'Attendance.csv'
        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)

        server.sendmail(from_email, to_email, text)
        server.quit()

        print("Email sent successfully!")

        print("Reseting the Attendance.csv file")

        with open('Attendance.csv', 'w') as f:
            f.write('Name,Time,Status')

        print("Attendance.csv has been reseted successfully")
        print("Exiting Program")

        exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    splash = SplashScreen()
    splash.show()
    splash.progress()

    login = LoginScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(login)
    widget.setFixedWidth(643)
    widget.setFixedHeight(529)
    widget.show()

    splash.finish(widget)




    app.exec()