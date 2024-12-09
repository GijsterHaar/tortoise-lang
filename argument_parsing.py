from return_english import ReturnEnglish

class ArgumentParser():

    def __init__(self, program):
        self.program = program
    
    def english(self):
        commands_to_parse = ReturnEnglish(self.program)
        return commands_to_parse.return_english()
