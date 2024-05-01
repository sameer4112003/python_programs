class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def find_middle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr.data

    def merge_sorted(self, other):
        if not self.head:
            return other.head
        if not other.head:
            return self.head

        merged_list = LinkedList()
        current_self = self.head
        current_other = other.head

        while current_self and current_other:
            if current_self.data < current_other.data:
                merged_list.append(current_self.data)
                current_self = current_self.next
            else:
                merged_list.append(current_other.data)
                current_other = current_other.next

        while current_self:
            merged_list.append(current_self.data)
            current_self = current_self.next

        while current_other:
            merged_list.append(current_other.data)
            current_other = current_other.next

        return merged_list

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Function to get user input for a linked list
def create_linked_list():
    linked_list = LinkedList()
    while True:
        data = input("Enter data for the linked list (type 'done' to finish): ")
        if data == "done":
            break
        linked_list.append(int(data))
    return linked_list

# Main function to interact with the user
def main():
    linked_list = create_linked_list()
    while True:
        print("\nChoose an operation:")
        print("1. Insert at the beginning")
        print("2. Insert at the end")
        print("3. Delete an element")
        print("4. Search for an element")
        print("5. Reverse the list")
        print("6. Find the middle element")
        print("7. Merge sorted lists")
        print("8. Display the linked list")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            data = input("Enter data to insert at the beginning: ")
            linked_list.prepend(int(data))
        elif choice == "2":
            data = input("Enter data to insert at the end: ")
            linked_list.append(int(data))
        elif choice == "3":
            data = input("Enter data to delete: ")
            linked_list.delete(int(data))
        elif choice == "4":
            data = input("Enter data to search: ")
            if linked_list.search(int(data)):
                print("Element found in the linked list.")
            else:
                print("Element not found in the linked list.")
        elif choice == "5":
            linked_list.reverse()
            print("Linked list reversed.")
        elif choice == "6":
            print("Middle element of the linked list:", linked_list.find_middle())
        elif choice == "7":
            other_linked_list = create_linked_list()
            merged_list = linked_list.merge_sorted(other_linked_list)
            print("Merged sorted lists:")
            merged_list.display()
        elif choice == "8":
            print("Linked list:")
            linked_list.display()
        elif choice == "9":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
