# Group Chat Application in Python

## Project Overview

The **Group Chat Application** is a Python-based program that allows multiple users to communicate with each other in real-time over a network. It uses **socket programming** for client-server communication and **threading** to handle multiple clients simultaneously.

---

## Features

* Real-time messaging between multiple users.
* Each client can send and receive messages concurrently.
* Simple command-line interface.
* Scalable to multiple clients.

---

## Tools and Technologies Used

* **Programming Language:** Python 3.x
* **Libraries:** `socket`, `threading`
* **IDE/Editor:** VS Code / PyCharm / Any text editor
* **Platform:** Cross-platform (Windows, Linux, MacOS)

---

## How It Works

1. **Server:**

   * Listens for incoming client connections.
   * Creates a separate thread for each connected client.
   * Broadcasts messages from one client to all others.

2. **Client:**

   * Connects to the server using IP address and port.
   * Sends messages to the server.
   * Receives messages from the server in real-time.

---

## Setup Instructions

1. **Clone the Repository**

```bash
git clone <repository-url>
cd group-chat-python
```

2. **Run the Server**

```bash
python server.py
```

3. **Run the Client(s)**

```bash
python client.py
```

* You can run multiple clients to simulate a group chat.
* Enter messages in the client terminal to send messages to all connected users.

---

## Code Structure

* `server.py` - Handles client connections and message broadcasting.
* `client.py` - Connects to the server and sends/receives messages.

---

## Example Usage

1. Start the server: `python server.py`
2. Start clients: `python client.py`
3. Clients can type messages, which will be broadcast to all connected clients.

---

## Future Enhancements

* Add **GUI** using Tkinter or PyQt.
* Implement **private messaging** between users.
* Add **encryption** for secure communication.
* Integrate **user authentication**.

---

## Author

* [Nitin Anand]
* Email: [champnitin982@gmail.com)
* SRM Institute of Science and Technology
