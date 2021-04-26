################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Apr 22, 2021
# Description: This program simulates interactions occurred in server related to
# credentials. Two classes called, Privileges and User, will be made and used.
################################################################################

class Privileges:
    privs: set

    def __init__(self, defaultPrivs: list):
        # Default privileges set (interact and post)
        self.privs = set(defaultPrivs)

    def grant(self, permission: str):
        if permission in self.privs:
            print(f"Permission {permission} is already granted.")
        else:
            self.privs.add(permission)
            print(f"Granted {permission}")

    def revoke(self, permission: str):
        if permission not in self.privs:
            print(f"Permission {permission} is already revoked.")
        else:
            self.privs.remove(permission)
            print(f"Revoked {permission}")

    def get_privs(self):
        return ', '.join(map(str, sorted(self.privs)))


class User:
    name: str
    email: str
    privs: Privileges

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.privs = Privileges(defaultPrivs=["interact", "post"])

    def describe_user(self):
        print("User Profile")
        print(f"  Name: {self.name}\n  Email: {self.email}\n  Privs: {self.privs.get_privs()}")



def main():
    aliceUser: User = User("Alice", "alice@example.com")
    aliceUser.describe_user()
    aliceUser.privs.grant("teleport")
    aliceUser.describe_user()
    aliceUser.privs.revoke("post")
    aliceUser.describe_user()



if __name__ == '__main__':
    main()
