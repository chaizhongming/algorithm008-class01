#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start


class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def move_node_to_header(self, key):
        node=self.hashmap[key]
        node.pre.next=node.next
        node.next.pre=node.pre

        node.pre=self.head
        node.next=self.head.next
        self.head.next.pre=node
        self.head.next=node

    def add_node_to_header(self, key, value):
        new = ListNode(key, value)
        self.hashmap[key] = new
        new.pre=self.head
        new.next=self.head.next
        self.head.next.pre=new
        self.head.next=new

    def pop_tail(self):
        last_node=self.tail.pre
        self.hashmap.pop(last_node.key)
        last_node.pre.next=self.tail
        self.tail.pre=last_node.pre

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_node_to_header(key)
            res = self.hashmap[key].value
        else:
            res = -1
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.move_node_to_header(key)
            self.hashmap[key].value = value
        else:
            if len(self.hashmap) >= self.capacity:
                self.pop_tail()
            self.add_node_to_header(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
