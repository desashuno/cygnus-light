class Gui:
    def __init__(self, main):
        self.main = main

        if self.main.config.gui_mode == "cli":
            # run in cli mode
            self.cli_gui()


    def cli_gui(self):
        print(self.main.config.model + " text gen in cli mode...")
        self.main.conversation.new_conversation()
        print("")
        print(self.main.config.character_name + " :> " + self.main.config.character_init)
        
        while True:
            self.main.user_input = input("user :> ")
            self.exceptions()

            # generates the answer
            self.main.conversation.response()
            print(self.main.config.character_name + " :> " + self.main.ai_output.text())

    
    def exceptions(self):

            #exits the chat
            if self.main.user_input == "system.exit":
                print("bye ;)")
                exit()
