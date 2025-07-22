from collections import deque


# Функция bfs возвращает True, если
# результат поиска в ширину элемента
# desired в дереве tree, начиная с
# элемента start, удачен, и False,
# если нет.
def bfs(tree, start, desired):
    search_queue = deque([start])
    visited = set()
    while search_queue:
        node = search_queue.popleft()
        if node == desired:
            return True
        visited.add(node)
        for neighbor in tree[node]:
            if neighbor not in visited:
                search_queue.append(neighbor)
                visited.add(neighbor)


def test_bfs():
    tree = {
        1: [2, 3, 4],
        2: [5, 6],
        3: [],
        4: [7, 8],
        5: [9, 10],
        6: [],
        7: [11, 12],
        8: [],
        9: [],
        10: [],
        11: [],
        12: []
    }
    if bfs(tree, 1, 11):
        print('OK')
    if bfs(tree, 1, 6):
        print('OK')
    if bfs(tree, 2, 10):
        print('OK')
    if not bfs(tree, 2, 11):
        print('OK')
    if bfs(tree, 4, 12):
        print('OK')
    if not bfs(tree, 4, 10):
        print('OK')


def main():
    test_bfs()


if __name__ == '__main__':
    main()
