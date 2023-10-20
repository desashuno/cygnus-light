import yaml


class Config:
    def __init__(self, main):
        self.main = main
        self.load_config()

    def load_config(self):
        self.yaml_config()
        self.config_variables()



    def config_variables(self):

        #character
        self.character_name = self.character["name"]
        self.character_description = self.character["description"]
        self.character_init = self.character["init"]
        self.character_template = self.character["template"]

        # model settings
        self.model_name = self.settings["model"]["name"]
        self.model_path = self.settings["model"]["path"]
        self.model_max_tokens = self.settings["model"]["max_tokens"]
        self.model_temperature = self.settings["model"]["temperature"]
        self.model_top_p = self.settings["model"]["top_p"]
        self.model_top_k = self.settings["model"]["top_k"]


        #cygnus-light-configs

        self.gui_mode = self.settings["gui_mode"]


    def yaml_config(self):
        # gets the AI configuration
        try:
            with open("settings.yaml", "r") as file:
                self.all_settings = yaml.safe_load(file)
            
            self.character = self.all_settings["character"]
            self.settings = self.all_settings["settings"]


        except FileNotFoundError:
            print("config file not found, using default configuration")
            
            self.settings = {
            "model" : {"name" : "Cygnus-7B", 
            "path" : "./models/llama-2-7b-chat.Q2_K.gguf",
            "max_tokens" : 256, 
            "temperature" : 0.7, 
            "top_p" : 0.9, 
            "top_k" : 20},
            "gui_mode" : "cli"
            }

            self.character = {
            "name" : "Cygnus",

            "description" : "Is a local revolutionary AI of the race of Xelkonians, actually it is:  smart, kind, always tries to help",
            
            "init" :  "Hello, I am Cygnus, and I am here for everithing you want.",
            
            "default_template" : "You are a helpful, \
            respectful and honest assistant. Always answer as helpfully as possible, \
            while being safe.  Your answers should not include any harmful, unethical, \
            racist, sexist, toxic, dangerous, or illegal content. \
            Please ensure that your responses are socially unbiased and positive in nature. \
            If a question does not make any sense, or is not factually coherent, \
            explain why instead of answering something not correct. \
            If you don't know the answer to a question, please don't share false information.",

            "template" : "You are a helpful, \
            respectful and honest AI assistant named Cygnus. Always answer as helpfully as possible, \
            while being safe. \
            Please ensure that your responses are socially unbiased and positive in nature. \
            If a question does not make any sense, or is not factually coherent, \
            explain why instead of answering something not correct. \
            If you don't know the answer to a question, please don't share false information."
        }

