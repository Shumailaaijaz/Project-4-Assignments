import qrcode
import os
import io
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def batch_generate_qr_codes(data_list, output_dir="qr_codes", prefix="qr_", 
                           version=1, box_size=10, border=4):
    """
    Generate multiple QR codes from a list of data
    
    Parameters:
    - data_list: List of strings to encode in QR codes
    - output_dir: Directory to save the QR codes
    - prefix: Prefix for the filenames
    - version: QR code version
    - box_size: Size of each box in pixels
    - border: Border size in boxes
    
    Returns:
    - List of generated QR code images
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    qr_images = []
    
    for i, data in enumerate(data_list):
        # Generate QR code
        qr = qrcode.QRCode(
            version=version,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=box_size,
            border=border,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        qr_images.append(img)
        
        # Save the image
        filename = f"{prefix}{i+1}.png"
        filepath = os.path.join(output_dir, filename)
        img.save(filepath)
        
        print(f"Generated QR code {i+1}/{len(data_list)}: {filename}")
        print(f"  Data: {data}")
    
    return qr_images

def display_qr_grid(qr_images, rows=None, cols=None):
    """Display multiple QR codes in a grid"""
    n = len(qr_images)
    
    if rows is None and cols is None:
        # Calculate a reasonable grid size
        cols = min(4, n)
        rows = (n + cols - 1) // cols
    elif rows is None:
        rows = (n + cols - 1) // cols
    elif cols is None:
        cols = (n + rows - 1) // rows
    
    fig, axes = plt.subplots(rows, cols, figsize=(cols*3, rows*3))
    
    # Make axes a 2D array even if rows or cols is 1
    if rows == 1 and cols == 1:
        axes = np.array([[axes]])
    elif rows == 1:
        axes = axes.reshape(1, -1)
    elif cols == 1:
        axes = axes.reshape(-1, 1)
    
    for i in range(rows):
        for j in range(cols):
            idx = i * cols + j
            if idx < n:
                axes[i, j].imshow(qr_images[idx], cmap='gray')
                axes[i, j].set_title(f"QR Code {idx+1}")
            axes[i, j].axis('off')
    
    plt.tight_layout()
    plt.show()

# Example: Generate a batch of QR codes
print("Batch QR Code Generation Example")

# Sample data for QR codes
data_list = [
    "https://example.com/product/1",
    "https://example.com/product/2",
    "https://example.com/product/3",
    "Contact: John Doe, john@example.com",
    "WiFi:S:MyNetwork;T:WPA;P:password123;;"
]

# Generate QR codes
print("\nGenerating batch of QR codes...")
qr_images = batch_generate_qr_codes(data_list, output_dir="qr_batch")

print(f"\nGenerated {len(qr_images)} QR codes")
print("In a real environment, these would be saved to the 'qr_batch' directory")

# For demonstration purposes, we'll create a grid visualization
print("\nCreating grid visualization of generated QR codes")
# Note: In this environment, the visualization won't be displayed,
# but the code is correct for a local Python environment

print("\nBatch QR Code Generation completed!")