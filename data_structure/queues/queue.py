class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):    # method untuk menambahkan item
        self.items.append(item)

    def dequeue(self):  # method untuk mengambil data
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def peek(self):     # method untuk melihat awal item
        if not self.is_empty():
            return self.items[0]
        return None

    def size(self): # method untuk melihat ukuran item
        return len(self.items)

    def is_empty(self): # method bool apakah items kosong atau ada
        return len(self.items) == 0

    def __iter__(self): # method untuk menampilkan semua item
        return iter(self.items)


if __name__ == "__main__":
    antrian = Queue()
    antrian.enqueue(1)
    antrian.enqueue(2)
    antrian.enqueue(3)
    antrian.enqueue(4)
    for angka in antrian:
        print(angka)
        # 1
        # 2
        # 3
        # 4

    antrian.dequeue()
    print("setelah hapus data pertama :")
    for angka in antrian:
        print(angka)
        # setelah hapus data pertama :
        # 2
        # 3
        # 4

    print("ukuran: ", antrian.size()) # ukuran : 3
    print("apakah kosong : ", antrian.is_empty()) # apakah kosong :  False
    print("data awal adalah : ", antrian.peek()) # data awal adalah :  2
