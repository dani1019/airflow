def get_sftp():
    print('sftp start')
    

def regist(name, sex, *args):
    print(f'name1: {name}')
    print(f'sex1: {sex}')
    print(f'etc1.: {args}')


def regist2(name, sex, *args, **kwargs):
    print(f'name2: {name}')
    print(f'sex2: {sex}')
    print(f'etc2.: {args}')
    email = kwargs['email'] or None
    phone = kwargs['phone'] or None
    if email:
        print(email)
    if phone:
        print(phone)