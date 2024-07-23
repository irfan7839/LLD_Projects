class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_key(self, key):
        self.key = key


class HashMap:
    INITIAL_SIZE = 16

    def __init__(self):
        self.hash_map = [None] * self.INITIAL_SIZE

    def get_hash_code(self, key):
        return key % self.INITIAL_SIZE

    def put(self, key, value):
        has_code = self.get_hash_code(key)
        if self.hash_map[has_code] is None:
            self.hash_map[has_code] = Node(key, value)
        else:
            root = self.hash_map[has_code]
            prev_node = root
            while root:
                if root.key == key:
                    root.value = value
                    return
                prev_node = root
                root = root.next
            prev_node.next = Node(key, value)

    def get(self, key):
        has_code = self.get_hash_code(key)
        if self.hash_map[has_code] is None:
            return None
        root = self.hash_map[has_code]
        while root:
            if root.key == key:
                print(root.value)
                return root.value
            root = root.next


class Hash:
    @staticmethod
    def start():
        has_map = HashMap()
        has_map.put(1, 'ir')
        has_map.put(2, "my")
        has_map.put(3, "name")
        has_map.put(4, "is")
        has_map.put(5, "Shrayansh")
        has_map.put(6, "how")
        has_map.put(7, "are")
        has_map.put(8, "you")
        has_map.put(9, "friends")
        has_map.put(10, "?")

        has_map.get(1)
        has_map.get(8)
        has_map.get(2)
        has_map.get(7)


hash_imp = Hash()
hash_imp.start()
