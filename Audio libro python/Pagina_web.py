import sys 
from tkinter import *
import textwrap
import random
from googlesearch import search
import pyttsx3
import threading
import speech_recognition as sr
import PyPDF2 as pd
import pywhatkit
import datetime
import wikipedia
from gtts import gTTS
import os
from tkinter.filedialog import askopenfilename
import re 
import webbrowser
from tkinter import messagebox

str2iso_639_1 = {'Abkhaz': 'ab',
                 'Afar': 'aa',
                 'Afrikaans': 'af',
                 'Akan': 'ak',
                 'Albanian': 'sq',
                 'Amharic': 'am',
                 'Arabic': 'ar',
                 'Aragonese': 'an',
                 'Armenian': 'hy',
                 'Assamese': 'as',
                 'Avaric': 'av',
                 'Avestan': 'ae',
                 'Aymara': 'ay',
                 'Azerbaijani': 'az',
                 'Bambara': 'bm',
                 'Bashkir': 'ba',
                 'Basque': 'eu',
                 'Belarusian': 'be',
                 'Bengali; Bangla': 'bn',
                 'Bihari': 'bh',
                 'Bislama': 'bi',
                 'Bosnian': 'bs',
                 'Breton': 'br',
                 'Bulgarian': 'bg',
                 'Burmese': 'my',
                 'Catalan; Valencian': 'ca',
                 'Chamorro': 'ch',
                 'Chechen': 'ce',
                 'Chichewa; Chewa; Nyanja': 'ny',
                 'Chinese': 'zh',
                 'Chuvash': 'cv',
                 'Cornish': 'kw',
                 'Corsican': 'co',
                 'Cree': 'cr',
                 'Croatian': 'hr',
                 'Czech': 'cs',
                 'Danish': 'da',
                 'Divehi; Dhivehi; Maldivian;': 'dv',
                 'Dutch': 'nl',
                 'Dzongkha': 'dz',
                 'English': 'en',
                 'Esperanto': 'eo',
                 'Estonian': 'et',
                 'Ewe': 'ee',
                 'Faroese': 'fo',
                 'Fijian': 'fj',
                 'Finnish': 'fi',
                 'French': 'fr',
                 'Fula; Fulah; Pulaar; Pular': 'ff',
                 'Galician': 'gl',
                 'Ganda': 'lg',
                 'Georgian': 'ka',
                 'German': 'de',
                 'Greek, Modern': 'el',
                 'Guaraní': 'gn',
                 'Gujarati': 'gu',
                 'Haitian; Haitian Creole': 'ht',
                 'Hausa': 'ha',
                 'Hebrew (modern)': 'he',
                 'Herero': 'hz',
                 'Hindi': 'hi',
                 'Hiri Motu': 'ho',
                 'Hungarian': 'hu',
                 'Icelandic': 'is',
                 'Ido': 'io',
                 'Igbo': 'ig',
                 'Indonesian': 'id',
                 'Interlingua': 'ia',
                 'Interlingue': 'ie',
                 'Inuktitut': 'iu',
                 'Inupiaq': 'ik',
                 'Irish': 'ga',
                 'Italian': 'it',
                 'Japanese': 'ja',
                 'Javanese': 'jv',
                 'Kalaallisut, Greenlandic': 'kl',
                 'Kannada': 'kn',
                 'Kanuri': 'kr',
                 'Kashmiri': 'ks',
                 'Kazakh': 'kk',
                 'Khmer': 'km',
                 'Kikuyu, Gikuyu': 'ki',
                 'Kinyarwanda': 'rw',
                 'Kirundi': 'rn',
                 'Komi': 'kv',
                 'Kongo': 'kg',
                 'Korean': 'ko',
                 'Kurdish': 'ku',
                 'Kwanyama, Kuanyama': 'kj',
                 'Kyrgyz': 'ky',
                 'Lao': 'lo',
                 'Latin': 'la',
                 'Latvian': 'lv',
                 'Limburgish, Limburgan, Limburger': 'li',
                 'Lingala': 'ln',
                 'Lithuanian': 'lt',
                 'Luba-Katanga': 'lu',
                 'Luxembourgish, Letzeburgesch': 'lb',
                 'Macedonian': 'mk',
                 'Malagasy': 'mg',
                 'Malay': 'ms',
                 'Malayalam': 'ml',
                 'Maltese': 'mt',
                 'Manx': 'gv',
                 'Marathi (Marāṭhī)': 'mr',
                 'Marshallese': 'mh',
                 'Mongolian': 'mn',
                 'Māori': 'mi',
                 'Nauru': 'na',
                 'Navajo, Navaho': 'nv',
                 'Ndonga': 'ng',
                 'Nepali': 'ne',
                 'North Ndebele': 'nd',
                 'Northern Sami': 'se',
                 'Norwegian': 'no',
                 'Norwegian Bokmål': 'nb',
                 'Norwegian Nynorsk': 'nn',
                 'Nuosu': 'ii',
                 'Occitan': 'oc',
                 'Ojibwe, Ojibwa': 'oj',
                 'Old Church Slavonic, Church Slavonic, Old Bulgarian': 'cu',
                 'Oriya': 'or',
                 'Oromo': 'om',
                 'Ossetian, Ossetic': 'os',
                 'Panjabi, Punjabi': 'pa',
                 'Pashto, Pushto': 'ps',
                 'Persian (Farsi)': 'fa',
                 'Polish': 'pl',
                 'Portuguese': 'pt',
                 'Pāli': 'pi',
                 'Quechua': 'qu',
                 'Romanian': 'ro',
                 'Romansh': 'rm',
                 'Russian': 'ru',
                 'Samoan': 'sm',
                 'Sango': 'sg',
                 'Sanskrit (Saṁskṛta)': 'sa',
                 'Sardinian': 'sc',
                 'Scottish Gaelic; Gaelic': 'gd',
                 'Serbian': 'sr',
                 'Shona': 'sn',
                 'Sindhi': 'sd',
                 'Sinhala, Sinhalese': 'si',
                 'Slovak': 'sk',
                 'Slovene': 'sl',
                 'Somali': 'so',
                 'South Azerbaijani': 'az',
                 'South Ndebele': 'nr',
                 'Southern Sotho': 'st',
                 'Spanish': 'es',
                 'Sundanese': 'su',
                 'Swahili': 'sw',
                 'Swati': 'ss',
                 'Swedish': 'sv',
                 'Tagalog': 'tl',
                 'Tahitian': 'ty',
                 'Tajik': 'tg',
                 'Tamil': 'ta',
                 'Tatar': 'tt',
                 'Telugu': 'te',
                 'Thai': 'th',
                 'Tibetan Standard, Tibetan, Central': 'bo',
                 'Tigrinya': 'ti',
                 'Tonga (Tonga Islands)': 'to',
                 'Tsonga': 'ts',
                 'Tswana': 'tn',
                 'Turkish': 'tr',
                 'Turkmen': 'tk',
                 'Twi': 'tw',
                 'Ukrainian': 'uk',
                 'Urdu': 'ur',
                 'Uyghur, Uighur': 'ug',
                 'Uzbek': 'uz',
                 'Venda': 've',
                 'Vietnamese': 'vi',
                 'Volapük': 'vo',
                 'Walloon': 'wa',
                 'Welsh': 'cy',
                 'Western Frisian': 'fy',
                 'Wolof': 'wo',
                 'Xhosa': 'xh',
                 'Yiddish': 'yi',
                 'Yoruba': 'yo',
                 'Zhuang, Chuang': 'za',
                 'Zulu': 'zu'}

