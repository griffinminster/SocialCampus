from instapy import InstaPy
from instapy import smart_run
import quickstart
import tkinter as tk
from tkinter import simpledialog


def main():
    application_window = tk.Tk()
    username_question = simpledialog.askstring("Input", "What is your Instagram username?")
    if username_question is not None:
        insta_username = username_question
    else:
        print("Sorry! Error!")
        exit(0)

    password_question = simpledialog.askstring("Input", "What is your Instagram password?")
    if password_question is not None:
        insta_password = password_question
    else:
        print("Sorry! Error!")
        exit(0)

    quickstart.main()

    # get an InstaPy session!
    # set headless_browser=True to run InstaPy in the background
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=False)

    with smart_run(session):
        session.set_skip_users(skip_private=False,
                               skip_no_profile_pic=False,
                               skip_business=False)
        # session.set_sleep_reduce(1)

        accs = quickstart.main.final_arr
        session.follow_by_list(accs, times=10000, sleep_delay=0, interact=False)

if __name__ == '__main__':
    main()
