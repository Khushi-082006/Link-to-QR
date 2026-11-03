# Link2QR – QR Code Generator

Link2QR is a simple web application that converts a URL into a QR code. Users can enter a link, generate its QR code instantly, and download the generated image without reloading the webpage.

## Features

- Generate QR codes from URLs.
- Simple and responsive user interface.
- Generate QR codes without page reload.
- Preview the generated QR code.
- Download the QR code as a PNG image.
- Backend powered by FastAPI.

## Technologies Used

- **Python** – Backend programming
- **FastAPI** – Web framework and API endpoints
- **HTML** – Webpage structure
- **Tailwind CSS** – Styling and responsive design
- **JavaScript** – Sending requests without reloading the page
- **Jinja2** – Rendering HTML templates
- **QRCode** – Generating QR code images
- **Uvicorn** – Running the FastAPI application

## Project Structure

```text
Link2QR/
├── app.py
├── README.md
├── template/
│   └── index.html
├── static/
│   └── qrcodes/
└── venv/
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Link2QR
```

Replace `<your-repository-url>` with your GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install fastapi uvicorn jinja2 "qrcode[pil]"
```

## How to Run

Start the development server using:

```bash
python -m uvicorn app:app --reload
```

Open your browser and visit:

**http://localhost:8000**

## How to Use

1. Open Link2QR in your browser.
2. Enter the URL you want to convert into a QR code.
3. Click the **Generate QR Code** button.
4. View the generated QR code on the webpage.
5. Click **Download QR Code** to save the image.

## How It Works

1. The user enters a URL in the input field.
2. JavaScript sends the URL to the FastAPI backend using a POST request.
3. FastAPI processes the URL and generates a QR code using the Python `qrcode` library.
4. The generated image is saved in `static/qrcodes/`.
5. The backend returns the image URL to the frontend.
6. JavaScript displays the QR code without refreshing the webpage.


## Author

Developed as a Python web development project to practice backend development, API integration, and frontend-backend communication.
