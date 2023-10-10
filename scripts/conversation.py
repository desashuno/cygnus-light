import llm


class Conversation:
    def __init__(self, main):
        self.main = main

        # conversation parameters
        self.conversation_history = []
        self.conversation_index = 0
        
        

    def new_conversation(self):
        print("loading model...")
        self.model = llm.get_model(self.main.config.model)
        print("model loaded!")



    def response(self):
        self.main.ai_output = self.model.prompt(self.main.user_input, system=self.main.config.character_description)        