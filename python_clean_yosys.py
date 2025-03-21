import json
import os
import re
import time
import shutil


def vlg_clean(file):
    file_tmp = file + ".tmp"
    shutil.copy(file, file_tmp)  # Use shutil for Windows compatibility
    os.remove(file)  # Remove original file

    with open(file_tmp, "r") as f:
        lines = f.readlines()
        with open(file, "a+") as f_tmp:
            for line in lines:
                # Remove attributes (* ... *)
                line = re.sub(r'\(\*(.*)\*\)', '', line)
                if line.strip():  # Remove empty lines
                    f_tmp.writelines(line)

    os.remove(file_tmp)  # Delete temporary file


if __name__ == '__main__':
    design_name = "mriscvcore"  # Change to your design
    cmd = 'sog'  # Process SOG-form Verilog file
    file_dir = f"./masterriscv_sog.v"  # Correct path to the output of yosys

    vlg_clean(file_dir)  # Run the cleanup function
    print('File Cleaning Completed')
