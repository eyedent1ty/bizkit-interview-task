from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    # No search parameter, return ALL users
    if not args:
        return USERS
    
    filtered_users = filter_users(args, USERS)
    sorted_users = sort_users(args, filtered_users)

    return sorted_users

# A function used to filter users based on the given criteria
def filter_users(args, users):
    def filter_key(user):
        for key in args.keys():
            if (not is_values_match(key, args, user)):
                continue
            return True
        return False
    
    return list(filter(filter_key, users))

# A function used to sort users based on the order of precedence provided
def sort_users(args, users):
    def sorting_key(user):
        sorted_criteria = []

        for key in args.keys():
            sorted_criteria.append(is_values_match(key, args, user))

        return tuple(sorted_criteria)
    
    return sorted(users, key=sorting_key, reverse=True)

# A helper function that is used for both filtering and sorting of users
def is_values_match(key, args, user):
    if (key == 'id' and args.get('id') == user.get('id')):
        return True
    elif (key == 'age'):
        user_age = int(user.get('age'))
        args_age = int(args.get('age'))
        return user_age >= args_age - 1 and user_age <= args_age + 1
    elif (key in ['name', 'occupation'] and args.get(key).upper() in user.get(key).upper()):
        return True
    return False