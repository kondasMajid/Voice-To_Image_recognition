import mysql.connector
import cv2

# Establish a database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pic_db"
)

# Function to fetch and display the image based on user input
def fetch_image(description):
    cursor = db.cursor()
    # Make a querry to database
    query = "SELECT image_path, name,position,description FROM pic_tb WHERE description = %s OR name = %s OR position = %s OR country = %s"
    cursor.execute(query, (description, description, description, description))
    result = cursor.fetchone()

    # Check if the querry contains the result data 
    if result:
        image_path = result[0]
        image = cv2.imread(image_path)
    
        print("User Search result : ", result)

        # if cv2 libabry can read the image path and continue to show the image 
        if image is not None:
            cv2.imshow("Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            # if cv2 libary can't read the image path  print Failed 
            print("Failed to load image.")
            
    else:
        print("No image found for the given description.")

# Use speech recognition to get user input
def recognize_speech():
    import speech_recognition as sr
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        description = r.recognize_google(audio)
        print("Description:", description)
        fetch_image(description)

    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
        fallback_text = input("Please enter the text description: ")
        fetch_image(fallback_text)

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Example usage
recognize_speech()

# Close the database connection
db.close()








































# import speech_recognition as sr
# import mysql.connector
# import cv2

# # Set up the speech recognition system
# r = sr.Recognizer()

# # Establish a database connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="pic_db"
# )

# # Function to fetch and display the image based on user input
# def fetch_image(description):
#     cursor = db.cursor()
#     query = "SELECT image_path FROM pic_tb WHERE description = %s"
#     cursor.execute(query, (description))
#     result = cursor.fetchone()

#     if result:
#         image_path = result[0]
#         image = cv2.imread(image_path)

#         if image is not None:
#             cv2.imshow("Image", image)
#             cv2.waitKey(0)
#             cv2.destroyAllWindows()
#         else:
#             print("Failed to load image.")
#     else:
#         print("No image found for the given description.")
#         fallback_text = input("Please enter the text description: ")
#         fetch_image(fallback_text)
        

# # Use speech recognition to get user input
# def recognize_speech():
#     import speech_recognition as sr
#     r = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source)

#     try:
#         description = r.recognize_google(audio)
#         print("Description:", description)
#         fetch_image(description)

#     except sr.UnknownValueError:
#         print("Speech recognition could not understand audio.")
#         # fallback_text = input("Please enter the text description: ")
#         # fetch_image(fallback_text)

#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))

# # Example usage
# recognize_speech()

    

# # Close the database connection
# db.close()





# # # Use speech recognition to get user input
# # with sr.Microphone() as source:
# #     print("Listening...")
# #     audio = r.listen(source)

# # try:
# #     # Recognize speech using Google Speech Recognition
# #     print("Recognizing...")
# #     description = r.recognize_google(audio)
# #     print("Description:", description)

# #     # Fetch and display the image based on the description
# #     fetch_image(description)

# # except sr.UnknownValueError:
# #     print("Speech recognition could not understand audio.")
# # except sr.RequestError as e:
# #     print("Could not request results from Google Speech Recognition service; {0}".format(e))