comandos={'saludos':"Buenos dias, es un gusto ayudarte. Soy tu asistente virtual Cortana, por favor para cualquier instruccion llamame por mi nombre y que quieres que realice",
          "escuchar":"Escuchando...",
          "intento":"Vuelve a intentarlo, no reconozco: ",
          "google":"Buscando resultados",
          "replay":"Abriendo pagina Youtube solicitada",
          "pdf":"Ingresa el lenguaje del pdf",
          "word":"Ingrese la palabra seleccionada:",
          "considencia":"Se encontraron las siguientes considencias ",
          "reproduce":"reproduce",
          "buscar":"buscar",
          "hora":"hora",
          "leer":"leer",
          "audiolibro":"audiolibro",
          "salir":"salir"
          }

lenguaje_instruccion='es'
numero_voice=0

mensaje_entrada=input("Ingresa el idioma que desea los comandos-Escriba Spanish o English")

if mensaje_entrada=="English":
    comandos={'saludos':"Good morning, it's a pleasure to help you. I'm your virtual assistant Cortana, please call me by name for any instructions and what you want me to do.",
          "escuchar":"Listening...",
          "intento":"Try again, I do not recognize: ",
          "google":"Searching for results",
          "replay":"Opening Youtube page requested",
          "pdf":"Enter the language of the pdf",
          "word":"Enter the selected word:",
          "considencia":"The following considerations were found",
          "reproduce":"play",
          "buscar":"search",
          "hora":"hour",
          "leer":"read",
          "audiolibro":"audiobook",
          "salir":"exit"}
    lenguaje_instruccion='en'
    numero_voice=1

