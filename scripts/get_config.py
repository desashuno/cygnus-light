import llm


class Config:
    def __init__(self, main):
        self.main = main
        self.get_json()
        self.get_character()
        self.config_variables()


    def config_variables(self):

        #character
        self.character_name = self.character["name"]
        self.character_description = self.character["description"]
        self.character_init = self.character["init"]

        # llm settings


        #cygnus-light-configs

        self.model = self.settings["model"]
        self.gui_mode = self.settings["gui_mode"]

    def get_character(self):
        self.character = {
            "name" : "Cygnus",
            "description" : "A revolucionary artificial inteligence",
            "init" :  "Hello, I am Cygnus, and I am here for everithing you want."
        }


    def get_json(self):
        self.settings = {
            "character" : "Cygnus-7B",
            "model" : "Cygnus-7B",
            "gui_mode" : "cli"
            }