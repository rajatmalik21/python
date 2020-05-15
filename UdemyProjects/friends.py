#ask user for a list of 3 friends
#for each friend, tell them if they are in the same city
#for each nearby friend, save their name in "nearby_friends.txt"

friends = input("Please enter names of 3 friends, separated by commas ( No spaces please): ").split(',')

people = open('people.txt' , 'r')
people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt','w')
for friend in friends_nearby_set:
    print(f'{friend} is nearby. Meet up!')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()


