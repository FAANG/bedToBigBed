import sys
import subprocess
import os
from module.checks import check_headers, modify_file, sort_file
from module.logging import logger
from configs.config import *

main_logger = logger(__name__)

def check_arg():
    if len(sys.argv) < 2:
        print('Please provide a directory path containing BED files')
        exit(0)
    return sys.argv[1]


def create_dir(dir_path):
    updated_dir_path = f"{dir_path}/updated"
    bigbed_dir_path = f"{dir_path}/bigbed"
    try:
        updated_exist = os.path.exists(updated_dir_path)
        bigbed_exist = os.path.exists(bigbed_dir_path)

        if not updated_exist:
            os.mkdir(updated_dir_path)

        if not bigbed_exist:
            os.mkdir(bigbed_dir_path)

        return updated_dir_path, bigbed_dir_path

    except OSError as error:
        main_logger.error(f"Error creating subdirectory {updated_dir_path} \n {error}")


def run_process(dir_path):
    try:
        (updated_dir_path, bigbed_dir_path) = create_dir(dir_path)
        for entry in os.scandir(dir_path):
            if entry.path.endswith(".bed") and entry.is_file():
                filepath = entry.path
                bed_to_bigbed(filepath, updated_dir_path, bigbed_dir_path)

    except RuntimeError as error:
        main_logger.error(f"Error with bigBed conversion {error}")


def bed_to_bigbed(filepath, updated_dir_path, bigbed_dir_path):
    try:
        filename = os.path.basename(filepath)
        modified_filepath = f"{updated_dir_path}/{filename}"
        bigbed_filepath = f"{bigbed_dir_path}/{filename.split('.')[0]}.bb"

        # file conversion to correct bed format
        header_res = check_headers(filepath)

        if header_res.returncode == 0 and int(header_res.stdout) == 1:
            modify_res = modify_file(filepath, modified_filepath)

            if modify_res.returncode != 0:
                main_logger.error(f"Error modifying file {filepath}")
            else:
                sort_res = sort_file(modified_filepath)

                if sort_res.returncode != 0:
                    main_logger.error(f"Error sorting file {filepath}")
                else:
                    # convert bed to bigbed
                    print(f"Proceeding with file conversion from bed to bigbed - {filename}.")
                    cmd = f"./bedToBigBed -as={AUTOSQL_FILE} -type=bed6+1 {modified_filepath} " \
                          f"{CHROMSIZES} {bigbed_filepath}"

                    conversion = subprocess.run(
                        cmd, capture_output=True, text=True, shell=True)

                    if conversion.returncode == 0:
                        print(f"File conversion from bed to bigbed has been successful - {filename}")
                    else:
                        main_logger.error(f"Error converting file {modified_filepath} to bigBed format")

        else:
            main_logger.error(f"Incorrect headers in file {filename}")

    except RuntimeError as error:
        main_logger.error(f"Error with bigBed conversion {error}")


if __name__ == '__main__':
    dir_path = check_arg()
    run_process(dir_path)
