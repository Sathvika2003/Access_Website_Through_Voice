import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'lisa' in command:
                command = command.replace('lisa', '')
                print(command)
    except:
        pass
    return command


def run_lisa():
    while True:
        command = take_command()
        print(command)
        if 'open youtube' in command:
             youtube = webbrowser.open("youtube.com")
             talk('opening youtube')
        elif 'open google' in command:
              google = webbrowser.open("google.com")
              talk('here you go!!')
        elif 'who is' in command:
              person = command.replace('who is', '')
              info = wikipedia.summary(person, 5)
              print(info)
              talk(info)
        elif 'open stanley' in command:
              stanley = webbrowser.open("stanley.edu.in")
              talk('here you go this is the home page of Stanley college!!')
        elif 'computer science' in command:
              cse = webbrowser.open("stanley.edu.in/cse")
              talk('here is the information about Computer science department of Stanley college')
        elif 'ai and ml' in command:
              aiml = webbrowser.open("stanley.edu.in/computer-science-engineering-ai-ml")
              talk('here is the information about AI and ML department of Stanley college')
        elif 'electronics and communication' in command:
              ece = webbrowser.open("stanley.edu.in/ece")
              talk('here is the information about Electronics and communication department of Stanley college')
        elif 'electrical and electronics' in command:
              eee = webbrowser.open("stanley.edu.in/eee")
              talk('here is the information about Electrical and Electronics department of Stanley college')
        elif 'it' in command:
              it = webbrowser.open("stanley.edu.in/itdept")
              talk('here is the information about IT department of Stanley college')
        elif 'cme' in command:
              cme = webbrowser.open("stanley.edu.in/copy-of-computer-science-engineerin-1")
              talk('here is the information about CME department of Stanley college')
        elif 'ai and ds' in command:
              cse = webbrowser.open("stanley.edu.in/copy-of-computer-science-engineerin")
              talk('here is the information about AI and DS department of Stanley college')
        elif 'mba' in command:
              mba = webbrowser.open("stanley.edu.in/mba")
              talk('here is the information about MBA of Stanley college')
        elif 'about stanley college' in command:
              about = webbrowser.open("stanley.edu.in/about")
              talk('here is the information you want about stanley college')
        elif 'more information' in command:
              why = webbrowser.open("https://www.stanley.edu.in/why-stanley")
              talk('Here is the information about why you should choose Stanley college')
        elif 'administration' in command:
              admin = webbrowser.open("stanley.edu.in/administration")
              talk('here is the information about stanley administration')
        elif 'courses' in command:
              courses = webbrowser.open("stanley.edu.in/courses-offered")
              talk('here you go, these are the courses offered by stanley college')
        elif 'admissions' in command:
              admission = webbrowser.open("stanley.edu.in/admissions")
              talk('here is the information about admissions and admission process in stanley college')
        elif 'almanac' in command:
              almanac = webbrowser.open("stanley.edu.in/almanac")
              talk('here is the almanac of stanley college')
        elif 'student life' in command:
              student = webbrowser.open("stanley.edu.in/studentlife")
              talk('here is the information about a student life in stanley')
        elif 'placements' in command:
              placements = webbrowser.open("stanley.edu.in/placements")
              talk('here is the information about placement cell of stanley college')
        elif 'companies' in command:
              recruiters = webbrowser.open("stanley.edu.in/top-recruiters")
              talk('these are the top recruiters of stanley college')
        elif 'affiliations' in command:
              affiliations = webbrowser.open("stanley.edu.in/affiliations")
              talk('stanley college is affiliated to')
        elif 'recent events' in command:
              recent = webbrowser.open("stanley.edu.in/recent-events")
              talk('these are the recent events in stanley college ')
        elif 'upcoming events' in command:
              upcoming = webbrowser.open("stanley.edu.in/upcoming-events")
              talk('these are the upcoming events in stanley college')
        elif 'syllabus' in command:
              syllabus = webbrowser.open("stanley.edu.in/basic-01")
              talk('here is the syllabus details')
        elif 'payment' in command:
              fee = webbrowser.open("stanley.edu.in/fee")
              talk('here is the fee payment procedure with link')
        elif 'administrative faculty' in command:
              faculty1 = webbrowser.open("https://www.stanley.edu.in/_files/ugd/d15c6e_ed11589caa90459cae986d5f7b73e56e.pdf")
              talk('here are the details of administrative faculty')
        elif 'cs faculty' in command:
              faculty2 = webbrowser.open("https://www.stanley.edu.in/_files/ugd/d15c6e_d0068cf1c78e4862b4cbcb23b4e74d38.pdf")
              talk('here are the details of Computer Science faculty')
        elif 'joke' in command:
              talk(pyjokes.get_joke())
        elif 'ok bye' in command:
              talk('thanks for you time')
              exit()
        else:
             talk('Please say the command again.')


while True:
    run_lisa()
