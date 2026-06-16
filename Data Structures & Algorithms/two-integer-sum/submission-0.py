class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted(nums)
        """
        Formas de organizar un arreglo en py
        sorted(arreglo)

        arreglo.sort(reversed = True/False)
        True de mayor a menor
        False de menor a mayor
        """
        amount_nums = len(nums)

        for index,num in enumerate(nums):
            rest = target - num

            for index2 in range(index+1,amount_nums):
                if nums[index2] == rest:
                    return [index,index2]


        