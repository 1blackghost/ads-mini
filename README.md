# Social Distancing Detection using Face Recognition

This project aims to detect social distancing violations using face recognition techniques. It utilizes face detection and recognition algorithms to identify individuals in an image and calculates the distances between them to determine if social distancing guidelines are being followed.

## Setup Instructions

### Prerequisites
- Python (3.6 or higher)
- Django web framework
- face_recognition library
- Additional Python packages (requirements.txt provided)

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/social-distancing-face-recognition.git
    ```

2. Navigate to the project directory:

    ```bash
    cd social-distancing-face-recognition
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the Django server:

    ```bash
    python manage.py runserver
    ```

2. Access the application in your web browser at `http://localhost:8000`.

3. Upload an image containing individuals to analyze social distancing compliance.

4. The application will detect faces in the image and determine if social distancing guidelines are being followed.

### Configuration

- Adjust the `DISTANCE_THRESHOLD` constant in `settings.py` to customize the minimum distance considered safe for social distancing.

## Contributing

Contributions are welcome! Please open an issue or pull request if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the [MIT License](LICENSE).
