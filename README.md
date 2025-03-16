# QR Code Generator for Google Maps Location

A simple Python application that generates QR codes for Google Maps locations based on latitude and longitude coordinates.

## Features

- Generate QR codes for any location using latitude and longitude coordinates
- Input validation for coordinates (latitude: -90 to 90, longitude: -180 to 180)
- Custom save location support
- Error handling for invalid inputs and file operations
- Creates save directory automatically if it doesn't exist

## Requirements

- Python 3.x
- Required packages:
  - qrcode
  - pillow

## Installation

1. Clone this repository or download the source code
2. Install the required packages using pip:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Follow the prompts:
   - Enter a directory path to save the QR code (or press Enter to use the current directory)
   - Enter the latitude (e.g., 34.1232255)
   - Enter the longitude (e.g., 74.1240809)

3. The QR code will be generated and saved as 'my_location_qr.png' in the specified directory

## QR Code Configuration

The QR code generation can be customized by modifying the following constants in `main.py`:

- `QR_VERSION`: QR code version (default: 1)
- `QR_BOX_SIZE`: Size of each box in pixels (default: 10)
- `QR_BORDER`: Border size in boxes (default: 4)
- `QR_OUTPUT_FILE`: Output filename (default: "my_location_qr.png")

## Error Handling

The application includes error handling for:
- Invalid coordinate inputs
- Directory creation errors
- File save errors
- QR code generation errors

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open issues and submit pull requests to improve the application.