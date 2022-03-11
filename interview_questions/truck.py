class Solution:
    @staticmethod
    def maximumUnits(boxTypes, truckSize):
        assert len(boxTypes) >= 1 and  len(boxTypes) <= 1000 and 1 <= truckSize and 1000000 >= truckSize, 'Invalid input to truck func'
        boxTypes.sort(key=lambda row: (row[1]), reverse=False)
        cap = truckSize
        items_fit = 0
        while cap > 0:
            items_fit += boxTypes[0][0]
            cap -= 1
            boxTypes[0][1] -= 1
            if boxTypes[0][1] == 0:
                del boxTypes[0]
            if len(boxTypes) == 0:
                break
        return items_fit
if __name__ == '__main__':
    print(Solution.maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4))