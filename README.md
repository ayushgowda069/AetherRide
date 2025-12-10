# AetherRide

**AetherRide** is a next-generation ride-sharing platform designed to revolutionize urban mobility. It connects passengers with drivers in real-time, offering a seamless, fast, and reliable experience powered by advanced technology.

## Features

*   **Real-time Ride Booking**: Users can easily request rides by specifying pickup and drop-off locations.
*   **Intelligent Driver Matching**: Efficient assignment of available drivers to ride requests.
*   **Live Status Updates**: Real-time tracking of ride status (Pending, Accepted, Completed).
*   **Warp Pass (Priority Upgrade)**: Premium option for users to get priority matching.
*   **Driver Dashboard**: Dedicated interface for drivers to view and accept assigned rides.
*   **Admin Dashboard**: Tools for monitoring platform activity and managing resources.

## Technology Stack

*   **Backend**: FastAPI (Python)
*   **Database**: PostgreSQL
*   **Frontend**: HTML, CSS, JavaScript
*   **Deployment**: Localhost (Development), Render/Railway (Production ready)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd AETHER_RIDE
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the database:**
    Ensure you have PostgreSQL installed and running. Update the database connection string in `database.py` if necessary.
    ```bash
    # Run database initialization scripts (if any)
    python reset_db.py
    ```


## Distributed Cluster Launch (New Feature)

To simulate a real-world distributed environment with multiple nodes, use the cluster launcher script. This will spawn multiple server instances for users, drivers, and an admin node.

1.  **Run the Cluster Script:**
    ```bash
    python run_cluster.py
    ```

2.  **Cluster Configuration:**
    *   **Admin Node**: Port `6001`
    *   **Driver Nodes**: Ports `7000` - `7007`
    *   **User Nodes**: Ports `8000` - `8007`

3.  **Access the Gateway:**
    The script will automatically open the **Gateway** (`AETHER_RIDE/static/gateway.html`) in your default browser. This gateway allows you to easily navigate between the different nodes.



## Project Structure

*   `main.py`: Entry point of the FastAPI application.
*   `models.py`: SQLAlchemy database models.
*   `schemas.py`: Pydantic schemas for data validation.
*   `database.py`: Database connection and session management.
*   `static/`: Contains frontend HTML, CSS, and JS files.
*   `AetherRide_Project_Report.md`: Comprehensive project report and documentation.

## Team Members

*   **Full Stack Developer**: Ayush Gowda P
*   **System Architect**: Kumar K C
*   **Product Manager**: Yagnesh L

## License

[MIT License](LICENSE.md) - See the LICENSE.md file for details.
