from gtts import gTTS
import os
  
class Tts():
    def __init__(self, main):
        self.main = main
        self.lang = "en"

    def text_speach(self, text):
        The_response = text
        myobj = gTTS(text=The_response, lang=self.lang, slow=False)
        myobj.save(self.main.tts_name + ".mp3")
        os.system("mpg123" + self.main.tts_name + ".mp3")