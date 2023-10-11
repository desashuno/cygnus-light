from llama_cpp import Llama


class Conversation:
    def __init__(self, main):
        self.main = main
        
        self.user_input=""
        self.ai_output=""
        

        # conversation parameters
        self.conversation_history = []
        self.conversation_index = 0
        
        

    def new_conversation(self):
        print("loading model...")
        self.model = Llama(model_path=self.main.config.model_path)
        print("model loaded!")



    def response(self):
        self.ai_output = self.model("[INST] <<SYS>> \n" + \
            self.main.config.character_template +"\n <</SYS>>" + \
            self.user_input + "[/INST]", \
            max_tokens = self.main.config.model_max_tokens, \
            temperature = self.main.config.model_temperature, \
            top_p = self.main.config.model_top_p, \
            top_k = self.main.config.model_top_k)        