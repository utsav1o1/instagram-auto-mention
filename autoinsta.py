import users as users
from instapy import InstaPy
from instapy import smart_run
from pip._internal.network import session
from time import sleep

InstaPy(username="utsav_jung_karki",
        password="Utsav123")

sleep(20)
# users = session.target_list("username3.txt")
session.set_comments(users, amount=3, randomize=False)
session.set_action_delays(enabled=True, comment=5.2, randomize=True, random_range_from=70, random_range_to=140)


