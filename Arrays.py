from typing import List

#1 Best Time to Buy and Sell Stock



def maxProfit( prices: List[int]) -> int:
        minprice = prices[0]
        profit = 0
        for i in prices:
            if i > minprice:
                print(i,minprice)
                profit += i - minprice
            minprice = i
        return profit

#2 Rotate Array

##Less effecient

def rotate( nums: List[int], k: int) -> None:
    if k > len(nums):
        k = k % len(nums)
    for x in range(k):
        prev = nums[-1]
        for i in range(0,len(nums)):
            current = nums[i]
            nums[i] = prev
            prev = current
    return

## Effective and passes

def rotate_two( nums: List[int], k: int) -> None:
    len_ = len(nums)
    if k > len_:
        k = k % len_

    end = nums[len_ - k:]

    for x in reversed(end):
        nums.insert(0, x)
        nums.pop()
    return

#3 Contains duplicate



def containsDuplicate( nums: List[int]) -> bool:
     nums_check = set(nums)
     if len(nums_check) < len(nums):
         return True
     return False


#4 Single number

bitch = [1,3,4,5,6,7,7,6,3,5,]

def singleNumber(nums: List[int]) -> int:
    srt = sorted(nums)
    for index, element in enumerate(srt):
	       if index % 2 == 0:
                if index == len(srt)-1: #If last number in list it is unique
                    print(element)
                    return
                if srt[index+1] != element:
                    print(element)
                    return

singleNumber(bitch)

#5 Intersection of Two Arrays



def intersect( nums1: List[int], nums2: List[int]) -> List[int]:
    new = []
    for x in nums1:
        if x in  nums2:
            new.append(x)
            nums2.remove(x)
    return new


#6 Plus One

def plusOne( digits: List[int]) -> List[int]:
    dig = [str(int) for int in digits]
    ints = int("". join(dig)) + 1
    answer = [int(i) for i in str(ints)]
    return(answer)



#7 Move Zeroes

li = [0,1,0,3,12]


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    count = 0
    for x in range(0,len(nums)-1):
        print(x)
        if nums[x] != 0:
            nums.pop(x)
            nums.insert(0,nums[x])
    print(nums)





#8 Two Sum

li =[3,3]
targ = 6

def twoSum(nums: List[int], target: int) -> List[int]:
    ran = 0
    len_ = len(nums)
    for num in range(0,len_):
        for num_2 in range(ran,len_ ):
            if nums[num_2] + nums[num] == targ and num_2 != num:
                return [num,num_2]
            else:
                continue
        ran += 1



#9 Valid Sudoku


sudoku = [["1","2",".",".",".",".","6",".","7"],
          [".",".",".",".",".",".",".",".","5"],
          [".",".","9",".","6",".","4",".","."],
          [".","6",".",".",".",".",".",".","."],
          [".",".",".",".","4",".",".","7","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".","5",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","2"],
          [".","9",".",".",".",".",".",".","."]]

def isValidSudoku(board: List[List[str]]) -> bool:
    #Row check
    for row in sudoku:
        fil_row = list(filter(lambda a: a != '.', row)) #Filter out '.'
        if  containsDuplicate(fil_row) == True: #Use own duplicate checker
            print('False : Row invalid')
            return False

    #Column check
    ## Creating list of columns

    columns = []
    for col_pos in range(0,9):
        columns_temp = []
        for row in sudoku:
            columns_temp.append(row[col_pos])
        columns.append(list(filter(lambda a: a != '.', columns_temp)))

    ## Checking columns List

    for column in columns:
        if containsDuplicate(column) == True:
            print('False : Column invalid')
            return False

    # 3x3 grid check
    ## Creating grids

    master = []
    str,ent = 0,3
    for blah in range(0,3):
        start,end = 0,3
        for grid in range(0,3):
            dexes = []
            for index in range(start,end): # Moves it downwards
                for dex in range(str,ent): # Moves it right horizontal
                    dexes.append(sudoku[index][dex])

                    flatList = [ item for elem in dexes for item in elem if elem != '.']
                    if containsDuplicate(flatList) == True:
                        print(flatList)
                        print('False : 3x3 grid invalid')
                        return False
            master.append(flatList)

            start += 3
            end += 3
        str += 3
        ent += 3
    print(master)





    return True



#10 Rotate Image



matrix = [[1,2,3],[4,5,6],[7,8,9]]



def rotate(matrix: List[List[int]]) -> None:
    revs = list(reversed([x for x in range(0,len(matrix))]))
    dot,master,lens = 0,[],len(matrix)
    for y in range(0,lens):
        temp = []
        for x in revs:
            temp.append(matrix[x][dot])
        dot += 1
        master.append(temp)

    for lis in reversed(master):
        matrix.insert(0,lis)
    del matrix[lens:]
    print(matrix )
