<head>
  <title>Tkinter Event Examples</title>
  <link rel="“canonical”" href="https://tkinterexamples.com/events">
  <meta content=
  "Examples for using python tkinter events to handle button clicks, key presses, and window configurations."
  name="description">
  <meta content=
  "tkinter event examples,python gui events,tkinter events,python tkinter events tutorial,tkinter python events,python gui events tutorial,tkinter bind, tkinter bind examples"
  name="keywords">
</head>

## Events
Events in `tkinter` are all the command inputs that can happen inside your application such as mouse movements / clicks, keyboard entries, window resizes, widget introduction, the list goes on. Generally there are two types of events, those which are built into a widget and those which are explicitly bound to a widget.

### Implicit Events
Some widgets have events built into them such as the `Button` widget which takes a `command=` argument. When we click the button, the callable in our command parameter will be called. Some other widgets with built in event bindings (via `command=`) are:

- `Checkbutton` - called on selection
- `Radiobutton` - called on selection
- `Scale` - called on update (movement of scale widget)
- `Scrollbar` - called on update (movement of scrollbar)
- `Spinbox` - called on update (new value selected)

### Explicitly-Bound Events
There are many events which can be bound to any widget with the syntax: `widget.bind("<Event-Specifier>", callable_handler)`. This causes the specified handler to get called whenever the event occurs. Note that we can also bind events to our container
objects such as `Tk, Frame, & TopLevel`

- [Keyboard Events](/events/keyboard)
- [Mouse Events](/events/mouse)
- [Window Events](/events/window)

#### Binding Options
There are multiple ways to bind events to widgets in `tkinter`:

- `.bind()` - bind to the specific widget only (instance binding)
- `.bind_class()` - bind to the all widgets of this class (class binding)
- `.bind_all()` - bind across the whole application (application binding)

Be aware that `.bind_class()` can get in the way of default widget behavior since this is how tkinter itself implements default behaviors for widgets. The preferred method is creating a widget class that inherits from the base class and configures a bind on instantiation.

```
class BoundButton(tkinter.Button):
def __init__(self, master, **kw):
  apply(tkinter.Button.__init__, (self, master), kw)
  self.bind("<Return>", lambda event: print(event))
```

#### Declaring Callables
When we declare callables to act as event handlers we should take note that the triggering event will pass an `event object` (see below) into our callable function. This means we should define our event handlers with one parameter. Implicit events sometimes have the additional argument.

```
def keyboard_handler(event):
print(event.char)

def mouse_handler(event):
print(event.x, event.y)
print(event.char) # prints ??
```

Note that we can also pass callables directly into the `.bind()` function using lambdas.

```
root.bind("k", lambda event: print("k was pressed!"))
```

#### The Event Object
The event object passed into our event-handlers has many attributes. Some of the commonly used ones are:

- `widget` - the widget which generated the event
- `type` - the type of event this is (equal to inner text of the event specifier)
- `x, y` - the position of the mouse relative to the bound widget (mouse events
only)
- `num` - the mouse button pressed (mouse events only)
- `char` - the pressed key as a character literal (keyboard events only)
- `keycode, keysym` - the pressed key as a code or symbol (keyboard events only)
