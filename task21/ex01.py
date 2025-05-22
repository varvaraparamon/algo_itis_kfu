"""
Есть отель в котором К комнат. Есть N запросов на бронирование.
Каждый запрос определяется номером дня начала бронирования и номером
дня окончания бронирования (день окончания исключается). Определить
достаточно имеющихся К комнат, чтобы удовлетворить все запросы на
бронирование или нет. Сложность O(N log N)
"""
import timeit

def can_accommodate(bookings, K):
    events = []
    for start, end in bookings:
        events.append((start, 1))
        events.append((end, -1))
    
    events.sort(key=lambda x: (x[0], x[1]))
    
    current_rooms = 0
    for day, change in events:
        current_rooms += change
        if current_rooms > K:
            return False
    
    return True

bookings1 = [(1, 4), (2, 6), (4, 7)]
K1 = 2
print(can_accommodate(bookings1, K1))
print(timeit.timeit(lambda : can_accommodate(bookings1, K1), number=1000)/1000)