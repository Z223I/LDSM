try:
    from builtins import object
except ImportError:
    pass

import warnings
import sys


from functools import partial
from transitions import Machine, MachineError, State, EventData
from transitions.core import listify, _prep_ordered_arg


class LDSM():
    def test(self):
        states = ['A', 'B', 'C', 'D']
        # Define with list of dictionaries
        transitions = [
            {'trigger': 'walk', 'source': 'A', 'dest': 'B'},
            {'trigger': 'run', 'source': 'B', 'dest': 'C'},
            {'trigger': 'sprint', 'source': 'C', 'dest': 'D'}
        ]
        m = Machine(states=states, transitions=transitions, initial='A')
        m.walk()
        if (m.state == 'B'):
            print ( "1. Good" )

        # Define with list of lists
        transitions = [
            ['walk', 'A', 'B'],
            ['run', 'B', 'C'],
            ['sprint', 'C', 'D']
        ]
        m = Machine(states=states, transitions=transitions, initial='A')
        m.to_C()
        m.sprint()
        if (m.state == 'D'):
            print ( "2. Good" )


