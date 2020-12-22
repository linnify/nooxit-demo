users = [
    {
        'email': 'razvan.bretoiu@linnify.com',
        'password': 'test1234',
        'name': 'Razvan Bretoiu',
        'groups': ['users']
    },
    {
        'email': 'vlad.rusu@linnify.com',
        'password': 'test1234',
        'name': 'Vlad Rusu',
        'groups': ['users', 'members']
    }
]


def find_by_email_and_password(email, password):
    for item in users:
        if item["email"] == email and item['password'] == password:
            return item
    return None


def find_by_email(email):
    return next(item for item in users if item["email"] == email)
