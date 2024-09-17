# Music-RecSys-with-gRPC-and-Flask
This project is made within the lab of micro-servive architecture and programming course. It is hands on implementation for gRPC.

This project is a CRUD music recommendation service built using gRPC for handling service logic and Flask for the web interface. The goal was to learn how to set up gRPC for a real-world application while making it easy to interact with through a web browser.

**Why gRPC?**
gRPC is awesome! It's like communication between services, making them fast and super reliable. gRPC uses protobuf to serialize data efficiently. This means:

It is faster than JSON or XML.
It can be used gRPC across Python, Java, Go etc.
Just define your service once, and gRPC generates the client and server code for you

## Project Overview
**gRPC Server**: Handles all the heavy lifting for creating, reading, updating, and deleting music recommendations.
**Flask Web Interface**: Lets you interact with the gRPC service using a user-friendly web page.
**Client**: A command-line interface to directly test out gRPC functionality.

### Quick start guide
Clone the repo and move to that directory.
```bash
pip install grpcio grpcio-tools Flask

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. greet.proto

python server.py

python app.py
```
visit http://localhost:5000 in your browser to start the service

