import os
import xml.etree.ElementTree as ET

def convert_to_yolo_format(xml_file, class_id=0):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Get image size
    size = root.find('size')
    img_width = int(size.find('width').text)
    img_height = int(size.find('height').text)

    # Get object information
    objects = root.findall('object')
    yolo_annotations = []

    for obj in objects:
        # Get bounding box coordinates
        bndbox = obj.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)

        # Convert to YOLO format (normalize the coordinates)
        x_center = (xmin + xmax) / 2.0 / img_width
        y_center = (ymin + ymax) / 2.0 / img_height
        bbox_width = (xmax - xmin) / img_width
        bbox_height = (ymax - ymin) / img_height

        # Format: <class_id> <x_center> <y_center> <width> <height>
        yolo_annotation = f"{class_id} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}"
        yolo_annotations.append(yolo_annotation)

    return yolo_annotations

def process_multiple_xml_files(input_dir, output_dir, class_id=0):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for xml_file in os.listdir(input_dir):
        if xml_file.endswith('.xml'):
            xml_file_path = os.path.join(input_dir, xml_file)
            yolo_annotations = convert_to_yolo_format(xml_file_path, class_id)

            # Save the annotations to a YOLO file (same name as the image file but with .txt extension)
            output_txt_path = os.path.join(output_dir, xml_file.replace('.xml', '.txt'))
            with open(output_txt_path, 'w') as f:
                f.write("\n".join(yolo_annotations))

            print(f"Annotations saved to {output_txt_path}")
# Example usage with WSL-style paths
input_directory = '/mnt/c/Users/hardi/Downloads/license_plate_dataset_kaggle/train/labels_xml'
output_directory = '/mnt/c/Users/hardi/Downloads/license_plate_dataset_kaggle/train/labels'


process_multiple_xml_files(input_directory, output_directory, class_id=0)  # assuming 'LP' is class 0
