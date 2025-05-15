import streamlit as st
from typing import Tuple
import qrcode
from qrcode.constants import ERROR_CORRECT_L
from qrcode.exceptions import DataOverflowError
import os
from io import BytesIO

# Set page configuration
st.set_page_config(
    page_title="QR Code Generator",
    page_icon="🗺️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
        .main {
            padding: 2rem;
        }
        .stTitle {
            color: #2c3e50;
            font-size: 3rem !important;
            padding-bottom: 2rem;
        }
        .stButton>button {
            background-color: #3498db;
            color: white;
            padding: 0.5rem 2rem;
            border-radius: 5px;
            border: none;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #2980b9;
            transform: translateY(-2px);
        }
        .download-btn {
            background-color: #27ae60 !important;
        }
        .coordinate-input {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
        }
    </style>
""", unsafe_allow_html=True)

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

def create_qr_code(latitude: float, longitude: float) -> BytesIO:
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
        
        # Save image to BytesIO object
        img_bytes = BytesIO()
        img.save(img_bytes)
        img_bytes.seek(0)
        return img_bytes
    except (DataOverflowError, ValueError) as e:
        st.error(f"Error with QR code data: {str(e)}")
        return None

def main():
    # Header with icon
    st.markdown("<h1 style='text-align: center;'><span style='font-size: 3rem;'>🗺️</span><br>QR Code Generator for Maps</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666; font-size: 1.2em;'>Generate QR codes for any location on Google Maps</p>", unsafe_allow_html=True)
    
    # Add a divider
    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
    
    # Container for inputs
    with st.container():
        st.markdown("<div class='coordinate-input'>", unsafe_allow_html=True)
        st.subheader("📍 Enter Location Coordinates")
        
        # Create two columns for latitude and longitude inputs
        col1, col2 = st.columns(2)
        
        with col1:
            latitude = st.number_input(
                "Latitude",
                min_value=-90.0,
                max_value=90.0,
                value=0.0,
                format="%.6f",
                help="Enter latitude between -90 and 90",
                key="lat_input"
            )

        with col2:
            longitude = st.number_input(
                "Longitude",
                min_value=-180.0,
                max_value=180.0,
                value=0.0,
                format="%.6f",
                help="Enter longitude between -180 and 180",
                key="long_input"
            )
        st.markdown("</div>", unsafe_allow_html=True)

    # Add a generate button
    if st.button("Generate QR Code"):
        qr_bytes = create_qr_code(latitude, longitude)
        if qr_bytes:
            st.image(qr_bytes, caption="Scan this QR code to view the location on Google Maps")
            
            # Add a download button
            st.download_button(
                label="Download QR Code",
                data=qr_bytes,
                file_name=QR_OUTPUT_FILE,
                mime="image/png"
            )
            
            # Display the Google Maps link
            maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
            st.write("Direct link to location:", maps_url)

if __name__ == "__main__":
    main()
