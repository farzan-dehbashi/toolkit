def activity_selection(start, end):
    """Select max number of non-overlapping activities — greedy O(n log n)."""
    activities = sorted(zip(start, end), key=lambda x: x[1])
    selected = [activities[0]]
    for s, e in activities[1:]:
        if s >= selected[-1][1]:
            selected.append((s, e))
    return selected


def fractional_knapsack(weights, values, capacity):
    """Fractional knapsack — greedy by value/weight ratio O(n log n)."""
    items = sorted(zip(values, weights), key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0.0
    for value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            break
    return total_value


if __name__ == "__main__":
    start = [1, 3, 0, 5, 8, 5]
    end =   [2, 4, 6, 7, 9, 9]
    print(activity_selection(start, end))

    print(fractional_knapsack([10, 20, 30], [60, 100, 120], 50))