root = Tk()
root.config(bg="light grey")
root.geometry('300x500+10+500')
root.title('Carolina')
root.iconbitmap('images.ico')
canvas = Canvas(root, width=200, height=200, bg="snow")
canvas.grid(row=0, column=0, columnspan=2)
canvas.place(x=10, y=10, width=280, height=430)

name = 'cortana'
flag = 1
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[numero_voice].id)
engine. setProperty('rate', 150)
engine.setProperty('volume', 0.85)
messages = []

class Me:
    def __init__(self, master, message=""):
        self.master = master
        self.frame = Frame(master, bg="cyan")
        self.i = self.master.create_window(
            270, 390, window=self.frame, anchor="ne")
        Label(self.frame, text=textwrap.fill(message, 20), font=(
            "Sogue", 10), bg="cyan").grid(row=1, column=0, sticky="w", padx=1, pady=3)
        root.update_idletasks()
        ask.delete(0, END)
         
        def talk(text):
            engine.say(text)
            engine.runAndWait()

        engine.say(comandos['saludos'])
        engine.runAndWait()

        # Programa principal 
        def listen():
            flag = 1
            try:
                with sr.Microphone() as source:
                    print(comandos['escuchar'])
                    voice = listener.listen(source)
                    rec = listener.recognize_google(voice, language=lenguaje_instruccion)
                    rec = rec.lower()
                    
                    if name in rec:
                        rec = rec.replace(name, '')
                        flag = run(rec)
                    else:
                        talk(comandos['intento'] + rec)
            except:
                pass
            return flag
       
        def run(rec):
            
            if comandos["reproduce"] in rec:
                music = rec.replace('Play', '')
                talk('Play ' + music)
                pywhatkit.playonyt(music)
                put_answer(comandos["replay"])

            elif comandos["hora"] in rec:
                hora = datetime.datetime.now().strftime('%I:%M %p')
                put_answer(hora)

            elif comandos["buscar"] in rec:
                Google(rec)
                
            elif comandos["leer"] in rec: 
                idioma=input(comandos["pdf"])
                lenguaje=convert(idioma)
                output_text=busqueda_pdf(lenguaje)
                busqueda=input(comandos["word"])
                result = [_.start() for _ in re.finditer(busqueda.lower(), output_text.lower())] 
                print(comandos["considencia"] + str(len(result)))
                for i in range(0,len(result)):
                    print(comandos["considencia"] + i)
                    #messagebox.showinfo(message=(output_text[result[i]:result[i]+150]), title="Se encontro:")
                    #confirmacion=messagebox.askyesno(message="¿Desea que se presente como audiolibro?", title="Asistente virtual")
                    #if confirmacion=='yes':
                    talk(output_text[result[i]:result[i]+150])
                 
            elif comandos["audiolibro"]  in rec: 
                audiolibro()

            elif comandos["salir"] in rec:
                quit()

            else:
                talk(comandos["intento"] + rec)
           
            return flag
     
        flag = 1

        while flag:
            flag = listen()

