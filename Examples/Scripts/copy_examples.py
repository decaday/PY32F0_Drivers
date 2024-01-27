import os
import shutil


def get_example(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    # Traverse the files in the folder and copy the PDF files to a new folder
    for file in os.listdir(input_folder):
        # Check if it is a PDF file, skip non-PDF files
        file_path = os.path.join(input_folder, file)
        if not (file_path.endswith(".pdf") or file_path.endswith(".PDF")):
            continue

        # Copy the PDF file to a new subfolder
        new_file_path = os.path.join(output_folder, file)
        shutil.copy(file_path, new_file_path)

    # Traverse the folders in the subfolder, there may be SPI, etc.
    for folder in os.listdir(input_folder):
        # Check if it is a folder, skip non-folders
        folder_path = os.path.join(input_folder, folder)
        if not os.path.isdir(folder_path):
            continue
        output_path = os.path.join(output_folder, folder)

        # Traverse the folders in the subfolder, there may be SPI_TwoBoards_FullDuplexMaster_Polling_Init, etc.
        for subfolder in os.listdir(folder_path):
            # Check if it is a folder, skip non-folders
            subfolder_path = os.path.join(folder_path, subfolder)
            if not os.path.isdir(subfolder_path):
                continue
            sub_output_path = os.path.join(output_path, subfolder)
            get_files(subfolder_path, sub_output_path)


def get_files(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    # Traverse all files and folders in the subfolder, copy the files ending with .c and .h and readme files to a new
    # subfolder, except for folders starting with system_
    for root, dirs, files in os.walk(input_folder):

        # Traverse files, check if they are .c or .h or readme files, and copy them if they are
        for file in files:
            if (file.endswith(".c") or file.endswith(".h") or file == "readme.txt") and not (file.startswith("system_")):
                file_path = os.path.join(root, file)
                new_file_path = os.path.join(output_folder, file)
                shutil.copy(file_path, new_file_path)


# Define the run function, the parameters are input_file and input_folder
def run(input_folder):
    # Check if the input folder exists, if not, throw an exception
    if not os.path.isdir(input_folder):
        raise NotADirectoryError(f"No such directory: {input_folder}")
    # Extract the part ending with -STK from the folder path, assuming it is the part after the last backslash
    folder_name = input_folder.split("\\")[-1]
    if not folder_name.endswith("-STK"):
        raise ValueError(f"Invalid folder name: {folder_name}")
    # Extract the PY32F002B part from the folder name, assuming it is the part before -STK
    mcu_name = folder_name[:-4]

    output_folder_root = os.path.join("", mcu_name)
    os.makedirs(output_folder_root, exist_ok=True)

    # Traverse each subfolder in the input folder
    for subfolder in os.listdir(input_folder):
        # Concatenate the full path of the subfolder
        subfolder_path = os.path.join(input_folder, subfolder)
        # Check if it is a folder, if not, skip it
        if not os.path.isdir(subfolder_path):
            continue
        # Concatenate the full path of the output folder, assuming it is the root directory plus the subfolder name
        output_folder = os.path.join(output_folder_root, subfolder)
        # Call the get_example function, pass in the subfolder and output folder as parameters
        get_example(subfolder_path, output_folder)
    # Return the extracted mcu name
    return mcu_name


# Call the run function, pass in your input file and input folder
run(r"E:\Projects\41-py32f0-template\Libraries\PY32F0_Drivers\Temp\PY32F030-STK")
