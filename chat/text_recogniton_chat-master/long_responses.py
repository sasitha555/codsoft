import random

R_WALKING = "Start slowly. If you've been inactive, then start gently with five to 10 minutes at a steady pace, and build up your time and distance over a couple of weeks to months."
R_SHOPPING = "Look at your finances and decide how much you have to spend. Make a budget and stick to it. Don't wrack up debt because you want a new purse."
R_HATE = "to dislike intensely or passionately; feel extreme aversion for or extreme hostility toward; detest."

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response