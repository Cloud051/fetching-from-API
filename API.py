import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

class User:
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Email: {self.email}"

def fetch_users(endpoint_url: str = "https://jsonplaceholder.typicode.com/users"):
    try:
        response = requests.get(endpoint_url, timeout=10)
        response.raise_for_status()
        users = response.json()
        return users
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching users: {e}")
        return []

def fetch_posts(user_id: int | None = None):
    base_url = "https://jsonplaceholder.typicode.com/users"
    params = {"userId": user_id} if user_id else {}
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
        return []

def create_user_objects(data_users):
    user_objects = []
    for user in data_users:
        user_obj = User(
            id=user['id'],
            name=user['name'],
            email=user['email'],
            phone=user['phone']
        )
        user_objects.append(user_obj)
    return user_objects

def save_users_to_file(users_data):
    with open("data.txt", "w") as file:
        for user in users_data:
            if isinstance(user, User):
                file.write(f"{user.id},{user.name},{user.email}")

def display_users(user_objects):
    for user in user_objects:
        print(user)

users_data = fetch_users()
user_objects = create_user_objects(users_data)
for user in user_objects:
    print(user)

save_users_to_file(user_objects)