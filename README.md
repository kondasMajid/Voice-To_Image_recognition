# Voice To Speech Image Recognition

A class Project on Computer Graphics

#Specification
- Python System Installation
- LAMP/WAMP Server Installation
- Database Configuration



#   Summary 

#   ................................................................

#  recognize_speech() 

-   This code defines a function, recognize_speech(), which uses the speech_recognition library to listen for user voice input.

-   The audio input is then tried to be recognized by Google Speech Recognition service. 

-   If it is successful, it will print the description and call another function fetch_image() with the description.

-   If the audio input is not recognized, it will prompt the user to enter a text description, and then call the fetch_image() function. 

-   If there are any errors with the speech recognition library or the internet connection, it will print an error message.




#   fetch_image function 

-   The code function  fetches and displays an image based on user input.

-   It starts by creating a query to search for the image in the database based on the description, name, position or country given. 

-   If the query returns a result, the image path is retrieved and the image is loaded using the cv2 library. 

-   If the library can read the image path, it will be displayed. 

-   Otherwise, a "Failed to load image" message is printed.
 
-   If no result is found for the given description, a "No image found for the given description" message is printed.





