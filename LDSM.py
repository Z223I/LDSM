from transitions import Machine


states = ['A', 'B', 'C', 'D']
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
    print ( "Good" )



