
def swap(list_num, index1, index2):
    list_num[index1], list_num[index2] = list_num[index2], list_num[index1]

class Sorted(object):
    def __init__(self):
        self.list_num = []
        return

    # 选择排序
    def selectionSort(self, x):
        i = 0
        while i < len(x) - 1:
            minindex = i
            j = i + 1
            while j < len(x):
                if x[minindex] > x[j]:
                    minindex = j
                j += 1
            if minindex != i:
                swap(x, i, minindex)
            i += 1
        return x

    # 双向二元选择排序
    def selectionSort2num(self, x):
        i = 0
        while i <= len(x) // 2:
            minindex = i
            maxindex = i
            j = i + 1
            while j < len(x) - i:
                if x[minindex] > x[j]:
                    minindex = j
                if x[maxindex] < x[j]:
                    maxindex = j
                j += 1
            if x[minindex] == x[maxindex]:
                return x
            if minindex != i:
                swap(x, i, minindex)
            if maxindex != len(x) - 1 - i:
                if maxindex != i:
                    swap(x, len(x) - 1 - i, maxindex)
                else:
                    swap(x, len(x) - 1 - i, minindex)
            i += 1
        return x

    # 冒泡
    def BubbleSort(self, x):
        j = len(x) - 1
        while j > 0:
            i = 0
            while i < j:
                if x[i] > x[i + 1]:
                    swap(x, i, i + 1)
                i += 1
            j -= 1
        return x
    # 在最好的情况下，冒泡排序法依然会执行每个循环但不进行任何操作，可以设定一个标记判断冒泡排序法在一次内层循环中是否进行了交换，如果没有，说明算法已经使排好序的，就可以直接返回，不过这种方法只是对最好的情况进行了改进
    def BubbleSort2(self, x):
        j = len(x) - 1
        while j > 0:
            flag = False
            i = 0
            while i < j:
                if x[i] > x[i + 1]:
                    swap(x, i, i + 1)
                    flag = True
                i += 1
            if not flag:
                return x
            j -= 1
        return x

    # 双向冒泡排序
    def BidirectionalBubbleSort(self, x):
        j = 0
        while j <= len(x) // 2:
            flag = False
            for i in range(j, len(x) - j - 1):
                if x[i] > x[i + 1]:
                    swap(x, i, i + 1)
                    flag = True
            for i in range(len(x) - 1 - j, j, -1):
                if x[i] < x[i - 1]:
                    swap(x, i, i - 1)
                    flag = True
            if not flag:
                return x
            j += 1
        return x

    # 插入排序
    def InsertionSort(self, x):
        i = 1
        while i < len(x):
            j = i - 1
            item = x[i]
            while j >= 0 and item < x[j]:
                x[j + 1] = x[j]
                j -= 1
            x[j + 1] = item
            i += 1
        return x

    # 希尔排序（插入排序改进)
    # 希尔算法的逻辑是，先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，
    # 待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序，具体步骤如下：
    #
    # 设定一个较大间隔gap，对所有间隔为gap的数据通过插入排序法进行排序；
    # 执行完之后根据某种逻辑缩小gap（代码中采用除以3取整的办法），重复上述过程，直到gap = 0。
    # 复杂度是O(nlogn)
    def HashSort(self, x):
        gap = round(len(x) * 2 / 3)
        while gap > 0:
            print('gap =  ', gap)
            i = gap
            while i < len(x):
                j = i - gap
                item = x[i]
                while j >= 0 and item < x[j]:
                    x[j + gap] = x[j]
                    j -= gap
                x[j + gap] = item
                i += 1
            gap = round(gap / 3)
        return x

    def quicksort(self, x, l, r):
        if l < r:
            q = self.partition(x, l, r)
            self.quicksort(x, l, q - 1)
            self.quicksort(x, q + 1, r)

    def partition(self, array, l, r):
        x = array[r]
        i = l - 1
        for j in range(l, r):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[r] = array[r], array[i + 1]
        return i + 1


if __name__ == '__main__':
    sort_calc = Sorted()
    array = [1, 5, 3, 6, 2, 9]
    print(sort_calc.selectionSort(array))
    print(sort_calc.selectionSort2num(array))
    print(sort_calc.BubbleSort(array))
    print(sort_calc.BubbleSort2(array))
    print(sort_calc.BidirectionalBubbleSort(array))
    print(sort_calc.InsertionSort(array))
    print(sort_calc.HashSort(array))
    # 快速排序是直接对array的操作。
    sort_calc.quicksort(array, 0, len(array) - 1)
    print(array)
