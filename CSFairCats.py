#Samuel Nardone
#CS Fair Project
#November 15, 2017
#Crazy Cats Cheer Up

#Samuel Nardone
#CS FAIR PROJECT PYTHON
# THIS PROGRAM WILL ASK USERS IF THEY PREFER CATS OR DOGS OR BOTH. AFTER WE ASK
# FOR THE EMOTIONAL STATE OF THE USER. BASED ON THAT WE WILL DECIDE WHAT
# CATEGORY OF PICTURE TO DISPLAY. WE RANDOMIZE THE PHOTO GENERATED.

#import random and webbrowser library
import random
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage


#define our main function
def main():
    
#make our variables for selections
    cats = 1
    dogs = 2
    both = 3

    
    again = 'y'
    #while loop to ask user if they would like to repeat
    while again == 'y' or again == 'Y':

    #we ask user if they would like their results emailed to them
        email_y = input('Would you like your results emailed to you (type y or Y for yes)?: ')

        
        #we ask if they prefer cats dogs or both
        preferred_animal = cats_dogs()

    #function to get the users emotional status
        user_emotion = get_user_input()

        #if user selects both we will randomize a choice for them
        if preferred_animal == both:
            choice = random.randint(1, 2)
            
            # if the random number 'choice' is 1 we call the cat function            
            if choice == cats:
                kitten_image = kitten_image_finder(user_emotion)
                
            #if the random number 'choice' is 2 we call the dog function
            if choice == dogs:
                puppy_image = puppy_image_finder(user_emotion)

   #depending on preferred animal we call function
        if preferred_animal == cats:
        #calling the kitten_image finder function which will find a cat image from our folder to display on the screen
            kitten_image = kitten_image_finder(user_emotion)
            
        #calling puppy image finder if number 2 is chosen
        if preferred_animal == dogs:
            #calling the puppy image finder to find a random puppy picture
            puppy_image = puppy_image_finder(user_emotion)

        #if they want results emailed to them then we do so

        if email_y == 'y' or email_y == 'Y':
            toaddr = input('Enter your email address please: ')
            email_picture(toaddr)

  #if user if they would like to repeat      
        again = input('Pres y to repeat prrrocess over again. To exit type anything else: ')



################### FUNCTION FOR SELECTING CATS, DOGS, OR BOTH##########################
def cats_dogs():
    #make flag variable and other variables
    selection = False
    cats = 1
    dogs = 2
    both = 3
    #print the chart for the dog and cat 
    print('Cats', '\t', cats)
    print('Dogs', '\t', dogs)
    print('Both', '\t', both)

    #while loop until valid input
    while selection == False:

        try:
           
            user_preference = int(input('Cats, dogs, or both: '))
            
        except ValueError:
            print('That is not an option, please use the numbers')
        except TypeError:
            print('That is not an option, please use the numbers')
        except NameError:
            print('That is not an option, please use the numbers')

        try:           
            if user_preference >= 1 and user_preference <= 3:
                selection = True
            else:
                print('Choose a valid number please')
        except UnboundLocalError:
            print('Choose a valid number please')

    return user_preference
################ END USER PREFERENCE FOR CATS AND DOGS ##########################



############# FUNCTION FOR GETTING THE USERS EMOTIONAL STATUS #####################
    #getting the users input and validating   
def get_user_input():
    #assgined each number to an emotion
    happy = 1
    angry = 2
    confused = 3
    sad = 4
    scared = 5
    laugh = 6
    
    #need to prompt user with a list of emotions they could be feeling
    print('We have a list of six emotions you can choose from, depending on your emotion we will show you a picture of a kitten to cheer you up')
    
    #print the list of emotions
    print('Emotion', '   ', 'Number')
    print('---------------------')
    print('Happy', '\t', '\t', happy)
    print('Angry', '\t', '\t', angry)
    print('Confused', '\t', confused)
    print('Sad', '\t', '\t', sad)
    print('Scared', '\t', '\t', scared)
    print('If you just want to laugh', '\t', laugh)

    #need to validate the user input
    emotion = False

    #while loop for valid input on user emotion
    while emotion == False:
        
        try:
            emotion_num = int(input('What is your choice?: '))
            
        except ValueError:
            print('That is not an option')
        except TypeError:
            print('That is not an option')
        except NameError:
            print('That is not an option')

        try:           
            if emotion_num >= 1 and emotion_num <= 6:
                emotion = True
            else:
                print('Choose a valid number please')
        except UnboundLocalError:
            print('Choose a valid number please')
    #returning the valid user input
    return (emotion_num)
#####################  END EMOTIONAL INPUT  #########################


##################### FINDING KITTEN PICTURE FUNCTION #########################
#creating kitten image finder function
def kitten_image_finder(emotion_num):

#make if statements for selecting cat photos
    #if user happy
    if emotion_num == 1:

        cat_num = str(random.randint(1, 10))
        message = 'https://scnardon.w3.uvm.edu/cs008/PythonCSFair/kitten' + cat_num + '.jpeg'
        webbrowser.open('https://scnardon.w3.uvm.edu/cs008/PythonCSFair/kitten' + cat_num + '.jpeg')
