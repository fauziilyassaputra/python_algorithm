class Node:
    def __init__(self, val=None):
        self.next = None
        self.prev = None
        self.val = val

class DoublyLinkedList:
    def __init__(self):
        self.linked_list_head = None

    def insert_head(self, new_node):
        if self.linked_list_head is None:
            self.linked_list_head = new_node
        else:
            new_node.next = self.linked_list_head
            self.linked_list_head = new_node

    def insert(self, new_node):
        if self.linked_list_head is None:
            self.insert_head(new_node)
        else:
            temp = self.linked_list_head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def insert_after(self, target, new_Node):
        temp = self.linked_list_head
        while temp.val != target:
            temp = temp.next
        new_Node.next = temp.next
        temp.next = new_Node
        new_Node.prev = temp

    def delete_head(self):
        temp = self.linked_list_head
        self.linked_list_head = temp.next
        self.linked_list_head.prev = None
        temp = None

    def delete_tail(self):
        temp = self.linked_list_head
        if temp.next is None:
            self.delete_head()
            return
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def delete_node(self, target):
        temp = self.linked_list_head
        if temp.val == target:
            self.delete_head()
            return
        else:
            while temp.next.val != target:
                temp = temp.next
            temp.next = temp.next.next
            temp.next.next.prev = temp

    def print_linked_list(self):
        result = []
        temp = self.linked_list_head
        while temp is not None:
            result.append(str(temp.val))
            temp = temp.next
        linked_list_result = " -> ".join(result)
        print(linked_list_result)


if __name__ == "__main__":
    double_linked_list = DoublyLinkedList()
    double_linked_list.insert(Node(5))
    double_linked_list.insert(Node(10))
    double_linked_list.insert(Node(15))
    double_linked_list.insert(Node(25))
    double_linked_list.print_linked_list()
    # 5 -> 10 -> 15 -> 25

    double_linked_list.insert_head(Node(20))
    double_linked_list.print_linked_list()
    # 20 -> 5 -> 10 -> 15 -> 25

    double_linked_list.insert_after(10,Node(13))
    double_linked_list.print_linked_list()
    # 20 -> 5 -> 10 -> 13 -> 15 -> 25

    double_linked_list.delete_head()
    double_linked_list.print_linked_list()
    # 5 -> 10 -> 13 -> 15 -> 25

    double_linked_list.delete_node(13)
    double_linked_list.print_linked_list()
    # 5 -> 10 -> 15 -> 25

    double_linked_list.delete_tail()
    double_linked_list.print_linked_list()
    # 5 -> 10 -> 15


