from PIL import Image

def convert_image(source_path, destination_path, output_format, **kwargs):
    """
    Convert an image from one format to another.

    Parameters:
        source_path (str): The source file path for the image to be converted.
        destination_path (str): The destination file path for the converted image.
        output_format (str): The format to convert the image to. E.g., 'JPEG', 'PNG', etc.
        **kwargs: Additional keyword arguments for image conversion like quality, compression, etc.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with Image.open(source_path) as img:
            # Convert 'P' mode to 'RGB' if converting to JPEG
            if img.mode == 'P' and output_format == 'JPEG':
                img = img.convert('RGB')
            
            img.save(destination_path, output_format, **kwargs)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
