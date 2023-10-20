from scripts.get_config import Config
from scripts.conversation import Conversation
from scripts.gui import Gui_manager


class Main:
    def __init__(self):
        self.start_up()

    def start_up(self):
        self.config = Config(self)
        self.conversation = Conversation(self)
        self.gui_manager = Gui_manager(self)
        

    def run(self):
        self.gui_manager()


if __name__ == "__main__":
    main = Main()
    main.run()