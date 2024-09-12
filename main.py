import speech_recognition as sr
import pyttsx3
import requests
import json
import cv2
import face_recognition
import time
import subprocess
import os
from dotenv import load_dotenv

def configure():
    load_dotenv

def recognize_speech_from_mic():
    global text
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        #add index according to the input device, 0 - device/default as in the device settings.
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio,language="en-IN")
            
            #uses google's speech recognition engine so should be online else gonna return speech services down.
            
            print(f"User: {text}")
            return text
        except sr.UnknownValueError:
            print("I didn't quite get that")
            speak_text("I didn't quite get that")
            return ""
        except sr.RequestError as e:
            print(f"Speech services down; {e}")
            return ""

def speak_text(texts):
    #call required properties
    voices = engine.getProperty('voices')
    rate=engine.getProperty('rate')
    #try different indices inside voices[], 0 or 1 for a male and female voice.
    engine.setProperty('voice',voices[1].id)
    r=175
    #speech rate
    engine.setProperty('rate',r)
    engine.say(texts)
    #run and wait for the speech to complete before proceeding
    engine.runAndWait()

def chat(messages):
    global output
    #port is often 11434, get the exact number by hitting the terminal with 'ollama serve' and copy-paste the stuff after tcp.
    #streams one token at a time by following the last parameter
    port = "http://127.0.0.1:11434/api/chat"
    response = requests.post(port,json={"model":selected_model,"messages":messages, "stream":True})
    response.raise_for_status()
    output=""

    for line in response.iter_lines():
        
        body=json.loads(line)
        if "error" in body:
            raise Exception(body["error"])
            
        if body.get("done") is False:
            message=body.get("message","")
            content=message.get("content","")
            output+= content
            #streaming one token at a time
            print(content, end="", flush=True)
        
        if body.get("done",False):
            message["content"]=output
            return message

def face_unlock():

    video_capture=cv2.VideoCapture(0)
    known_face = face_recognition.load_image_file("known_face.jpg")
    known_face_encoding = face_recognition.face_encodings(known_face)[0]

    #pick a single frame
    ret,frame = video_capture.read()
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    face_locations=face_recognition.face_locations(rgb_frame)
    face_encodings= face_recognition.face_encodings(rgb_frame,face_locations)

    if len(face_locations)==0:
            cv2.destroyAllWindows()
            video_capture.release()
            speak_text("Couldn't recognize User's face, retrying in a few seconds")
            print("Couldn't recognize User's face, retrying in a few seconds")
            time.sleep(4)
            face_unlock()

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Compare the found face with the known face
        match = face_recognition.compare_faces([known_face_encoding], face_encoding)

            # If a match is found, display the frame with a rectangle around the face and text overlay
        if match[0]==False:
            not_welcome = "I can't see you there, sir!"
            print(not_welcome)
            speak_text(not_welcome)
            video_capture.release()
            cv2.destroyAllWindows()
            face_unlock()
           
        else:
                # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

                # Draw text 'ASHMIL' near the rectangle
            cv2.putText(frame, 'ASHMIL', (left + 6, bottom - 6), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 255, 0), 1)

                # Display the frame
            cv2.imshow('Face Recognition', frame)
            welcome="Hi there! Good to see you."
            print(welcome)
            speak_text(welcome)
            cv2.waitKey(0)  # Wait for a key press to continue (or modify as per requirement)

            # Release the video capture and close all OpenCV windows
            video_capture.release()
            cv2.destroyAllWindows()


def input_method_reciever():
    global input_method
    input_method = input("Input S for Microphone/Speak. Input T for Keyboard/Type")

def model_select():
    global selected_model
    
    selected_model=int(input("Input 1 for Alice-uncensored based on llama2. \nInput 2 for Alice-censored based on llama3. \nInput 3 for model with better coding skills but lower communication skills."))
    if selected_model==1:
        selected_model="Alice"
    elif selected_model==2:
        selected_model="Alice3"
    elif selected_model==3:
        selected_model="deepseek-coder:6.7b"
def main():

    configure()
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n----------------ALICE by ASHMIL based on llama2-uncensored and llama3-------------------------------------------------------------------------\nINSTRUCTIONS \n\n !READ ME!: The face recognition module will start soon. FACE UNLOCK with Ashmil's face. Right after that press any button to proceed.\n\n\n EXIT : To quit the chat just input 'talk to you later' after you start the conversation.")
    global engine
    
    
    engine = pyttsx3.init()
    messages=[]
    time.sleep(4)
    face_unlock()
    model_select()
    while True:
        
        input_method_reciever()
        if input_method.lower() == "s" :
            print("You have choosen to speak to me, get your microphone ready and wait till you see 'listening...'")
            text = recognize_speech_from_mic()
       
        elif input_method.lower() == "t":
            print("You have choosen to text me, wait a few seconds...")
            time.sleep(2)
            print("\n \n ENTER KEY SENDS THE MESSAGE")
            text = input("~~~")
      
        else :
            print("INVALID INPUT METHOD")

        if text:
            
            if "talk to you later" in text.lower():
                break
           
           
            elif "ashmil" in text.lower():
                print("https://github.com/Ashmil-Kurikkal")
                text = os.getenv('ASHMIL_INFO')
                response = chat(messages)
                messages.append(response)
                speak_text(output)

                
            else:
                messages.append({"role":"user","content":text})
                response = chat(messages)
                messages.append(response)
                speak_text(output)

if __name__ == "__main__":
    main()
