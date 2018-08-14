import pyttsx

engine = pyttsx.init()
#change speech rate
engine.setProperty('rate', 115)

#Loop through the avaliable languages
'''
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   print voice.id
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
'''

#Choose language
engine.setProperty('voice', 12)
with open("wiki.txt") as f:
	for line in f:
		engine.say(line)

engine.runAndWait()

