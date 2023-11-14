import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

machine = pyttsx3.init()
    
def talk(text):
    machine.say(text)
    machine.runAndWait()

def get_instruction():
    instruction = ""  # Initialize the instruction variable
    try:
        #Get the default mircophone
        with sr.Microphone() as source:        
            print("listening")
            #listen to command, using AVD(Automatic Voice Detection)
            r.adjust_for_ambient_noise(source)
            speech = r.listen(source)            
            instruction = r.recognize_google(speech).lower()#Recognizes speech using Google as a service: Online
    
            if "george" in instruction:
                instruction = instruction.replace('george', " ")
            print(instruction)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    return instruction

def play_George():
    # Here is where we initialize the 'instruction' variable in the 'play_George' function.
    instruction = get_instruction()
    print(instruction)

    if "tell me about the french place" in instruction:
        talk("Alliance Française de Lusaka promotes the French language, francophone culture, and cross-cultural exchange with other centers and cultures in Zambia and abroad.")
    
    elif 'what is the price for exam registration' in instruction:
        talk("Exam fees may vary depending on the level of exam you wish to write. Please visit our website and fill out the registration form for more information.")
    
    elif 'give me the contact details for the francophone culture event coordinator' in instruction:
        talk("Sorry, I cannot assist you with that information.")
    
    elif 'how are you' in instruction:
        talk('I am fine. How about you?')
    
    elif 'what is your name' in instruction:
        talk('I am George. What can I do for you?')
    
    elif 'can you provide information about the DELF certification?' in instruction:
        talk("DELF (Diplôme d’Etudes en Langue Française) and DALF (Diplôme Approfondi de Langue Française) are official qualifications awarded by the French Ministry of Education to certify the competency of candidates from outside France in the French language.")
    
    else:
        talk('Please repeat')

play_George()
