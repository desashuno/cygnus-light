from tkinter import *
from tkinter import ttk


class Gui_manager:
    def __init__(self, main):
        self.main = main
        self.cli_gui = Cli_gui(self.main)
        self.tkinter_gui = Tkinter_gui(self.main)

        # run in cli mode
        if self.main.config.gui_mode == "cli": self.cli_gui.run()
        if self.main.config.gui_mode == "gui": self.tkinter_gui.run()
        


class Cli_gui:
    def __init__(self, main):
        self.main = main

    def run(self):
        print(self.main.config.model_name + " text gen in cli mode...")
        self.main.conversation.new_conversation()
        print("")
        print(self.main.config.character_name + " :> " + self.main.config.character_init)
        
        while True:
            self.main.conversation.user_input = input("user :> ")
            self.exceptions()


            # generates the answer
            self.main.conversation.response()
            #print(self.main.config.character_name + " :> " + self.main.ai_output)
            print(self.main.conversation.ai_output["choices"][0]["text"])

    def exceptions(self):
        #key codes
        keyword="system."
        if self.main.conversation.user_input == keyword + "exit":
            print("bye ;)")
            exit()
        if self.main.conversation.user_input == keyword + "model":
            print(self.main.config.model_name)
        if self.main.conversation.user_input == keyword + "reloadcfg":
            self.main.config.load_config()


class Tkinter_gui():
    def __init__(self, main):
        self.main = main
        
    def run(self):
        pass