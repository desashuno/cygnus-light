import tkinter as tk
from tkinter import ttk


class Gui_manager:
    def __init__(self, main):
        self.main = main

        # run in cli mode
        if self.main.config.gui_mode == "cli": 
            self.cli_gui = Cli_gui(self.main)
            self.cli_gui.run()
        if self.main.config.gui_mode == "ttk": 
            self.tkinter_gui = Tkinter_gui(self.main)
            self.tkinter_gui.mainloop()
        


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


class Tkinter_gui(tk.Tk):
    def __init__(self, main):
        super().__init__()

        self.main = main
        self.main.conversation.new_conversation()

        # configure the root window
        self.title('My Awesome App')
        self.geometry('600x350')

        # entry
        self.user_response = tk.StringVar()
        self.entry = ttk.Entry(self)
        self.entry["textvariable"] = self.user_response
        self.entry.pack()

        # label
        self.label = ttk.Label(self, text=self.main.config.character_init)
        self.label.pack()

        # button
        self.button = ttk.Button(self, text='Generate')
        self.button['command'] = self.button_generate
        self.button.pack()

    def button_generate(self):
        #self.label["text"] = self.user_response.get()

        #user input
        self.main.conversation.user_input = self.user_response.get()
        print(self.main.conversation.user_input)

        self.main.conversation.response()
        self.label["text"] = self.main.conversation.ai_output["choices"][0]["text"]
            
    
        