import llm
from scripts.get_config import Config
from scripts.conversation import Conversation
from scripts.gui import Gui


class Main:
    def __init__(self):
        self.start_up()
        
        self.user_input=""
        self.ai_output=""

    def start_up(self):
        self.config = Config(self)
        self.conversation = Conversation(self)
        self.gui = Gui(self)
        

    def run(self):
        self.gui()


if __name__ == "__main__":
    main = Main()
    main.run()