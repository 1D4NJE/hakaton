from datetime import datetime
messages = []
class Message:
    def __init__(self, sender, content, group_name):
        self.sender = sender
        self.content = content
        self.group_name = group_name
        self.time = {"seconds": datetime.now().second,
                     "minutes": datetime.now().minute,
                     "hours": datetime.now().hour}
        self.date = {"day": datetime.now().day,
                     "month": datetime.now().month,
                     "year": datetime.now().year}
        print(content)

    def __repr__(self):
        return (f"the message sender is {self.sender}\n"
                f"the message content is {self.content}\n"
                f"the group chat name is {self.group_name}\n"
                f"the time is {self.time}\n"
                f"the date is {self.date}\n")
    def get_sender(self):
        return self.sender
    def get_content(self):
        return self.content
    def get_group_name(self):
        return self.group_name
    def get_time(self):
        return f"{self.time['hours']}:{self.time['minutes']}:{self.time['seconds']}"
    def get_date(self):
        return f"{self.date['day']},{self.date['month']},{self.date['year']}"

    def set_content(self, content):
        self.content = content
    def set_group_name(self, group_name):
        self.group_name = group_name


class GroupChat:
    def __init__(self, name, users, forbidden_words, social_media):
        self.name = name
        self.users = users  # Expects a list of User objects
        self.forbidden_words = forbidden_words
        self.social_media = social_media
        self.mid_age = self._calculate_mid_age()

    def _calculate_mid_age(self):
        if not self.users:
            return 0
        ages = sorted([user.age for user in self.users])
        n = len(ages)
        index = n // 2
        if n % 2 != 0:
            return ages[index]
        else:
            return (ages[index - 1] + ages[index]) / 2

    def nickname_to_name(self, identifier):
        for user in self.users:
            if user.nickname == identifier:
                return user.name
            elif user.name == identifier:
                return user.nickname
        return "User not found"

    def get_name(self):
        return self.name

    def get_users(self):# מחזירה את רשימת המשתמשים
        return self.users

    def get_forbidden_words(self):
        return self.forbidden_words

    def get_social_media(self):
        return self.social_media

    def get_mid_age(self):
        return self.mid_age

    def add_forbidden_word(self, word):
        self.forbidden_words.append(word)

    def change_group_name(self, new_name):
        self.name = new_name

    def add_user(self, user):
        self.users.append(user)
        print(f"the user {self.name} has been added to the group")
    def set_mid_age(self):
        self.mid_age = self._calculate_mid_age()

    def remove_forbidden_word(self, word):
        self.forbidden_words.remove(word)

    def remove_user(self, user):
        self.users.remove(user)
        print(f"the user {self.name} has been removed from the group")


class User:
    def __init__(self, GENDER,age,nickname,username,number,user_id):
        if GENDER == "F" or GENDER == "M":
            self.GENDER = GENDER
        else:
            print("GENDER must be F or M")
        self.age = age
        self.nickname = nickname
        self.username = username
        self.number = number
        self.most_used_group = ""
        self.groups = []
        self.user_id = user_id
        self.blocked_users = []

    def send_message (self,message, group_name):
        msg = Message(self.username, message, group_name)
        messages.append(msg)
        return msg
    def block_user(self,user_id):
        if user_id not in self.blocked_users:
            self.blocked_users.append(user_id)
            print(f"User with ID {user_id} has been blocked.")
        else:
            print(f"User with ID {user_id} is already blocked.")


    def exit_group(self,group):
        self.groups.remove(group)


    def join_group(self,group):
        self.groups.append(group)
    def print_user_info(self):
        print(f"the users gender is {self.GENDER}\n"
              f"his age is {self.age}\n"
              f"his nickname is {self.nickname}\n"
              f"his username is {self.username}\n"
              f"his number is {self.number}\n"
              f"his id is {self.user_id}")




def main():
    # יצירת משתמשים
    user1 = User("M", 17, "alon123", "Alon", "0501111111", 1)
    user2 = User("M", 17, "elihav456", "Elihav", "0502222222", 2)
    user3 = User("M", 17, "idan789", "Idan", "0503333333", 3)

    # יצירת קבוצה
    group = GroupChat("Movie Night", [user1, user2, user3], ["bad word"], "WhatsApp")

    # המשתמשים מצטרפים לקבוצה
    user1.join_group(group)
    user2.join_group(group)
    user3.join_group(group)

    # שליחת הודעות
    msg1 = user1.send_message("חבר'ה בא לכם ללכת לסרט?", group.get_name())

    msg2 = user2.send_message("כן אחי נשמע טוב!", group.get_name())

    msg3 = user3.send_message("איזה סרט?", group.get_name())

    msg4 = user1.send_message("אולי איזה אקשן חדש", group.get_name())

    msg5 = user2.send_message("אני זורם", group.get_name())

    # עידן מתעצבן
    msg6 = user3.send_message("די כבר אתם לא מחליטים! bad word", group.get_name())
    for message in messages:
        print(message)
main()
