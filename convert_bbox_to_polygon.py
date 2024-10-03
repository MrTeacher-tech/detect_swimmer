import os

def bbox_to_polygon(class_id, x_center, y_center, width, height):
    # Convert center-based format to corner coordinates
    half_width = width / 2
    half_height = height / 2
    
    # Calculate the four corners of the square
    x1 = x_center - half_width  # Top-left x
    y1 = y_center - half_height  # Top-left y
    x2 = x_center + half_width  # Top-right x
    y2 = y_center - half_height  # Top-right y
    x3 = x_center + half_width  # Bottom-right x
    y3 = y_center + half_height  # Bottom-right y
    x4 = x_center - half_width  # Bottom-left x
    y4 = y_center + half_height  # Bottom-left y
    
    # Create the polygon in YOLO format (class_id followed by normalized coordinates)
    polygon = [class_id, x1, y1, x2, y2, x3, y3, x4, y4]
    
    return polygon

def convert_bbox_to_polygon_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                # Split the line into components
                components = line.strip().split()
                
                # Parse the components (class_id, x_center, y_center, width, height)
                class_id = int(components[0])
                x_center = float(components[1])
                y_center = float(components[2])
                width = float(components[3])
                height = float(components[4])
                
                # Convert bounding box to polygon
                polygon = bbox_to_polygon(class_id, x_center, y_center, width, height)
                
                # Write the converted polygon to the output file
                outfile.write(' '.join(map(str, polygon)) + '\n')

    except:
        print("except:", input_file)

def process_folder(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)
        
        # Ensure we are processing only files (not directories)
        if os.path.isfile(input_file_path):
            output_file_path = os.path.join(output_folder, filename)
            
            # Convert the bounding boxes in the file to polygons
            convert_bbox_to_polygon_file(input_file_path, output_file_path)
            print(f"Processed file: {filename}")



'''
# Example usage
input_file = './data/labels/train/image_068.txt'  # Replace with your actual input file path
output_file = 'output.txt'  # Replace with your actual output file path

convert_bbox_to_polygon_file(input_file, output_file)
'''

input_folder = './data/labels/val_bboxes'

output_folder = './data/labels/new_val'

process_folder(input_folder, output_folder)