import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


# A helper function used to get all the unique numbers for the given argument
def getUniqueNumbers(numbers):
    uniqueNumbers = set() # ensure that there is no duplicate numbers inside the list
    for number in numbers:
        uniqueNumbers.add(number)
    return uniqueNumbers

def is_match(fave_numbers_1, fave_numbers_2):
    arg1 = getUniqueNumbers(fave_numbers_1)
    arg2 = getUniqueNumbers(fave_numbers_2)

    return arg2.issubset(arg1)