#figure out way to get website up
        

    #if user angry
    if emotion_num == 2:
    #get random number
        cat_num = str(random.randint(1, 10))
    #Will open webbrowser to a cat meme
        message = 'https://scnardon.w3.uvm.edu/cs008/PythonCSFair/angrykitten' + cat_num + '.jpeg'
        webbrowser.open('https://scnardon.w3.uvm.edu/cs008/PythonCSFair/angrykitten' + cat_num + '.jpeg')
#figure way to get website up
        
    #if user confused
    if emotion_num == 3:
    #get random number
        cat_num = str(random.randint(1, 10))
    #Will open webbrowser to a cat meme
        message = 'https://scnardon.w3.uvm.edu/cs008/PythonCSFair/conkitten' + cat_num + '.jpeg'
        webbrowser.open('https://scnardon.w3.uvm.edu/cs008/PythonCSFair/conkitten' + cat_num + '.jpeg')
        

    #if user sad
    if emotion_num == 4:
        #get random number
        cat_num = str(random.randint(1, 10))
    #Will open webbrowser to a cat meme
        message = 'https://scnardon.w3.uvm.edu/cs008/PythonCSFair/sadkitten' + cat_num + '.jpeg'
        webbrowser.open('https://scnardon.w3.uvm.edu/cs008/PythonCSFair/sadkitten' + cat_num + '.jpeg')
        

    #if user scared
    if emotion_num == 5:
        #get random number
        cat_num = str(random.randint(1, 10))
        #Will open webbrowser to a cat meme
        webbrowser.open('https://scnardon.w3.uvm.edu/cs008/PythonCSFair/scarkitten' + cat_num + '.jpeg')


    #if user wants to laugh
    if emotion_num == 6:
        #get random number
        cat_num = str(random.randint(1, 15))
        #Will open webbrowser to a cat meme
        message = 'https://scnardon.w3.uvm.edu/cs008/PythonCSFair/funkitten' + cat_num + '.jpeg'
        webbrowser.open('https://scnardon.w3.uvm.edu/cs008/PythonCSFair/funkitten' + cat_num + '.jpeg')


################### END FINDING KITTEN PICTURE FUNCTION ########################


########################### FINDING DOG FUNCTON ################################
def puppy_image_finder(emotion_num):
    
    #make if statements for selecting dog photos
    #if user happy
    if emotion_num == 1:
        #get random number
        dog_num = str(random.randint(1, 10))
        #will open web browser to a happy dog
        message = 'https://scnardon.w3.uvm.edu/cs008/PythonCSFair/puppy' + dog_num + '.jpeg'
        webbrowser.open('https://scnardon.w3.uvm.edu/cs008/PythonCSFair/puppy' + dog_num + '.jpeg')
        

    #if user angry
    if emotion_num == 2:
    #get random number
        dog_num = str(random.randint(1, 10))
    #Will open webbrowser to a angry dog meme
        message = 'https://scnardon.w3.uvm.edu/cs008/PythonCSFair/angrypup' + dog_num + '.jpeg'
        webbrowser.open('https://scnardon.w3.uvm.edu/cs008/PythonCSFair/angrypup' + dog_num + '.jpeg')

        
    #if user confused
    if emotion_num == 3:
    #get random number
        dog_num = str(random.randint(1, 10))
    #Will open webbrowser to a confused dog meme
        message = 'https://scnardon.w3.uvm.edu/cs008/PythonCSFair/conpup' + dog_num + '.jpeg'
        webbrowser.open('https://scnardon.w3.uvm.edu/cs008/PythonCSFair/conpup'+ dog_num + '.jpeg')
        

    #if user sad
    if emotion_num == 4:
        #get random number
        dog_num = str(random.randint(1, 10))
    #Will open webbrowser to a sad dog meme
        message = 'https://scnardon.w3.uvm.edu/cs008/PythonCSFair/sadpup' + dog_num + '.jpeg'
        webbrowser.open('https://scnardon.w3.uvm.edu/cs008/PythonCSFair/sadpup'+ dog_num + '.jpeg')
        

    #if user scared
    if emotion_num == 5:
        #get random number
        dog_num = str(random.randint(1, 10))
        #Will open webbrowser to a scared dog meme
        message = 'https://scnardon.w3.uvm.edu/cs008/PythonCSFair/scarpup' + dog_num + '.jpeg'
        webbrowser.open('https://scnardon.w3.uvm.edu/cs008/PythonCSFair/scarpup'+ dog_num + '.jpeg')
        

    #if user wants to laugh
    if emotion_num == 6:
        #get random number
        dog_num = str(random.randint(1, 16))
        #Will open webbrowser to a dog meme
        message = 'https://scnardon.w3.uvm.edu/cs008/PythonCSFair/funpup' + dog_num + '.jpeg'
        webbrowser.open('https://scnardon.w3.uvm.edu/cs008/PythonCSFair/funpup' + dog_num + '.jpeg')

################### END FINDING DOG PICTURE FUNCTION ###########################
#####################email funciton to send picture ###############################
def email_picture(toaddr):
    with open('catmessage.txt') as fp:
        msg = EmailMessage()
        msg.set_content(fp.read())
    msg['Subject'] = ('cat pictures')
    msg['From'] = 'samuel.nardone12@gmail.com'
    msg['To'] = toaddr

    #send message via SMTP server
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
    

main() 
        
        
