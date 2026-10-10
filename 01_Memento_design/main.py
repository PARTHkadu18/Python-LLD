from history import History
from text_editor import TextEditor
from text_memento import TextMemento

text_editor = TextEditor();
history=History()

text_editor.write("Hello ")
text_editor.write("World")
history.save_state(text_editor.save())

text_editor.write("This is fun")
history.save_state(text_editor.save())

print(text_editor.get_text())
text_editor.restore(history.undo())
print(text_editor.get_text())
text_editor.restore(history.undo())
print(text_editor.get_text())