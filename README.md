<a name="readme-top"></a>

<img src="https://user-images.githubusercontent.com/82551484/194697977-541e32ae-d298-472c-9534-ccf6d385accc.png" align="right" />

# Face Attendance System</br>
![Issues](https://img.shields.io/github/issues/lynnaouad/CoffeeShop-Website)&nbsp;
![Stars](https://img.shields.io/github/stars/lynnaouad/CoffeeShop-Website)&nbsp;
![Contributors](https://img.shields.io/github/contributors/lynnaouad/CoffeeShop-Website)&nbsp;
![Forks](https://img.shields.io/github/forks/lynnaouad/CoffeeShop-Website)

> Welcome aboard fellow developer, this is where you will find projects which you are free to contribute to. You can contribute by submitting your own scripts, which you think would be amazing for other people to see. 

## Description
The objective of the project is to create a program with a friendly user interface that assists University Doctors with taking student attendance. First the student must login then join the meeting, the program will scan the student's face using the camera connected to the device on which the program is running, it will find the face in the video and encode it into data that will be compared with the encoding of the images present in the program database, upon detecting the facial identification, it will save the student's name together with the time he joined and left the meeting in a csv file that will be sent to the instructor via Email after he finishes the meeting. <br>

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
      git clone https://github.com/lynnaouad/CoffeeShop-Website.git
      ```
      
      **5.** When you run `git clone https://github.com/lynnaouad/CoffeeShop-Website.git`, You should see output like
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

  - **Steps you must do to make the app work properly** :
      **1.** Install all the packages listed in the "Python Packages Used" section in this README.<br>

      **2.** Copy the images of the students and the instructor faces to the "Students_Images" folder. Each image has to have the name of the student.<br>

      **3.** Insert the information of the instructors and logins in SQlite database "SystemDB.db".<br>
      
      **4.** Execute the program (AttendanceSystem.py).<br>
 
      
<p align="right">(<a href="#readme-top">back to top</a>)</p> <br>


## Usage



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

