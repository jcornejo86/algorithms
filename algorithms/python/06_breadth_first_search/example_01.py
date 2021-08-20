from collections import deque

graph = {}
graph["me"] = ["alice", "bob", "claire"]


search_queue = deque() # Creates a new queue
search_queue += graph["me"] # Adds element to the queue
searched = []

while search_queue:
    person = search_queue.popleft()

    if not person in searched:
        if person_is_seller(person):
            print(person)
            return True
        else:
            search_queue += graph[person] # Add to the queue `person` first degree network
            searched.append(person)

def person_is_seller(name):
    return name[-1] == 'b'
