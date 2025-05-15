# QR Code Generator for Google Maps Location

A modern web application built with Streamlit that generates QR codes for Google Maps locations based on latitude and longitude coordinates. Share locations easily by generating scannable QR codes that open directly in Google Maps.

## Features

- Modern, responsive web interface
- Real-time QR code generation
- Input validation for coordinates (latitude: -90 to 90, longitude: -180 to 180)
- One-click download of generated QR codes
- Direct link to view location on Google Maps
- Dark/Light mode support
- Mobile-friendly design
- Error handling with visual feedback

## Requirements

- Python 3.x
- Required packages:
  - streamlit
  - qrcode
  - pillow

## Installation

1. Clone this repository or download the source code
2. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit web application:

```bash
streamlit run main.py
```

2. Using the application:
   - Enter latitude (e.g., 34.1232255) using the number input field
   - Enter longitude (e.g., 74.1240809) using the number input field
   - Click the "Generate QR Code" button
   - The QR code will be displayed instantly
   - Use the "Download QR Code" button to save the image
   - Click "View on Google Maps" to open the location directly

## Features in Detail

### User Interface

- Clean, modern web interface built with Streamlit
- Responsive design that works on desktop and mobile
- Interactive number input fields with validation
- Real-time feedback and error messages
- Smooth animations and transitions
- Professional styling with consistent design elements

### QR Code Generation

- Instant QR code generation with live preview
- Configurable QR code parameters:
  - `QR_VERSION`: QR code version (default: 1)
  - `QR_BOX_SIZE`: Size of each box in pixels (default: 10)
  - `QR_BORDER`: Border size in boxes (default: 4)
  - High-quality PNG output

### Location Handling

- Real-time coordinate validation
- Support for precise decimal coordinates
- Direct Google Maps integration
- Easy-to-copy coordinate display
- Visual coordinate representation

### Error Handling and Validation

- Input validation with visual feedback
- Error messages for invalid coordinates
- QR code generation error handling
- Network error handling
- User-friendly error messages

## Development

### Tech Stack

- Python 3.x
- Streamlit for web interface
- QRCode library for QR generation
- Custom CSS for styling
- Responsive design principles

### Future Enhancements

- Map preview integration
- Batch QR code generation
- Custom QR code styling
- Location search functionality
- History of generated QR codes
- Export in multiple formats

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Here's how you can help:

- Report bugs and suggest features
- Submit pull requests
- Improve documentation
- Share your ideas and feedback

## Support

If you find this project useful, please consider:

- Starring the repository
- Sharing it with others
- Contributing to its improvement
