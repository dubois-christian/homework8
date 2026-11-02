"""Run with: python -m unittest -v test_hash_table.py"""

import io
import unittest
from contextlib import redirect_stdout

from hash_table import Contact, HashTable, Node


class HashTableTests(unittest.TestCase):
    def test_contact_and_node(self):
        contact = Contact("Riley", "012-456-7890")
        node = Node(contact.name, contact)
        self.assertEqual(str(contact), "Riley: 012-456-7890")
        self.assertEqual(node.key, "Riley")
        self.assertIs(node.value, contact)
        self.assertIsNone(node.next)

    def test_collision_updates_and_missing_name(self):
        table = HashTable(1)  # Force all names into the same chain.
        for name in ("Amy", "May", "John"):
            table.insert(name, "original")
        for name in ("Amy", "May", "John"):
            table.insert(name, "updated")
            self.assertEqual(table.search(name).number, "updated")
        current = table.data[0]
        count = 0
        while current is not None:
            count += 1
            current = current.next
        self.assertEqual(count, 3)
        self.assertIsNone(table.search("Chris"))

    def test_empty_and_populated_output(self):
        table = HashTable(1)
        output = io.StringIO()
        with redirect_stdout(output):
            table.print_table()
            table.insert("Amy", "123")
            table.insert("May", "456")
            table.print_table()
        self.assertEqual(output.getvalue(),
                         "Index 0: Empty\nIndex 0: - Amy: 123 - May: 456\n")

    def test_hash_indices_and_example_collision(self):
        table = HashTable(10)
        for name in ("", "Amy", "May", "Rebecca", "Zoë", "李"):
            self.assertTrue(0 <= table.hash_function(name) < table.size)
        self.assertEqual(table.hash_function("Amy"), table.hash_function("May"))

    def test_invalid_sizes(self):
        for size in (0, -1, 1.5, True):
            with self.assertRaises(ValueError):
                HashTable(size)


if __name__ == "__main__":
    unittest.main()
