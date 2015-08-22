# coding: utf-8

from unittest import TestCase

from yased import EventsDispatcher, Event


class AnyEvent(Event):
    """Represents any event."""


class EventsDispatcherTestCase(TestCase):
    def setUp(self):
        self.ed = EventsDispatcher()

    def test_send(self):
        calls = []

        def handler(*args, **kwargs):
            calls.append(True)

        self.ed.connect(handler, AnyEvent)
        self.ed.send(AnyEvent())
        self.assertEqual(len(calls), 1)

        self.ed.disconnect(handler, AnyEvent)
        self.ed.send(AnyEvent())
        self.assertEqual(len(calls), 1)

    def test_send_with_sender(self):
        calls = []

        def handler(*args, **kwargs):
            calls.append(True)

        self.ed.connect(handler, AnyEvent, self)
        self.ed.send(AnyEvent(), sender=self)
        self.assertEqual(len(calls), 1)

        self.ed.send(AnyEvent())
        self.assertEqual(len(calls), 1)

        self.ed.disconnect(handler, AnyEvent)
        self.ed.send(AnyEvent(), sender=self)
        self.assertEqual(len(calls), 2)

        self.ed.disconnect(handler, AnyEvent, sender=self)
        self.ed.send(AnyEvent(), sender=self)
        self.assertEqual(len(calls), 2)

    def test_send_args_kwargs(self):
        calls = []
        event_args = (1, 2, 3)
        event_kwargs = {'a': 4, 'b': 5, 'c': 6}

        def handler(*args, **kwargs):
            calls.append(True)
            self.assertEqual(args, event_args)
            self.assertEqual(kwargs, event_kwargs)

        self.ed.connect(handler, AnyEvent)
        self.ed.send(AnyEvent(*event_args, **event_kwargs))
        self.assertEqual(len(calls), 1)