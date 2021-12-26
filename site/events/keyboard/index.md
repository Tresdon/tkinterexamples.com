<head>
  <title>Tkinter Keyboard Events</title>
  <link rel="canonical" href="https://tkinterexamples.com/events/keyboard">
  <meta name="description" content="Examples of using keyboard events within a tkinter application">
  <meta name="keywords" content="tkinter keyboard event examples,tkinter keyboard events">
</head>

## Keyboard Events
Capturing keystrokes inside our `tkinter` program.

### Capture All Key Presses
We often want to bind a widget to a key on our keyboard being pressed. The general case for this is using the `<Key>` event type.

```
import tkinter

root = tkinter.Tk()

def key_handler(event):
    print(event.char, event.keysym, event.keycode)

root.bind("<Key>", key_handler)

root.mainloop()
```

This program outputs the following on a few key strokes. Note that for special characters the `event.char` attribute is empty.
```
j j 106
h h 104
7 7 55
6 6 54
. period 46
, comma 44
; semicolon 59
Return 2359309
Caps_Lock 65536
Tab 3145737
```

### Key Presses
Binding to a specific key requires a very simple event specifier - the character of the key you want to bind to. Note that "space" and "<" cannot be used like this (see special keys below) Also note that capitalization matters ("z" is not equal to "Z")

```
root.bind("z", lambda x: print("You pressed lowercase z"))
root.bind("Z", lambda x: print("You pressed capital Z"))
root.bind("3", lambda x: print("You pressed 3"))
```

### Key Sequences
`tkinter` gives us a very easy way to only call a handler if keys were pressed in a specific sequence. This takes advantage of how the `.bind()` method works, requiring a sequence of specifiers for the first argument:

```
root.bind("abc", lambda x: print("You pressed abc in that order"))
root.bind("beef", lambda x: print("ooh yummy!"))
```

### Special Keys
There are some special keys that have distinct event bindings:

- `<Return>` - The return / enter key
- `<Up>, <Down>, <Left>, <Right>` - The arrow keys
- `<space>, <less>` - The space and less than keys, respectively
- `<Shift-Up>, <Alt-Up>, <Control-Up>` - The up key was pressed while a modifier key was pressed


### Keyboard Focus Events
The last thing we need to talk about regarding keyboard events is the "focus" events. These are triggered when keyboard focus has been moved to or from the specified widget. This focus is moved by
using the `focus_set()` method on the widget.

- `<FocusIn>` - Keyboard focus was moved to this widget
- `<FocusOut>` - Keyboard focus was moved out of this widget
