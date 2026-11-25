# Motion Detection & Intrusion Alert System

A simple Python-based **motion detection and intrusion alert system** using OpenCV and Tkinter.

The application uses your computer's webcam to monitor a room. When motion is detected, it identifies the room as **occupied**, captures screenshots, and triggers an alert.

## Features

- Real-time webcam monitoring
- Motion detection using OpenCV
- Intrusion/occupancy detection
- Automatic screenshots when motion is detected
- Email alert functionality
- Simple Tkinter-based interface
- User email configuration

## Technologies Used

- Python
- OpenCV
- Tkinter
- `datetime`
- `time`
- `os`

## Project Files

```text
├── app.py
├── alert.py
├── configure.py
├── intrusion.py
├── user.py
└── README.md
```

### 1. Set and Detect

This is the main GUI application.

It provides two options:

- **Start Tracking** – starts the webcam-based motion detection.
- **Set Target Email** – allows you to configure the email address and password used by the alert system.

### 2. Intrusion Detection

This module:

- Opens the webcam
- Detects changes/movement in the camera feed
- Identifies the room as `OCCUPIED` when significant movement is detected
- Draws a bounding box around detected movement
- Captures screenshots
- Triggers the alert after sustained motion detection

### 3. User Details

This module collects the target email credentials and stores them in `configure.py`.

## Getting Started

### Step 1: Install Python

Make sure Python is installed on your computer.

Check your installation:

```bash
python --version
```

### Step 2: Install OpenCV

Install the required OpenCV package:

```bash
pip install opencv-python
```

Tkinter is generally included with standard Python installations.

### Step 3: Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Move into the project directory:

```bash
cd <PROJECT-FOLDER>
```

### Step 4: Configure Your Email

Run:

```bash
python user.py
```

Enter the email address that should be used by the application.

The program will create/update:

```text
configure.py
```

with the email configuration.

> **Security Note:** Do not upload real email passwords or other credentials to a public GitHub repository. Use environment variables or another secure configuration method for production use.

### Step 5: Start the Application

Run:

```bash
python app.py
```

A window will open with two options:

**Start Tracking**  
Starts the webcam and begins motion detection.

**Set Target Email**  
Configures the email details used by the alert system.

## Using Motion Detection

After selecting **Start Tracking**:

1. The webcam will open.
2. The system will monitor the camera feed.
3. When significant movement is detected, the system marks the room as **OCCUPIED**.
4. Screenshots are captured during the detected intrusion.
5. An alert is triggered after the detection threshold is reached.
6. Press **ESC** to stop the camera.

## Screenshots

When motion is detected, screenshots are saved automatically in the project directory.

Example:

```text
screen1.png
screen2.png
screen3.png
...
```

## Important Notes

- Make sure your webcam is connected and accessible.
- Allow camera permissions when prompted.
- The application is intended for **educational and demonstration purposes**.
- Test the system in a controlled environment before using it for actual security monitoring.
- Do not commit passwords, API keys, or other sensitive information to GitHub.

## Possible Improvements

Some ideas for extending the project:

- Face detection and recognition
- Telegram/WhatsApp alerts
- Cloud-based image storage
- Multiple camera support
- Web-based dashboard
- Intrusion history and logs
- AI-based person detection
- Email alerts with captured images
- Remote monitoring

## Author

Developed as a Python/OpenCV cybersecurity and computer-vision project.