# -*- coding: utf-8 -*-

# Non-blocking gui.get()
# causes thousands of exceptions per second using 100% CPU,
# while the GUI still works.

from guietta import B,  _, Gui, Quit, Empty

counter = 0

gui = Gui(
    
  [  'Enter expression:', '__expr__'  , B('Eval!') ],
  [  'Result:'          , 'result'    , _          ],
  [  'counter'          , _           , Quit       ] )

while True:
    try:
        name, event = gui.get(block=False)
    except Empty:
        counter += 1
        gui.counter.setText(str(counter))
        continue

    if name == 'Eval':
        try:
            result = eval(gui.expr.text())
            gui.result.setText(str(result))
        except Exception as e:
            gui.result.setText('Error: ' + str(e))

    elif name is None:
        break
