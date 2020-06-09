from collections import deque
from types import coroutine

friends = deque(('Rolf','Jose','Anne','Charlie','Jen'))


@coroutine
def friends_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    print('Starting...')
    await g
    print('Ending...')


greeter = greet(friends_upper())
greeter.send(None)
greeter.send('Hello')

greeting = input("Enter a greeting: ")
greeter.send(greeting)

greeting = input("Enter a greeting: ")
greeter.send(greeting)
