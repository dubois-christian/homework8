class Contact:
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name}: {self.number}"


class Node:
    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size: int = 10):
        if not isinstance(size, int) or isinstance(size, bool) or size <= 0:
            raise ValueError("Table size must be a positive integer.")
        self.size = size
        self.data = [None] * size

    def hash_function(self, key: str) -> int:
        index = 0
        for character in key:
            index = (index * 31 + ord(character)) % self.size
        return index

    def insert(self, key: str, value: str) -> None:
        index = self.hash_function(key)
        current = self.data[index]
        previous = None
        while current is not None:
            if current.key == key:
                current.value.number = value
                return
            previous = current
            current = current.next

        node = Node(key, Contact(key, value))
        if previous is None:
            self.data[index] = node
        else:
            previous.next = node

    def search(self, key: str):
        current = self.data[self.hash_function(key)]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self) -> None:
        for index, head in enumerate(self.data):
            contacts = []
            current = head
            while current is not None:
                contacts.append(f"- {current.value}")
                current = current.next
            contents = " ".join(contacts) if contacts else "Empty"
            print(f"Index {index}: {contents}")


def main():
    table = HashTable(10)
    print("Empty table:")
    table.print_table()
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    assert table.hash_function("Amy") == table.hash_function("May")
    table.insert("Rebecca", "999-444-9999")
    print("\nPopulated table (including a collision and an update):")
    table.print_table()
    print("\nSearch result:", table.search("John"))
    print("Missing contact:", table.search("Chris"))


if __name__ == "__main__":
    main()
