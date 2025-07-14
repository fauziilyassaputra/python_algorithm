import random

def bogo_sorting(arr: list[int]) -> list[int]:

    def sudah_disorting(data):
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                return False
        return True

    while not sudah_disorting(arr):
        random.shuffle(arr)
    return arr


if __name__ == "__main__":
    array = [2,5,3,4,0,1]
    print(bogo_sorting(array))
