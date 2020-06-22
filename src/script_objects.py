class Script:
    def __init__(self, title):
        self.title = title
        self.characters = None
        self.action_lines = None

    def initialize(self, characters, action_lines):
        self.characters = characters
        self.action_lines = action_lines

    def get_all_text_from_all_characters(self):
        output = []
        for name in self.characters:
            output.extend(self.get_all_text_from_one_character(name))
        return output
    
    def get_all_text_from_action_lines(self):
        output = []
        for line in self.action_lines:
            output.append(line.text)
        return output

    def get_all_text_from_one_character(self, name):
        output = []
        for line in self.characters[name].dialogue:
            output.append(line.text)
        return output

        # gets only action and dialogue lines, no scene headers or parentheticals
    def get_whole_script_as_corpus(self):
        corpus = []
        corpus.extend(self.get_all_text_from_all_characters())
        corpus.extend(self.get_all_text_from_action_lines())
        return corpus

class ScriptObject:
    def __init__(self, script):
        self.script = script
        
# eventually may want to find the age and character description
class Character(ScriptObject):
    def __init__(self, script, name):
        super(Character, self).__init__(script)
        self.name = name
        self.dialogue = []

    def add_dialogue(self, line):
        self.dialogue.append(line)

    def __repr__(self):
        return f'Name: {self.name} || Number of Lines: {len(self.dialogue)}'


class ActionLine(ScriptObject):
    def __init__(self, script, text):
        super(ActionLine, self).__init__(script)
        self.text = text

class Dialogue(ScriptObject):
    def __init__(self, script, text, parenthetical):
        super(Dialogue, self).__init__(script)
        self.text = text
        self.parenthetical = parenthetical