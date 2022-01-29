class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

class Linked_List(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isempty(self):
        return not bool(self.head)

    def add_first(self, item):
        node = Node(item)
        if not self.isempty():
            node.pointer = self.head
            self.head = node
        else:
            self.head = node
        self.length += 1

    def add_last(self, item):
        if not self.isempty():
            node = self.head
            while node.pointer:
                node = node.pointer
            node.pointer = (Node(item))
        else:
            self.head = Node(item)
        self.length += 1

    def insert(self, pos, item):
        if not self.isempty():
            if pos == 0:
                self.add_first(item)

            elif pos == self.length:
                self.add_last(item)

            else:
                node = self.head
                cnt = 0
                while pos > 0 and pos < self.length:
                    if cnt == pos - 1:
                        new_node = Node(item, node.pointer)
                        node.pointer = new_node
                        break
                    node = node.pointer
                    cnt += 1
                self.length += 1
        else:
            print('list is empty')

    def remove(self, target):
        if not self.isempty():
            node = self.head
            if node.value == target:
                self.head = node.pointer
                self.length -=1
                return True
            else:
                prev = node
                node = node.pointer
                while node:
                    if node.value == target:
                        prev.pointer = node.pointer
                        node = None
                        self.length -= 1
                        return True
                    prev = node
                    node = node.pointer
                return False
        else:
            print('list is empty')
            return False

    def search_target(self, target):
        if not self.isempty():
            pos = 0
            node = self.head
            while node:
                if node.value == target:
                    return pos
                node = node.pointer
                pos += 1
            return False
        else:
            print('list is empty')
            return False

    def search_pos(self, pos):
        if not self.isempty():
            cnt = 0
            node = self.head
            while node:
                if cnt == pos:
                    return node.value
                node = node.pointer
                cnt += 1
            return False
        else:
            print('list is empty')
            return False

    def size(self):
        return self.length

    def print(self):
        if not self.isempty():
            node = self.head
            while node:
                print(node.value, end=' ')
                node = node.pointer
            print()
        else:
            print('list is empty')

if __name__ == '__main__':
    list = Linked_List()
    print(list.isempty())
    list.add_last(5);    print('size is ', list.size()); list.print()
    list.add_last(9);    print('size is ', list.size()); list.print()
    list.add_first(3);    print('size is ', list.size()); list.print()
    list.insert(2, 7);    print('size is ', list.size()); list.print()
    list.insert(0, 8);    print('size is ', list.size()); list.print()
    list.remove(8);    print('size is ', list.size()); list.print()