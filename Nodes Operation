class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")
    def insert_at_end(self, data):
        new_node = Node(data)
        new_node.next = None
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        print(f"Inserted {data} at the end.")
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
def get_data_from_user():
    """Gets data from the user, handling different types."""
    dt = input("Enter data type of the data (int/str):- ").lower()
    if dt == "int":
        try:
            return int(input("Enter the data:- "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return None
    elif dt == "str":
        return input("Enter the data:- ")
    else:
        print("Invalid data type. Please choose 'int' or 'str'.")
        return None
if __name__ == "__main__":
    my_list = LinkedList()
    while True:
        print("\n--- Linked List Operations ---")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Display list")
        print("4. Search for an element")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            data = get_data_from_user()
            if data is not None:
                my_list.insert_at_beginning(data)
        elif choice == '2':
            data = get_data_from_user()
            if data is not None:
                my_list.insert_at_end(data)
        elif choice == '3':
            my_list.display()
        elif choice == '4':
            key = get_data_from_user()
            if key is not None:
                if my_list.search(key):
                    print(f"Key '{key}' found in the list.")
                else:
                    print(f"Key '{key}' not found in the list.")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
