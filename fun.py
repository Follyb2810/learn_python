def greet_user():
    print('we are greeting')
greet_user()

# with props
def greet_user_prop(name):
    print(f"welcome {name}")
greet_user_prop("folly")
def greet_user_props(first_name,last_name):
    print(f"welcome! my first name {first_name} and last name {last_name}")
greet_user_props('folly','babs')
greet_user_props(last_name='folly',first_name='babs')
def get_user(name='folly'):
    print(f"this is user {name}")
get_user()
get_user('follyb with argument')