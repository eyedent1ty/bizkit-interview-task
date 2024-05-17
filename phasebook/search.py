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

    if not args:
        return USERS
    
    filtered_users = filter_users(args, USERS)
    sorted_users = sort_users(args, filtered_users)

    return sorted_users

# A function used to filter users based on the given criteria
def filter_users(args, users):
    def filter_key(user):
        if (
            args.get('id') == user.get('id') or
            args.get('name') in user.get('name') or
            int(args.get('age')) == user.get('age') or
            args.get('occupation') in user.get('occupation')
        ):
            return True
        return False
    
    return list(filter(filter_key, users))

# A function used to sort users based on the order of precedence provided
def sort_users(args, users):
    def sorting_key(user):
        precedence = ['id', 'name', 'age', 'occupation']
        sorted_criteria = []

        for key in precedence:
            if key == 'id':
                sorted_criteria.append(args.get('id') == user.get('id'))
            elif key == 'age':
                sorted_criteria.append(int(args.get('age')) == user.get('age'))
            elif key in ['name', 'occupation']:
                sorted_criteria.append(args.get(key) in user.get(key, ''))

        return tuple(sorted_criteria)
    
    return sorted(users, key=sorting_key, reverse=True)