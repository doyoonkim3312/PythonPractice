################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Apr 22, 2021
# Description: This program simulates interactions occurred in server related to
# credentials. Two classes called, Privileges and User, will be made and used.
################################################################################

class Privileges:
    __privs: list = list()

    def __init__(self):
        # Default privileges set (interact and post)
        self.__privs.append("interact")
        self.__privs.append("post")

    def grant(self, permission: str):
        if permission in self.__privs:
            print(f"Permission {permission} is already granted.")
        else:
            self.__privs.append(permission)
            print(f"Granted {permission}")

    def revoke(self, permission: str):
        if permission not in self.__privs:
            print(f"Permission {permission} is already revoked.")
        else:
            self.__privs.remove(permission)
            print(f"Revoked {permission}")

    def get_privs(self):
        return self.__privs


class User:
    __name: str
    __email: str
    privs: Privileges

    def __init__(self, name: str, email: str):
        self.__name = name
        self.__email = email
        self.privs = Privileges()

    def describe_user(self):
        print("User Profile")
        print(f"  Name: {self.__name}\n  Email: {self.__email}\n  Privs: {', '.join(map(str, self.privs.get_privs()))}")



def main():
    aliceUser: User = User("Alice", "alice@example.com")
    aliceUser.describe_user()
    aliceUser.privs.grant("teleport")
    aliceUser.describe_user()
    aliceUser.privs.revoke("post")
    aliceUser.describe_user()



if __name__ == '__main__':
    main()
