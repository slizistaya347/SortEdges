def sort_edges(edges):
    """
    Сортирует дуги по начальной и конечной вершинам.
    
    :param edges: Список дуг, где каждая дуга представлена как кортеж (начальная вершина, конечная вершина).
    :return: Отсортированный список дуг.
    """
    return sorted(edges, key=lambda x: (x[0], x[1]))

def main():
    # Пример списка дуг
    edges = [(2, 3), (1, 4), (2, 1), (1, 2), (3, 4)]
    
    # Сортировка дуг
    sorted_edges = sort_edges(edges)
    
    # Вывод отсортированных дуг
    print("Отсортированные дуги:", sorted_edges)

# Тестирование функции
def test_sort_edges():
    assert sort_edges([(2, 3), (1, 4), (2, 1), (1, 2), (3, 4)]) == [(1, 2), (1, 4), (2, 1), (2, 3), (3, 4)]
    assert sort_edges([]) == []
    assert sort_edges([(1, 2)]) == [(1, 2)]
    assert sort_edges([(1, 2), (1, 3), (2, 1)]) == [(1, 2), (1, 3), (2, 1)]
    assert sort_edges([(1, 2), (2, 1), (1, 2)]) == [(1, 2), (1, 2), (2, 1)]

if __name__ == '__main__':
    main()
    test_sort_edges()
    print("Все тесты пройдены успешно.")
