AetherRide
Description
AetherRide is a simple client-server project that demonstrates how ride requests can be sent from a client to a server using Python. The server is built with Flask, while the client uses the requests library. This project serves as a basic demonstration of ride-sharing functionality, focusing on REST API interactions and modular code structure.

Features
REST API Backend: Built with Flask for handling ride requests.
Client Communication: Python client using the requests library to send JSON ride requests.
Structured Responses: Server responds with JSON data for ride status and confirmations.
Modular Structure: Separate folders for client and server for clean organization.
Demo-Focused: Lightweight implementation for educational or prototyping purposes.
Installation
Prerequisites:

Python 3.x installed.
Install required libraries: pip install flask requests.
Clone the Repository:

git clone [repository URL]
Navigate to the project directory.
Run the Server:

Go to the server folder.
Run python app.py (or equivalent script).
Run the Client:

Go to the client folder.
Run python client.py (or equivalent script) to send requests.
Usage
Start the Flask server on localhost (default port 5000).
Use the client script to send ride requests via HTTP POST.
Example: The client sends a JSON payload like {"pickup": "Location A", "destination": "Location B"} to /ride_request/.
Server processes the request and returns a JSON response with ride details.
Team
Ayush Gowda P: Full Stack Developer
Kumar K C: System Architect
Yagnesh L: Product Manager
Contributing
Fork the repository.
Create a feature branch.
Submit a pull request with changes.
