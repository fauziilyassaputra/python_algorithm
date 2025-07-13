from typing import Optional

class BinarySearchTree:
    def __init__(self, data: Optional[int] = None) -> None:
        self.data: Optional[int] = data
        self.left: Optional[int] = None
        self.right: Optional[int] = None
      
    # method insert untuk memasukkan data (node sebelah kiri harus lebih kecil dibanding kanannya)
    def insert(self, new_data: int) -> None:
        if self.data is None:
            self.data = new_data
        # jika data baru lebih kecil dari data sebelumnya, letakkan dikiri) 
        elif new_data < self.data:
            # jika node di kiri kosong maka panggil dengan class yang parameternya data baru tersebut
            if self.left is None:
                self.left = BinarySearchTree(new_data)
            else:
            # jika ada isinya, tambahkan node kiri dengan data baru  
                self.left.insert(new_data)
        # jika data baru lebih besar dari data sebelumnya, letakkan di kanan
        else:
            if self.right is None:
                self.right = BinarySearchTree(new_data)
            else:
                self.right.insert(new_data)
              
    # Traversal(cara mengunjungi node pada tree) :
    # 1. preorder : root node -> leftsubtree -> rightsubtree

    def preorder(self, arr:Optional[list[int]] =None) -> list[int]:
        if arr is None:
            arr = []
        arr.append(self.data)
        if self.left is not None:
            self.left.preorder(arr)
        if self.right is not None:
            self.right.preorder(arr)
        return arr
      
    # 2.inorder : leftsubtree -> root node -> rightsubtree
  
    def inorder(self, arr:Optional[list[int]] = None) -> list[int]:
        if arr is None:
            arr = []
        if self.left:
            self.left.inorder(arr)
        arr.append(self.data)
        if self.right:
            self.right.inorder(arr)
        return arr


    # 3.posorder : leftsubtree -> rightsubtree -> rootnode

    def posorder(self,arr:Optional[list[int]] = None) -> list[int]:
        if arr is None:
            arr = []
        if self.left:
            self.left.posorder(arr)
        if self.right:
            self.right.posorder(arr)
        arr.append(self.data)
        return arr



if __name__ == "__main__":
    root = BinarySearchTree()
    root.insert(4)
    root.insert(5)
    root.insert(3)
    root.insert(7)
    preorder_result = root.preorder()
    print(preorder_result)
    # [4, 3, 5, 7]

    inorder_result = root.inorder()
    print(inorder_result)
    # [3, 4, 5, 7]

    posorder_result = root.posorder()
    print(posorder_result)
    # [3, 7, 5, 4]
