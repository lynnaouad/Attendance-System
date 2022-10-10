<a name="readme-top"></a>

<img src="https://user-images.githubusercontent.com/82551484/194697977-541e32ae-d298-472c-9534-ccf6d385accc.png" align="right" />

# Face Attendance System</br>
![Issues](https://img.shields.io/github/issues/lynnaouad/CoffeeShop-Website)&nbsp;
![Stars](https://img.shields.io/github/stars/lynnaouad/CoffeeShop-Website)&nbsp;
![Contributors](https://img.shields.io/github/contributors/lynnaouad/CoffeeShop-Website)&nbsp;
![Forks](https://img.shields.io/github/forks/lynnaouad/CoffeeShop-Website)

> Welcome aboard fellow developer, this is where you will find projects which you are free to contribute to. You can contribute by submitting your own scripts, which you think would be amazing for other people to see. 

## Description
The objective of the project is to create a program with a friendly user interface that assists University Doctors with taking student attendance. First the student must enter his username and password to login then join the meeting, the program will scan the student's face, it will find the face in the video and encode it into data that will be compared with the encoding of all students' images present in the program database, upon detecting the facial identification, it will save the student's name together with the time he joined and left the meeting in a csv file that will be sent to the instructor via Email after he finishes the meeting. <br>

`Note` In this project SQLite database is used to save login and instructor information and PyQt5 library for graphical user interface.

## Built With

* [![Python][Python.com]][Python-url]
* [![SQLite][SQLite.com]][SQLite-url]
* [![PyQt5][PyQt5.com]][PyQt5-url]


**Python Packages Used:**<br>
<ul>
  <li>numpy</li>
  <li>cmake</li>
  <li>opencv-python</li>
  <li>dlib</li>
  <li>face_recognition</li>
  <li>secure-smtplib</li>
  <li>time</li>
  <li>PyQT5</li>
</ul><br>

  
## Installation

Download the project from github to your desktop:

  - **With Git** :
      If you’re familiar with git and have it installed on your computer, you can clone the repository to download the files.
      
      **1.** Click the green button labeled &nbsp;`Code`</br>
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://user-images.githubusercontent.com/82551484/194698853-75cf149f-b2cb-4e89-ab14-95b9a0324445.png" width="300px;" /></br>
      
      **2.** Copy the URL of the repository</br>
      
      **3.** Next, on your local machine, open your bash shell and change your current working directory to the location where you would like to clone your repository
      ```shell
      cd "path-to-your-folder"
      ```
      
      **4.** Once you have navigated to the directory where you want to put your repository, you can use
      ```shell
      git clone https://github.com/lynnaouad/Face-Attendance-System.git
      ```
      
      **5.** When you run `git clone https://github.com/lynnaouad/Face-Attendance-System.git`, You should see output like
      ```shell
      Cloning into 'test-repo'...
      remote: Counting objects: 5, done.
      remote: Compressing objects: 100% (4/4), done.
      remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
      Unpacking objects: 100% (5/5), done.
      Checking connectivity... done.
      ```
      </br>
      
  - **Without Git** :
      When downloading materials to your laptop, it is easiest to download the entire repository.<br>
      
      **1.** Click on the green `Code` button, then download the repository as a ZIP file</br>
      
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://user-images.githubusercontent.com/82551484/194698883-4b94312d-4537-48d2-ae16-84b807120605.png" width="350px;" /></br>
      
      **2.** Find the downloaded .zip file on your computer, likely in your Downloads folder</br>
      
      **3.** Unzip it, this will create a folder named after the GitHub repository</br></br>

  - **Steps you must do to make the app work properly** : <br><br>
      **1.** Install all the packages listed in the "Python Packages Used" section in this README.<br>

      **2.** Copy the images of the students and the instructor faces to the "Students_Images" folder. Each image has to have the name of the student.<br>

      **3.** Insert the information of the instructors and logins in SQlite database "SystemDB.db".<br>
      
      **4.** Execute the program (AttendanceSystem.py).<br>
 
      
<p align="right">(<a href="#readme-top">back to top</a>)</p> <br>


## Usage
**Splash Screen:** <br>
![WmEq225C9F](https://user-images.githubusercontent.com/82551484/194872756-debc7ca8-9bbc-4232-8fc3-9d307d1f2678.png) <br>

**Login page:** <br>
`Note` When student enters his username and password the program will fetch all logins from database then check if he is registered or not.<br>
![wPZ7rbWH2n](https://user-images.githubusercontent.com/82551484/194872837-ae81863b-589c-47b2-9ef7-c05d9d402aeb.png)


**Main Page:** <br>
`Note` Before joining the meeting only date and time information are displayed. <br>
![1](https://user-images.githubusercontent.com/82551484/194874327-ace941f1-2cee-4ec0-a28a-98051079536c.png) <br><br>

- **Joining Meeting:**<br>
![2](https://user-images.githubusercontent.com/82551484/194874385-211888bd-fde7-4e8d-a61d-8bdceec66386.png) <br><br>

`Note` After joining, the name and status of the student are displayed. <br>
![3](https://user-images.githubusercontent.com/82551484/194874437-ab73c614-eab0-4bfb-99c8-067fa4a398b5.png) <br>

- **Leaving Meeting:** <br>
![4](https://user-images.githubusercontent.com/82551484/194874487-5440158b-767b-42b1-81ad-a3112ab713a7.png) <br>

`Note` After leaving, the time that the student stayed in the meeting is calculated and displayed.
![5](https://user-images.githubusercontent.com/82551484/194874529-6c399d8c-6aa4-409f-a43f-32294a1b99d7.png) <br>

`Note` Attendance list: <br><br>
![pycharm64_Y9HyL1yXCD](https://user-images.githubusercontent.com/82551484/194876251-b66eb57e-43ee-4ff4-8bf5-41362752dbe4.png) <br>

`Note` During face detection if the current face didn't match with any of the others faces present in the program database then the student can't join the meeting. <br>
![8yioLiD7cz](https://user-images.githubusercontent.com/82551484/194874162-acd0f8d6-6a39-4b0a-9c9e-3f5f8fbc7955.png) <br>

![PYERe8XQ1q](https://user-images.githubusercontent.com/82551484/194874194-2e74e35d-58cd-44b8-a066-7d18407819de.png) <br>

`Note` After the instructor finishes the meeting the program will send him automatically an email containing the attendance file and exit. <br>
![RA1ReaDGt6](https://user-images.githubusercontent.com/82551484/194876103-7d99ec91-10f0-4fae-a8d2-56d184b85227.png) <br> 
![pycharm64_5oPEKiSaEG](https://user-images.githubusercontent.com/82551484/194876131-88874f62-2ca8-4250-8a97-81aed35327e2.png) <br>


<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Contribution Guidelines

The contribution guidelines are as per the guide [HERE](https://github.com/MouhammadAyoub/CVs-repository/blob/main/CONTRIBUTING.md).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Instructions

- Fork this repository
- Clone your forked repository
- Add your scripts
- Commit and push
- Create a pull request
- Star this repository
- Wait for pull request to merge
- Celebrate your first step into the open source world and contribute more

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## License

Distributed under the MIT License. See [`LICENSE`](https://github.com/lynnaouad/Face-Attendance-System/blob/main/LICENSE) for more information.  
Copyright © 2022, Lynn Aouad

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

- Email&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;&nbsp;[lynnaouad34@gmail.com](mailto:lynnaouad34@gmail.com)

- Project Link : &nbsp;[https://github.com/lynnaouad/Face-Attendance-System](https://github.com/lynnaouad/Face-Attendance-System)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Additional tools to help you get Started with Open-Source Contribution

* [How to Contribute to Open Source Projects – A Beginner's Guide](https://www.freecodecamp.org/news/how-to-contribute-to-open-source-projects-beginners-guide/)
* [How to Write a Good README File for Your GitHub Project](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)

#### Note: When you add a project, add it to the README for ease of finding it.
#### Note: Please do not have the project link reference your local forked repository. Always link it to this repository after it has been merged with main.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



[Python.com]: https://img.shields.io/badge/Python-563D7C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://Python.com

[SQLite.com]: https://img.shields.io/badge/SQLite-0769AD?style=for-the-badge&logo=sqlite&logoColor=white
[SQLite-url]: https://SQLite.com

[PyQt5.com]: https://img.shields.io/badge/PyQt5-ff7340?style=for-the-badge&logo=python&logoColor=white
[PyQt5-url]: https://PyQt5.com

