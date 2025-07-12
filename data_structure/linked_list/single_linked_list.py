class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val
      
# class SingleLinked untuk memanggil single linked list
class SingleLinked:
    # menjadi wadah awal data
    def __init__(self):
        self.head = None

    # method insert untuk menambah Node baru
    def insert(self,new_node):
      # jika node kosong maka buat node baru
        if self.head is None:
            self.head = new_node
        else:
      # jika node sudah ada, maka isi node baru ke node tersebut
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    # method insert_at untuk menambah Node baru setelah node tertentu
    def insert_at(self,target_val,new_node):
        temp = self.head
        # jika isi node tidak sama dengan yang kita inginkan, lanjut cek ke node berikutnya
        while temp.val != target_val:
            temp = temp.next
        # sambungkan setelah node baru dengan setelah node yang ingin ditempatkan
        new_node.next = temp.next
        temp.next = new_node
        temp = None

    # method delete_head untuk menghapus head pada kumpulan node
    def delete_head(self):
        temp = self.head.next
        self.head = None
        self.head = temp

    # method delete_tail untuk menghapus ujung pada kumpulan node
    def delete_tail(self):
        temp = self.head
        # jika isi node hanya satu, gunakan method delete head
        if temp.next is None:
            self.delete_head()
            return
        # jika setelah dua node itu kosong, maka satu node setelahnya merupakan node terakhir
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    # method delete_node untuk menghapus node tertentu
    def delete_node(self,target_val):
        temp = self.head
        if temp.val == target_val:
            self.delete_head()
            return
        while temp.next.val != target_val:
            temp = temp.next
        temp.next = temp.next.next

    # method print_linked untuk menampilkan seluruh node yang ada
    def print_linked(self):
        result = []
        temp = self.head
        while temp is not None:
            result.append(str(temp.val))
            temp = temp.next
        linked_list_result = " -> ".join(result)
        print(linked_list_result)

if __name__ == "__main__":
    my_linked = SingleLinked()
    my_linked.insert(Node(5))
    my_linked.insert(Node(10))
    my_linked.insert(Node(12))
    my_linked.insert(Node(20))
    my_linked.insert(Node(21))
    my_linked.print_linked()
    # 5 -> 10 -> 12 -> 20 -> 21

    my_linked.insert_at(10,Node(6))
    my_linked.print_linked()
    # 5 -> 10 -> 6 -> 12 -> 20 -> 21
  
    my_linked.delete_head()
    my_linked.print_linked()
    # 10 -> 6 -> 12 -> 20 -> 21
    my_linked.delete_tail()
    my_linked.print_linked()
    # 10 -> 6 -> 12 -> 20

    my_linked.delete_node(6)
    my_linked.print_linked()
    # 10 -> 12 -> 20
  
