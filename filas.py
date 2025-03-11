fila = ['Cliente1', ' Cliente2', 'Cliente3']
print(fila)
fila.append('Cliente4')
print(fila)

atendido = fila.pop(1)
print(fila)

import queue

fila_fifo = queue.Queue()
fila_fifo.put('Primeiro da fila')
fila_fifo.put('Segundo da fila')
print(fila_fifo.qsize())
print(fila_fifo.get())
fila_lifo = queue.LifoQueue()
fila_lifo.put('Primeiro da fila')
fila_lifo.put('Segundo da fila')
fila_lifo.put('Terceiro da fila')
print(fila_lifo.get())

fila_priority = queue.PriorityQueue()
fila_priority.put((2, 'Primeiro da fila'))
fila_priority.put((62, 'Primeiro da fila'))
fila_priority.put((1, 'Primeiro da fila'))
print(fila_priority.get())
