# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 UNINETT AS
#
# This file is part of Network Administration Visualized (NAV).
#
# NAV is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License version 2 as published by the Free
# Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.  You should have received a copy of the GNU General Public
# License along with NAV. If not, see <http://www.gnu.org/licenses/>.
#
"""Unit tests for the dispatcher module."""
import types
import unittest
from nav.smsd import dispatcher

class DispatcherHandlerTest(unittest.TestCase):
    """Tests for the DispatcherHandler class.

    Uses a subclass of the DispatcherHandler to provide a fake
    dispatcher loader function.  This loads a faked dispatcher
    module/class that will cooperate with this unit test.

    """
    def setUp(self):
        self.config = {
            'dispatcher': {'dispatcherretry':'30',
                           'dispatcher1':'FakeDispatcher'},
            'FakeDispatcher': {}
            }

    def test_init_with_simple_config(self):
        self.assert_(FakeDispatcherHandler(self.config))

    def test_empty_message_list(self):
        handler = FakeDispatcherHandler(self.config)
        self.assert_(handler.sendsms('fakenumber', []))

    def test_dispatcher_exception(self):
        handler = FakeDispatcherHandler(self.config)
        self.assertRaises(
            dispatcher.DispatcherError,
            handler.sendsms, 'failure', [])

    def test_dispatcher_unhandled_exception(self):
        handler = FakeDispatcherHandler(self.config)
        self.assertRaises(
            dispatcher.DispatcherError,
            handler.sendsms, 'unhandled', [])

class FakeDispatcherHandler(dispatcher.DispatcherHandler):
    def importbyname(self, name):
        print "import by name: %r" % name
        fakemodule = types.ModuleType('fakedispatcher')
        fakemodule.FakeDispatcher = FakeDispatcher
        return fakemodule
    
class FakeDispatcher(object):
    def __init__(self, *args, **kwargs):
        self.lastfailed = None
        pass

    def sendsms(self, phone, msgs):
        print "got phone %r and msgs %r" % (phone, msgs)
        if phone == 'failure':
            raise dispatcher.DispatcherError('FakeDispatcher failed')
        elif phone == 'unhandled':
            raise Exception('This exception should be unknown')
        return (None, 1, 0, 1, 1)
    


# Run all tests if run as a program
if __name__ == '__main__':
    unittest.main()
