class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self._build(arr, 2 * node + 1, start, mid)
            self._build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, l, r, node=0, start=None, end=None):
        if start is None:
            start = 0
        if end is None:
            end = self.n - 1
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return (self.query(l, r, 2 * node + 1, start, mid) +
                self.query(l, r, 2 * node + 2, mid + 1, end))

    def update(self, i, val, node=0, start=None, end=None):
        if start is None:
            start = 0
        if end is None:
            end = self.n - 1
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if i <= mid:
                self.update(i, val, 2 * node + 1, start, mid)
            else:
                self.update(i, val, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)
    print(st.query(1, 3))   # 15 (3+5+7)
    st.update(1, 10)
    print(st.query(1, 3))   # 22 (10+5+7)
