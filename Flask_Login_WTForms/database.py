users = {
    'rishu@admin.com': '123456',
    'shivam@admin.com': 'abcdefg'
}


def check_admin_login(admin_id, password):
    if admin_id in users.keys():
        if users[admin_id] == password:
            return True
        else:
            return False
    else:
        return False
