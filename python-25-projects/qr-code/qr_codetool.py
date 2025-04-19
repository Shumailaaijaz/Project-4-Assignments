import qrcode
from PIL import Image
import io
import base64
from pyzbar.pyzbar import decode
import numpy as np
import matplotlib.pyplot as plt

def generate_qr_code(data, version=1, box_size=10, border=4, fill_color="black", back_color="white"):
    """
    Generate a QR code with the given data and options
    
    Parameters:
    - data: The data to encode in the QR code
    - version: QR code version (1-40, controls size)
    - box_size: Size of each box in pixels
    - border: Border size in boxes
    - fill_color: Color of the QR code
    - back_color: Background color
    
    Returns:
    - PIL Image object containing the QR code
    """
    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img

def decode_qr_code(image):
    """
    Decode QR code from an image
    
    Parameters:
    - image: PIL Image object or path to image file
    
    Returns:
    - List of decoded data
    """
    if isinstance(image, str):
        image = Image.open(image)
    
    # Convert PIL image to numpy array - this is the key fix
    image_np = np.array(image)
    
    # Ensure the image is in the right format for pyzbar
    if len(image_np.shape) == 2:
        # Already grayscale
        pass
    elif len(image_np.shape) == 3:
        if image_np.shape[2] == 3:
            # Convert RGB to grayscale
            image_np = np.mean(image_np, axis=2).astype(np.uint8)
        elif image_np.shape[2] == 4:
            # Convert RGBA to grayscale, ignoring alpha
            image_np = np.mean(image_np[:, :, :3], axis=2).astype(np.uint8)
    
    decoded_objects = decode(image_np)
    results = []
    
    for obj in decoded_objects:
        results.append({
            'data': obj.data.decode('utf-8'),
            'type': obj.type,
            'rect': obj.rect
        })
    
    return results

def display_qr_code(image):
    """Display a QR code using matplotlib"""
    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# Example 1: Generate a basic QR code
print("Example 1: Generating a basic QR code")
data = "https://www.example.com"
qr_img = generate_qr_code(data)

# Convert to a format we can display in the output
img_byte_arr = io.BytesIO()
qr_img.save(img_byte_arr, format='PNG')
img_byte_arr = img_byte_arr.getvalue()
print(f"QR code generated with data: {data}")
print(f"QR code size: {qr_img.size[0]}x{qr_img.size[1]} pixels")

# Example 2: Generate a QR code with custom options
print("\nExample 2: Generating a QR code with custom options")
data = "Hello, QR Code with custom options!"
qr_img_custom = generate_qr_code(
    data,
    version=5,
    box_size=5,
    border=2,
    fill_color="blue",
    back_color="yellow"
)
print(f"Custom QR code generated with data: {data}")
print(f"Custom QR code size: {qr_img_custom.size[0]}x{qr_img_custom.size[1]} pixels")

# Example 3: Encode more complex data
print("\nExample 3: Encoding more complex data")
complex_data = {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+1234567890",
    "website": "https://www.example.com"
}
import json
complex_data_str = json.dumps(complex_data)
qr_img_complex = generate_qr_code(complex_data_str)
print(f"Complex data encoded: {complex_data_str}")

# Example 4: Decode a QR code
print("\nExample 4: Decoding a QR code")
# We'll decode the QR code we just created
decoded_data = decode_qr_code(qr_img)
print(f"Decoded data: {decoded_data}")

# Example 5: Generate a QR code with error correction
print("\nExample 5: QR code with error correction")
data = "This QR code has high error correction"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)
qr_img_error = qr.make_image(fill_color="black", back_color="white")
print(f"QR code with high error correction generated")
print("This QR code can be read even if up to 30% is damaged")

print("\nQR Code Generator and Decoder demonstration completed!")