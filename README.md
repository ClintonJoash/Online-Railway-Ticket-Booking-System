# Online-Railway-Ticket-Booking-System
Railways is one the most frequently used mode of transport by the people of our country as it is comparatively cheap and is convenient than other modes due to its great connectivity throughout India.  

Earlier, people used to face various problems while booking tickets as they had to frequently visit the reservation counter or ticket booking site agents.  

Thus, this Online Ticket Booking system will save people's time and make the process less tedious.  

Using the existing IRCTC website we cannot store the past travel history and access it for booking tickets in the future.  
Also, if a user needs to reach to a particular place, there is no such option of shortlisting trains based on it.  

Inorder to incorporate the above listed facilities I have made this desktop application for online booking of railway tickets.  
This application is made using Tkinter a Python GUI library. The Oracle database is used to store tha registration and booking information.  

The frontpage of the application:  
![Front Page](SCREENSHOTS/FRONT_PAGE.png)  

The registration page gets all the user data and stores it into the Oracle database. During the login process the username and password is validated using the stored data.  
The Registration and Login pages:  
![Front Page](SCREENSHOTS/REGISTRATION.JPG)               ![Front Page](SCREENSHOTS/LOGIN.JPG)  

If we want to check the schedule of a particular train we can enter the train name or number in the Train Schedule dialog box:  
![Train Schedule](SCREENSHOTS/FIND_TRAIN.JPG)  

For example if we select the JAN SHATABDI train, we will get the entire schedule for that train:  

![jan-shatabdi-afs0xhh0-1_ciibRo9P](https://user-images.githubusercontent.com/89999331/223333482-df14f87a-22b1-42fa-b468-642e9f3d27de.gif)

If we want to check the trains available between 2 stations then we can search for those 2 stations in the Check Available Trains dialog box:  
![Available Trains](SCREENSHOTS/Check_train_status.JPG)  

The trains available between the 2 stations will be listed with the fastest train first:  

After Clicking on the Book Ticket button we get a dialog box to confirm our booking:  
![Confirm Booking](SCREENSHOTS/TRAIN_BOOKING.JPG)  



