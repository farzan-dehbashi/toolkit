def bucket_sort(arr, num_buckets=10):
    """Bucket sort for floats in [0, 1) — O(n) average."""
    if not arr:
        return arr
    buckets = [[] for _ in range(num_buckets)]
    for num in arr:
        idx = int(num * num_buckets)
        idx = min(idx, num_buckets - 1)
        buckets[idx].append(num)
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))
    return result


def bucket_sort_integers(arr):
    """Bucket sort for arbitrary integers."""
    if not arr:
        return arr
    min_val, max_val = min(arr), max(arr)
    if min_val == max_val:
        return arr
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]
    range_val = max_val - min_val
    for num in arr:
        idx = int((num - min_val) / range_val * (num_buckets - 1))
        buckets[idx].append(num)
    return [x for bucket in buckets for x in sorted(bucket)]


if __name__ == "__main__":
    print(bucket_sort([0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]))
    print(bucket_sort_integers([29, 25, 3, 49, 9, 37, 21, 43]))
