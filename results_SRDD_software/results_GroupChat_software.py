# Software Name: GroupChat
# Category: SocialNetwork
# Description: GroupChat is a social networking software application that allows users to create and participate in group chats with individuals who share common interests or hobbies. Users can join existing groups or create their own and invite others to join. Each group chat has text and multimedia messaging capabilities, allowing users to share content, discuss various topics, and build connections within the group. GroupChat provides a platform for users to engage in meaningful conversations and form communities around specific interests or hobbies.

class GroupChat:
    def __init__(self, group_name, creator):
        """
        Initializes a new group chat.

        Args:
            group_name (str): The name of the group chat.
            creator (str): The username of the group chat creator.
        """
        self.group_name = group_name
        self.creator = creator
        self.members = [creator]
        self.messages = []

    def add_member(self, username):
        """
        Adds a new member to the group chat.

        Args:
            username (str): The username of the member to add.
        """
        if username not in self.members:
            self.members.append(username)
            print(f"{username} has been added to {self.group_name}.")
        else:
            print(f"{username} is already a member of {self.group_name}.")

    def remove_member(self, username):
        """
        Removes a member from the group chat.

        Args:
            username (str): The username of the member to remove.
        """
        if username in self.members:
            self.members.remove(username)
            print(f"{username} has been removed from {self.group_name}.")
        else:
            print(f"{username} is not a member of {self.group_name}.")

    def send_message(self, sender, message, media=None):
        """
        Sends a message to the group chat.

        Args:
            sender (str): The username of the message sender.
            message (str): The message content.
            media (str, optional): The path to a media file (e.g., image, video). Defaults to None.
        """
        if sender in self.members:
            message_data = {
                "sender": sender,
                "message": message,
                "media": media,
                "timestamp": "current_timestamp" #Replace later with actual timestamp
            }
            self.messages.append(message_data)
            print(f"{sender}: {message}")
            if media:
                print(f"  (Media attached: {media})")
        else:
            print(f"{sender} is not a member of {self.group_name} and cannot send messages.")

    def display_messages(self):
        """
        Displays all messages in the group chat.
        """
        print(f"--- Messages in {self.group_name} ---")
        for message in self.messages:
            print(f"{message['sender']}: {message['message']}")
            if message['media']:
                print(f"  (Media: {message['media']})")
        print("--- End of Messages ---")


class GroupChatPlatform:
    def __init__(self):
        """
        Initializes the group chat platform.
        """
        self.groups = {}

    def create_group(self, group_name, creator):
        """
        Creates a new group chat.

        Args:
            group_name (str): The name of the group chat.
            creator (str): The username of the group chat creator.
        """
        if group_name not in self.groups:
            self.groups[group_name] = GroupChat(group_name, creator)
            print(f"Group chat '{group_name}' created by {creator}.")
        else:
            print(f"Group chat '{group_name}' already exists.")

    def join_group(self, group_name, username):
        """
        Allows a user to join an existing group chat.

        Args:
            group_name (str): The name of the group chat to join.
            username (str): The username of the user joining the group.
        """
        if group_name in self.groups:
            self.groups[group_name].add_member(username)
        else:
            print(f"Group chat '{group_name}' does not exist.")

    def get_group(self, group_name):
          """
          Retrieves a group chat object by its name.

          Args:
              group_name (str): The name of the group chat.

          Returns:
              GroupChat: The GroupChat object if found, otherwise None.
          """
          if group_name in self.groups:
              return self.groups[group_name]
          else:
              print(f"Group chat '{group_name}' does not exist.")
              return None

#Example Usage
if __name__ == '__main__':
    platform = GroupChatPlatform()

    # Create a group
    platform.create_group("Python Lovers", "Alice")

    # Join the group
    platform.join_group("Python Lovers", "Bob")
    platform.join_group("Python Lovers", "Charlie")

    # Get the group object
    python_group = platform.get_group("Python Lovers")

    # Send messages
    if python_group:
        python_group.send_message("Alice", "Hello everyone!")
        python_group.send_message("Bob", "Hi Alice! Glad to be here.")
        python_group.send_message("Charlie", "Hey guys!")
        python_group.send_message("Alice", "sharing this image", media="python.png")

        # Display messages
        python_group.display_messages()

    #Try to get a non-existent group
    non_existent_group = platform.get_group("Java Fanatics")

    #Try to join a non-existent group
    platform.join_group("Java Fanatics", "Eve")