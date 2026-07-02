class Command:
    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError


class TextEditor:
    def __init__(self):
        self.text = ""
        self._history = []

    def execute(self, command):
        command.execute()
        self._history.append(command)

    def undo(self):
        if self._history:
            self._history.pop().undo()


class InsertCommand(Command):
    def __init__(self, editor, text):
        self._editor = editor
        self._text = text

    def execute(self):
        self._editor.text += self._text

    def undo(self):
        self._editor.text = self._editor.text[:-len(self._text)]


if __name__ == "__main__":
    editor = TextEditor()
    editor.execute(InsertCommand(editor, "Hello"))
    editor.execute(InsertCommand(editor, " World"))
    print(editor.text)   # Hello World
    editor.undo()
    print(editor.text)   # Hello
