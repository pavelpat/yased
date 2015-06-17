# yased - yet another simplest events dispatcher

Using yased example
-------------------

```
from yased import EventsDispatcher, Event


class OnClickEvent(Event):
    pass

 
def on_click(arg_1, kwarg_1, **kwargs):
    print(arg_1, kwarg_1)


ed = EventsDispatcher()
ed.connect(on_click, OnClickEvent)
ed.send(OnClickEvent('Hello', kwarg_1=' World!'))
```