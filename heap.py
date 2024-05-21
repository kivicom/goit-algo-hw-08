import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)

    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
total_cost = min_cost_to_connect_cables(cables)
print("Мінімальні загальні витрати на з'єднання кабелів:", total_cost)


def merge_k_lists(lists):
    min_heap = []

    # Ініціалізація купи з першими елементами кожного списку
    for i, l in enumerate(lists):
        if l:
            # (значення, індекс списку, індекс елемента в списку)
            heapq.heappush(min_heap, (l[0], i, 0))

    merged_lists = []

    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_lists.append(value)

        # Додаємо наступний елемент зі списку до купи
        if element_index + 1 < len(lists[list_index]):
            next_tuple = (lists[list_index][element_index + 1], list_index, element_index + 1)
            heapq.heappush(min_heap, next_tuple)

    return merged_lists

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
