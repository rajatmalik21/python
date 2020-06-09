from collections import deque

friends = deque(('Rolf','Jose','Anne','Charlie','Jen'))

def friends_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    yield from g
#    g.send(None)
 #   while True:
  #      greeting = yield
   #     g.send(greeting)


greeter = greet(friends_upper())
greeter.send(None)
greeter.send('Hello')
print('Hello, world! Multitasking...')
greeter.send('How are you, ')

