from versa_image_x import convert_image

# Test the function
png_to_jpeg_result = convert_image('sample.png', 'sample_converted.jpeg', 'JPEG')
jpeg_to_png_result = convert_image('sample.jpeg', 'sample_converted.png', 'PNG')
webp_to_png_result = convert_image('sample.webp', 'sample_converted.png', 'PNG', quality=20)
tiff_to_webp_result = convert_image('sample.tiff', 'sample_converted.webp', 'WebP', quality=20)
bmp_to_tiff_result = convert_image('sample.bmp', 'sample_converted.tiff', 'TIFF', compression='tiff_deflate')

print(f'Successfully converted PNG to JPEG: {png_to_jpeg_result}')
print(f'Successfully converted JPEG to PNG: {jpeg_to_png_result}')
print(f'Successfully converted WebP to PNG: {webp_to_png_result}')
print(f'Successfully converted TIFF to WebP: {tiff_to_webp_result}')
print(f'Successfully converted BMP to TIFF: {bmp_to_tiff_result}')
