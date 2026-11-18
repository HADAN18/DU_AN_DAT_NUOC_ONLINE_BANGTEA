
class Auth:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if not username or not password:
            return False

        if username in self.users:
            return False

        self.users[username] = password
        return True

    def login(self, username, password):
        if username in self.users:
            if self.users[username] == password:
                return True

        return False
