from instapy import InstaPy
from instapy.util import smart_run

# login credentials
insta_username = ""
insta_password = ""

# set InstaPy session
# headless_browser=True runs InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # settings
    session.login()
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=5000,
                                    max_following=5000,
                                    min_followers=45,
                                    min_following=77)
    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "comments"],
                                 peak_likes_hourly=45,
                                 peak_likes_daily=560,
                                 peak_comments_hourly=30,
                                 peak_comments_daily=240)
    session.set_do_like(enabled=True, percentage=60)
    session.set_do_comment(enabled=True, percentage=50)
    session.set_dont_like(["pizza", "naked", "nsfw", "bbc", "fishnets", "nudes", "undies", "food", "foodies", "porn", "men", "women", "sex", "bdsm"])

    comments = [u":fire:",
                "hehe love it!",
                "how cute!!",
                u":heart_eyes:"]

    hashtags = ["labradorsofinstagram",
               "chocolatelab_squad",
               "worldoflabs",
               "dogsofbuffalo"]

    # actions
    session.set_comments(comments)
    session.like_by_tags(hashtags, amount=10, interact=False, skip_top_posts=True)

session.end()
