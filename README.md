# yased - yet another simplest events dispatcher

Using yased example
-------------------

```
from yased import EventsDispatcher, Event


class ClickEvent(Event):
    pass

 
def on_click(arg_1, kwarg_1):
    print(arg_1, kwarg_1)


ed = EventsDispatcher()
ed.connect(on_click, ClickEvent)
ed.send(ClickEvent('Hello', kwarg_1=' World!'))
```

Also see tests.

Running tests
-------------

```
python -m unittest discover src 'tests'
# OR
python setup.py test
```

Coverage is 100%!
