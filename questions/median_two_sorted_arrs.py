class Solution:
    @staticmethod
    def solution(arr1, arr2):
        assert len(arr1) >= 1 and len(arr1) <= 1000 and len(arr2) >= 1 and len(arr2) <= 1000 , 'Unexpected size of input arrays'
        if len(arr1) <= 2 and len(arr2) <= 2:
            if len(arr1) == 2 and len(arr2) == 2:
                return (arr1[0]+arr1[1]+arr2[0]+arr2[1])/4
            elif len(arr1) == 2 and len(arr2) == 1:
                return ((arr1[0]+arr1[1])/2 +arr2[0])/2
            elif len(arr1) == 1 and len(arr2) == 2:
                return ((arr2[0]+arr2[1])/2 +arr1[0])/2
            elif len(arr1) == 1 and len(arr2) == 1:
                return (arr1[0]+arr2[0])/2
        if len(arr1) >= 2 and len(arr2) >= 2:
            arr1 = arr1[ len(arr1) // 4:3 * len(arr1) // 4 ]
            arr2 = arr2[ len(arr2) // 4:3 * len(arr2) // 4 ]
            return (Solution.solution(arr1,arr2))
        if len(arr1) >= 2:
            arr1 = arr1[len(arr1)//4:3*len(arr1)//4]
            return (Solution.solution(arr1,arr2))
        if len(arr2) >= 2:
            arr2 = arr2[len(arr2)//4:3*len(arr2)//4]
            return (Solution.solution(arr1, arr2))




if __name__ == '__main__':
    arr1 = [1,2,3]
    arr2 = [1,2,3]
    print(Solution.solution(arr1, arr2))