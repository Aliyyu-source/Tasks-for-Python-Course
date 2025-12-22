import hashlib
import os

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def ensure_credentials_file_exists() -> None:
    if not os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "w", encoding="utf-8") as f:
            pass


def load_credentials() -> list[tuple[int, str, str]]:
    users: list[tuple[int, str, str]] = []
    ensure_credentials_file_exists()
    with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            row = line.strip()
            if row == "":
                continue
            parts = row.split(DELIMITER)
            if len(parts) != 3:
                continue
            user_id = int(parts[0])
            username = parts[1]
            password_hash = parts[2]
            users.append((user_id, username, password_hash))
    return users


def save_credentials(users: list[tuple[int, str, str]]) -> None:
    with open(CREDENTIALS_FILE, "w", encoding="utf-8") as f:
        for user_id, username, password_hash in users:
            f.write(f"{user_id}{DELIMITER}{username}{DELIMITER}{password_hash}\n")


def register_user() -> None:
    users = load_credentials()
    username = input("Insert username: ")
    password = input("Insert password: ")

    if users:
        next_id = max(u[0] for u in users) + 1
    else:
        next_id = 0

    password_hash = hash_password(password)
    users.append((next_id, username, password_hash))
    save_credentials(users)

    print("User registration completed!\n")


def login_user() -> tuple[bool, int, str]:
    users = load_credentials()
    username = input("Insert username: ")
    password = input("Insert password: ")

    password_hash = hash_password(password)

    for user_id, stored_username, stored_hash in users:
        if stored_username == username and stored_hash == password_hash:
            print("Login successful.\n")
            return True, user_id, stored_username

    print("Login failed.\n")
    return False, -1, ""


def show_main_menu() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")


def show_user_menu() -> None:
    print("User options:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")


def user_session(user_id: int, username: str) -> None:
    while True:
        show_user_menu()
        choice = input("Your choice: ")

        if choice == "1":
            print(f"User profile: id={user_id}, username={username}\n")
        elif choice == "2":
            print("Change password not implemented.\n")
        elif choice == "0":
            print("Logging out.\n")
            break
        else:
            print("Invalid choice.\n")


def main() -> None:
    print("Program starting.")

    while True:
        show_main_menu()
        choice = input("Your choice: ")

        if choice == "1":
            success, user_id, username = login_user()
            if success:
                user_session(user_id, username)

        elif choice == "2":
            register_user()

        elif choice == "0":
            print("Exiting program.\n")
            break

        else:
            print("Invalid choice.\n")

    print("Program ending.")


if __name__ == "__main__":
    main()
