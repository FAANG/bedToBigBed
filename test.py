import sys
import subprocess
from module.checks import check_headers, modify_file


def run_process():
    print("Proceeding with file conversion from bed to bigbed.")

    cmd = './bedToBigBed -as=files/autosql/cage.as -type=bed6+1 files/sorted/CAGE_original.bed files/chrom_sizes/GCF_002742125.1_Oar_rambouillet_v1.0.chrom.sizes files/bigbed/koosum.bb'

    conversion = subprocess.run(
      cmd,
        capture_output=True, text=True, shell=True)

    if conversion.returncode == 0:
        print("File conversion from bed to bigbed has been successful")
    else:
        print(f"{conversion.stderr} + {conversion.returncode}")


if __name__ == '__main__':
    run_process()
