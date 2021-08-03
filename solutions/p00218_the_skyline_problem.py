from typing import List


class PriorityQueue:
    def __init__(self):
        self.tree: [(int, int)] = []
        self.key_indices = dict()

    def push(self, key: int, value: int):
        self.tree.append((key, value))
        i = len(self.tree) - 1
        self.key_indices[key] = i
        while i > 0:
            parent = self.parent(i)
            if self.tree[parent][1] < self.tree[i][1]:
                self.tree[parent], self.tree[i] = self.tree[i], self.tree[parent]
                self.key_indices[self.tree[i][0]] = i
                self.key_indices[self.tree[parent][0]] = parent
                i = parent
            else:
                break

    def max(self) -> (int, int):
        if len(self.tree) == 0:
            return None

        return self.tree[0]

    def pop(self) -> (int, int):
        n = len(self.tree)
        popped = self.tree[0]
        self.key_indices.pop(popped[0])

        self.tree[0] = self.tree[n-1]
        self.key_indices[self.tree[0][0]] = 0

        self.tree.pop()
        self.max_heapify(0)
        return popped

    def len(self) -> int:
        return len(self.tree)

    def max_heapify(self, i: int):
        n = len(self.tree)
        l = self.left_child(i)
        r = self.right_child(i)
        if (l < n and self.tree[i][1] < self.tree[l][1]) or (r < n and self.tree[i][1] < self.tree[r][1]):
            j = l
            if r < n and self.tree[l][1] < self.tree[r][1]:
                j = r
            self.tree[j], self.tree[i] = self.tree[i], self.tree[j]
            self.key_indices[self.tree[j][0]] = j
            self.key_indices[self.tree[i][0]] = i

            self.max_heapify(j)

    def remove(self, key):
        index = self.key_indices[key]
        self.key_indices.pop(key)
        n = len(self.tree)
        self.tree[index] = self.tree[n-1]
        self.key_indices[self.tree[index][0]] = index
        self.tree.pop()
        self.max_heapify(index)


    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left_child(i):
        return 2 * i + 1

    @staticmethod
    def right_child(i):
        return 2 * i + 2



class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        queue = PriorityQueue()
        result = []
        items = []
        n = len(buildings)
        for i in range(n):
            b = buildings[i]
            items.append((i, b[0], b[2]))
            items.append((i, b[1], -1))
        # item = (index, x, height)
        items = sorted(items, key=lambda x: x[1], reverse=False)
        for item in items:
            if item[2] != -1:
                queue.push(item[0], item[2])
            else:
                queue.remove(item[0])

            height = queue.max()[1] if queue.max() is not None else 0
            m = len(result)
            # print([item[1], height])
            if m > 0 and result[m-1][0] == item[1]:
                result[m-1] = [item[1], height]
            else:
                result.append([item[1], height])

        processed_result = []
        m = len(result)
        for i in range(0, m):
            if i == 0 or result[i][1] != result[i-1][1]:
                processed_result.append(result[i])


        return processed_result


s = Solution()
print(s.getSkyline([[0, 10, 10], [0, 10, 20], [0, 10, 30], [0, 10, 40], [40, 80, 20], [40, 60, 40]]))

