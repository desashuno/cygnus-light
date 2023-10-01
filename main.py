import llm
from scripts.load_model import *
from scripts.tts import Tts


class Main():
    def __init__(self):
        self.new_instance()

        # tts
        self.activate_tts = False
        self.tts_name = "out"

    def new_instance(self):
        self.tts = Tts(self)
        self.model = model


    def run(self):
        self.question = "write a enumerated list of 5 names for a dog"
        #question = input("input: ")

        self.response = model.prompt(self.question)

        if self.activate_tts:
            self.tts.text_speach(self.response.text())
        
        print("Output: " + self.response.text())


if __name__ == "__main__":
    main = Main()
    main.run()