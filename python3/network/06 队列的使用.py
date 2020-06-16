from multiprocessing import Queue


q = Queue(3)
q.put('a')
print(q.full())
q.put({'name': 'niu'})
q.put([3, 3])
print(q.full())
print(q.get())
print(q.get())
print(q.get())
print(q.empty())
print(q.get())
