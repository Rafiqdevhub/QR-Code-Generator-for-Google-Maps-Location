from typing import Tuple
import qrcode
from qrcode.constants import ERROR_CORRECT_L
from qrcode.exceptions import DataOverflowError
import os

# Constants for QR code configuration
QR_VERSION: int = 1
QR_BOX_SIZE: int = 10
QR_BORDER: int = 4
QR_OUTPUT_FILE: str = "my_location_qr.png"

def get_save_path() -> str:
    while True:
        save_dir = input("Enter the directory path to save the QR code (or press Enter for current directory): ").strip()
        
        if save_dir.lower() == 'e':
            print("Exiting the application...")
            exit()
            
        if not save_dir:
            return QR_OUTPUT_FILE
        
        try:
            # Create directory if it doesn't exist
            os.makedirs(save_dir, exist_ok=True)
            return os.path.join(save_dir, QR_OUTPUT_FILE)
        except (OSError, IOError) as e:
            print(f"Error creating directory: {str(e)}")
            print("Please enter a valid directory path.")

def get_coordinates() -> Tuple[float, float]:
    while True:
        try:
            latitude = float(input("Enter latitude (e.g., 34.1232255): "))
            longitude = float(input("Enter longitude (e.g., 74.1240809): "))
            if -90 <= latitude <= 90 and -180 <= longitude <= 180:
                return (latitude, longitude)
            else:
                print("Invalid coordinates! Latitude must be between -90 and 90, longitude between -180 and 180.")
        except ValueError:
            print("Please enter valid numbers for coordinates.")

def create_qr_code(coordinates: Tuple[float, float], output_file: str = QR_OUTPUT_FILE) -> None:
    latitude, longitude = coordinates
    maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"

    try:
        qr = qrcode.QRCode(
            version=QR_VERSION,
            error_correction=ERROR_CORRECT_L,
            box_size=QR_BOX_SIZE,
            border=QR_BORDER,
        )
        qr.add_data(maps_url)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")
        with open(output_file, "wb") as f:
            img.save(f)
        print(f"QR Code generated and saved as '{output_file}'")
    except (DataOverflowError, ValueError) as e:
        print(f"Error with QR code data: {str(e)}")
    except (IOError, OSError) as e:
        print(f"Error saving QR code file: {str(e)}")

if __name__ == "__main__":
    print("Welcome to QR Code Generator for Google Maps Location!")
    save_path = get_save_path()
    coordinates = get_coordinates()
    create_qr_code(coordinates, save_path)