answers = []

class Assistant:
    def __init__(self, master, answer=""):
        self.master = master
        self.frame = Frame(master, bg="dodger blue")
        self.i = self.master.create_window(
            10, 390 + 40, window=self.frame, anchor="nw")
        Label(self.frame, text=textwrap.fill(answer, 25), font=("Sogue", 10),
              bg="dodger blue").grid(row=1, column=0, sticky="w", padx=1, pady=3)
        root.update_idletasks()

def send_message():
    canvas.move(ALL, 0, -50)
    message = get_audio()
    me = Me(canvas, message)
    messages.append(me)
    #ask.delete(0, END)
    put_answer(message)

def write_message():
    canvas.move(ALL, 0, -50)
    me = Me(canvas, message=ask.get())
    messages.append(me)
    #ask.delete(0, END)
    put_answer(messages)

def put_answer(answer):
    assistant = Assistant(canvas, answer=answer)
    answers.append(assistant)
    canvas.move(ALL, 0, -35)
    canvas.update()
    q = threading.Thread(target=speak(answer))
    q.start()

def key(event=None):
    q = threading.Thread(target=send_message)
    q.start()

def key1(event=None):
    q = threading.Thread(target=write_message)
    q.start()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio)
        except Exception:
            put_answer('Error')
    return said.lower()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    return 

def busqueda_pdf(lenguaje):
    Tk().withdraw()
    filelocation = askopenfilename()
    basename = os.path.basename(filelocation)
    filename = os.path.splitext(basename)[0]

    with open(filelocation, 'rb') as f:

        text = pd.PdfFileReader(f, strict=False)
        language = lenguaje
        output_text = ''

        for pagenum in range (0, text.numPages):
            pageObj = text.getPage(pagenum)
            output_text= output_text + pageObj.extractText()
            output = gTTS(text=output_text, lang=language, slow=False)

    f.close()
    return(output_text)

def audiolibro():
    Tk().withdraw()
    filelocation = askopenfilename()
    basename = os.path.basename(filelocation)
    filename = os.path.splitext(basename)[0]

    with open(filelocation, 'rb') as f:

        text = pd.PdfFileReader(f, strict=False)
        language = 'es'
        output_text = ''

        for pagenum in range (0, text.numPages):
            pageObj = text.getPage(pagenum)
            output_text = output_text + pageObj.extractText()
            output = gTTS(text=output_text, lang=language, slow=False)

        output.save(filename+".mp3")

    f.close()
    return(filename)

def Google(rec):
    print(comandos['google'])
    results = search(rec)
    webbrowser.open_new_tab(next(results))
    canvas.move(ALL, 0, -20)

def convert(langName):
	termino=str2iso_639_1[langName]
	return (termino)

ask = Entry(root, bd=0, width=26, font=("Sogue", 12))
ask.place(x=10, y=450, width=230, height=35)
ask.focus()
ask.insert(0, "")

button = Button(root, justify=LEFT, command=key)
photo = PhotoImage(file="images.png")
button.config(image=photo, width="32", height="30", relief=FLAT)
button.pack(side=LEFT)
button.place(x=250, y=450)

root.bind('<Return>', key1)
root.resizable(width=False, height=False)
root.lift()
root.call('wm', 'attributes', '.', '-topmost', True)
root.update()
root.mainloop()
threading.Thread._keep_alive = False
