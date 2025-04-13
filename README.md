# 🚀 RAMTalk – Mobile-Based In-Memory Chat API

**RAMTalk** is a lightweight, blazing-fast chat server that stores everything in memory (RAM). It's built for experimentation, local chat systems, testing, and ephemeral messaging — no database, no files, just memory.

---

## 🧠 Concept

- Everything is stored in **RAM only**
- Users register via **mobile number**
- Optional: Name + profile image (max 50KB)
- Supports sending up to **5 messages per user**
- Messages are auto-deleted once fetched
- Now includes **timestamps** on every message

---

## ✅ Features (Implemented)

| Feature                        | Description                                               |
|-------------------------------|-----------------------------------------------------------|
| 📱 Mobile-Only Registration   | Register with just a mobile number                        |
| 🧑 Optional Name & Image      | Attach name and small profile photo (≤50KB)               |
| 💬 Message Queue              | Each user can hold up to 5 messages at once              |
| 🗑️ Auto-Message Clear         | Messages disappear after retrieval                        |
| ⏰ Timestamps                 | Every message includes a sent timestamp                   |
| 🧾 List Users                 | `/users` endpoint shows all registered users              |
| 🧪 Simple CLI Tool            | Send/receive messages via terminal                        |

---

## 🚧 Missing Features

| Missing Feature                | Notes                                                   |
|-------------------------------|---------------------------------------------------------|
| 🔐 Authentication             | No token/session protection yet (open endpoints)        |
| 🛡️ Rate Limiting             | No control over spamming or DDoS                        |
| 🕵️ Message Status            | No message IDs, read receipts, or delivery tracking     |
| 📦 Persistence                | All data lost if server restarts                        |
| 📊 Admin Stats API            | No live stats, memory usage, or tracking endpoints      |

> 💡 These are *intentionally excluded* to keep RAMTalk fast and minimal — but easily extendable!

---

## 💡 Future Ideas

| Idea                          | Description                                              |
|-------------------------------|----------------------------------------------------------|
| 🌐 WebSocket Support         | Real-time messaging over socket                          |
| 🔒 OTP-Based Auth            | Lightweight verification via SMS or dummy OTP            |
| 👻 Self-Destruct Messages    | Auto-delete after X seconds after seen                   |
| 🧾 Export API                | Download all your chats as JSON                          |
| 📲 Mobile UI                 | Flutter/React Native app on top of current API           |
| 🧍 Online Status             | "Last seen" & current activity indicator                 |
| 📂 Image Messages            | Allow small images in messages (with preview)            |
| 📊 CLI `stats` command       | Live memory/queue/user count inside CLI tool             |

---

## 📦 Installation

```bash
pip install fastapi uvicorn python-multipart requests
```

Or use the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Server

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

---

## 🧪 CLI Tool

```bash
python ramtalk_cli.py signup --mobile 017xxxxxxx --name Sabbir --image profile.jpg
python ramtalk_cli.py send --from_id <your_id> --to_id <target_id> --message "Hello"
python ramtalk_cli.py receive --user_id <your_id>
```

---

## 📌 Notes

- ⚠️ All data is lost on server restart.
- 🚫 No database, disk, or external storage used.
- 🤖 Ideal for testing, learning, and private network apps.

---

## 📁 Folder Structure

```
📦RAMTalk/
 ┣ main.py                # FastAPI in-memory server
 ┣ ramtalk_cli.py         # Command line client
 ┣ requirements.txt       # Dependencies
 ┣ requested.txt          # API usage example
 ┗ README.md              # This file
```

---

## 🛠️ Author

Made by Sabbir with ❤️ for RAM-only fast API love.

Let me know if you'd like to:

- Add a logo/banner
- Include screenshots or terminal examples
- Auto-generate sample user data

Ready to push it to GitHub? I can help format and commit it all too.
