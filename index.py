from instapy import InstaPy

session = InstaPy(username="melbaachocolab", password="")
session.login()
# session.set_relationship_bounds(enabled=True, max_followers=8500)
# session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
session.like_by_tags(["chocolatelabrador", "chocolatelab", "chocolatelab_squad", "worldoflabs", "labsofinstagram", "dogsofinstagram", "dogsofbuffalo"], amount=10)
session.set_dont_like(["naked", "nsfw", "bbc", "fishnets", "nudes", "undies", "food", "foodies", "porn", "men", "women", "sex", "bdsm"])
# session.set_do_comment(True, percentage=50)
# session.set_comments(["hehe love it!", "how cute!!", ":heart_eyes:"])
session.end()
