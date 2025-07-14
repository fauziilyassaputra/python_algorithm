def bubble_sort(collection):

    panjang = len(collection)

    for i in range(panjang - 1):
        swap = False

        for j in range(panjang - 1 - i):
            if collection[j] > collection[j + 1]:
                swap = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
            if not swap:
                break
    return collection

if __name__ == "__main__":
    data = [7,6,2,4,5]
    unsorted = [int(item) for item in data]
    print(f"sebelum sorting adalah : {unsorted}") # sebelum sorting adalah : [7, 6, 2, 4, 5]
    print(f"setelah sorting adalah : {bubble_sort(unsorted)}") # setelah sorting adalah : [2, 4, 5, 6, 7]
