# Imagine you run a website that presents users with different coding challenges in levels
# Easy, Medium, and Hard, where users get points for completing challenges.
# An Easy challenge is worth 5 points, a Medium challenge is worth 10 points,
# and a Hard challenge is worth 20 points.

# Create a function that takes in the number of each challenge
# level a user has played and calculates the user's total number of points
# . Keep in mind that a user cannot complete negative challenges,
# so the function should return the string "invalid" if any of the passed parameters are negative.


def score_calculator(easy, med, hard):
    if easy < 0 or med < 0 or hard < 0:
        return "invalid"
    else:
        return (easy * 5
                + med * 10
                + hard * 20)
