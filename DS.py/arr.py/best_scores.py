
arr = [1,12,16,18,20,19.4]

def best_score(scores = []):
    best_score = 0
    for score in scores:
        if score > best_score:
            best_score = score
    scores.remove(best_score)

    second_score = 0
    for score in scores:
        if score > second_score:
            second_score = score

    return (best_score, second_score)
if __name__ == '__main__':
    print(best_score(arr))