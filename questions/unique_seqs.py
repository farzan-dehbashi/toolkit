class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        for item in arr:
            if not (item in dict.keys()):
                dict[item] = 1
            else:
                dict[item] += 1
        occurances = []
        for key in dict.keys():
            occurances.append(dict[key])
        if len(set(occurances)) == len(occurances):
            return True
        else:
            return False