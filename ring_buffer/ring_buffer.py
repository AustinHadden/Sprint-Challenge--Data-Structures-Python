from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) == 0:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
            return

        if (len(self.storage)) == self.capacity and self.storage.tail.next is None:
            self.storage.tail.next = self.storage.head

        if self.storage.tail.next is None:
            self.storage.add_to_tail(item)
            self.current = self.current.next
        else:
            self.current = self.current.next
            self.current.value = item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        cursor = self.storage.head
        list_buffer_contents.append(cursor.value)
        cursor = cursor.next
        while cursor is not self.storage.head:
            list_buffer_contents.append(cursor.value)
            if cursor.next is None:
                break
            cursor = cursor.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
