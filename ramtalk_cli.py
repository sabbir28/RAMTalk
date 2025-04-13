import requests
import argparse
import json
import os

BASE_URL = "http://localhost:8000"

def signup(mobile, name=None, image_path=None):
    data = {"mobile": mobile}
    files = {}

    if name:
        data["name"] = name
    if image_path and os.path.exists(image_path):
        files["image"] = open(image_path, "rb")

    response = requests.post(f"{BASE_URL}/signup", data=data, files=files)
    print(response.json())

def send(from_id, to_id, message):
    payload = {
        "from_id": from_id,
        "to_id": to_id,
        "message": message
    }
    response = requests.post(f"{BASE_URL}/send", json=payload)
    print(response.json())

def receive(user_id):
    response = requests.get(f"{BASE_URL}/receive/{user_id}")
    print(response.json())

def list_users():
    response = requests.get(f"{BASE_URL}/users")
    print(json.dumps(response.json(), indent=2))

def main():
    parser = argparse.ArgumentParser(description="RAMTalk CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Signup
    signup_parser = subparsers.add_parser("signup")
    signup_parser.add_argument("--mobile", required=True, help="Mobile number")
    signup_parser.add_argument("--name", help="Name (optional)")
    signup_parser.add_argument("--image", help="Profile image path (optional)")

    # Send
    send_parser = subparsers.add_parser("send")
    send_parser.add_argument("--from_id", required=True, help="Sender user ID")
    send_parser.add_argument("--to_id", required=True, help="Receiver user ID")
    send_parser.add_argument("--message", required=True, help="Message text")

    # Receive
    recv_parser = subparsers.add_parser("receive")
    recv_parser.add_argument("--user_id", required=True, help="User ID to receive messages")

    # Users
    subparsers.add_parser("users")

    args = parser.parse_args()

    if args.command == "signup":
        signup(args.mobile, args.name, args.image)
    elif args.command == "send":
        send(args.from_id, args.to_id, args.message)
    elif args.command == "receive":
        receive(args.user_id)
    elif args.command == "users":
        list_users()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
