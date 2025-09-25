from collections import deque

queue = deque(["Citizen1", "Citizen2", "Citizen3", "Citizen4", "Citizen5", "Citizen6"])
# Serve 3 (dequeue)
queue.popleft()
queue.popleft()
queue.popleft()
print("Queue after serving 3:", list(queue))
print("Next to be served:", queue[0])
