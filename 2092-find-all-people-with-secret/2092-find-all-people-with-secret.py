class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        meetings.sort(key=lambda x: x[2])
        know = {0, firstPerson}
        i = 0

        while i < len(meetings):
            time = meetings[i][2]
            people = set()
            j = i

            while j < len(meetings) and meetings[j][2] == time:
                people.add(meetings[j][0])
                people.add(meetings[j][1])
                j += 1

            parent = {p: p for p in people}

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(x, y):
                parent[find(x)] = find(y)

            for k in range(i, j):
                union(meetings[k][0], meetings[k][1])

            groups = {}
            for p in people:
                root = find(p)
                groups.setdefault(root, []).append(p)

            for group in groups.values():
                if any(p in know for p in group):
                    know.update(group)

            i = j

        return list(know)
        