import qrcode
from PIL import Image
import io
import numpy as np
import matplotlib.pyplot as plt

def generate_qr_with_logo(data, logo_path=None, logo_size_ratio=0.2):
    """
    Generate a QR code with a logo in the center
    
    Parameters:
    - data: The data to encode in the QR code
    - logo_path: Path to the logo image file
    - logo_size_ratio: Size of the logo relative to the QR code (0.0-1.0)
    
    Returns:
    - PIL Image object containing the QR code with logo
    """
    # Generate QR code with high error correction
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')
    
    # If no logo is provided, return the QR code as is
    if logo_path is None:
        return qr_img
    
    # Open the logo image
    try:
        logo = Image.open(logo_path).convert('RGBA')
    except Exception as e:
        print(f"Error opening logo: {e}")
        return qr_img
    
    # Calculate logo size
    qr_width, qr_height = qr_img.size
    logo_max_size = int(min(qr_width, qr_height) * logo_size_ratio)
    
    # Resize logo while maintaining aspect ratio
    logo_width, logo_height = logo.size
    aspect_ratio = logo_width / logo_height
    
    if logo_width > logo_height:
        new_width = logo_max_size
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = logo_max_size
        new_width = int(new_height * aspect_ratio)
    
    logo = logo.resize((new_width, new_height), Image.LANCZOS)
    
    # Calculate position to place the logo (center)
    pos_x = (qr_width - new_width) // 2
    pos_y = (qr_height - new_height) // 2
    
    # Create a new image for the result
    result = Image.new('RGBA', (qr_width, qr_height), (0, 0, 0, 0))
    
    # Paste the QR code first
    result.paste(qr_img, (0, 0))
    
    # Paste the logo on top
    result.paste(logo, (pos_x, pos_y), logo)
    
    return result

# For this example, we'll create a simple placeholder logo
def create_placeholder_logo():
    """Create a simple placeholder logo"""
    logo = Image.new('RGBA', (100, 100), (255, 255, 255, 0))
    # Draw a blue circle
    for x in range(100):
        for y in range(100):
            # Calculate distance from center
            distance = np.sqrt((x - 50)**2 + (y - 50)**2)
            if distance < 40:  # Circle with radius 40
                logo.putpixel((x, y), (0, 0, 255, 255))  # Blue
    
    # Save the logo to a BytesIO object
    logo_io = io.BytesIO()
    logo.save(logo_io, format='PNG')
    logo_io.seek(0)
    
    # Save to a temporary file
    logo_path = "temp_logo.png"
    with open(logo_path, 'wb') as f:
        f.write(logo_io.getvalue())
    
    return logo_path

# Example: Generate QR code with logo
print("Generating QR code with embedded logo")
data = "https://www.example.com/qr-with-logo"

# Create a placeholder logo
logo_path = create_placeholder_logo()

# Generate QR code with logo
qr_with_logo = generate_qr_with_logo(data, logo_path, logo_size_ratio=0.25)

# Display information
print(f"QR code with logo generated for data: {data}")
print(f"QR code size: {qr_with_logo.size[0]}x{qr_with_logo.size[1]} pixels")
print("The logo is embedded in the center of the QR code")
print("Note: Using high error correction allows the QR code to be readable even with the logo")

# Convert to a format we can display in the output
img_byte_arr = io.BytesIO()
qr_with_logo.save(img_byte_arr, format='PNG')
img_byte_arr = img_byte_arr.getvalue()

print("\nQR Code with Logo demonstration completed!")