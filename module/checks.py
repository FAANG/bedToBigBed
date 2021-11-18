import subprocess


def check_headers(bedFile):
    awk_cmd = f"awk -f awk/checkHeaders.awk {bedFile}"
    res = subprocess.run(awk_cmd, capture_output=True, text=True, shell=True)
    return res


def modify_file(bed_filepath, updateddirpath):
    awk_cmd = f"awk -v updatedpath={updateddirpath} -f awk/modify.awk {bed_filepath}"
    res = subprocess.run(awk_cmd, capture_output=True, text=True, shell=True)
    return res


def sort_file(bed_filepath):
    sort_cmd = f"sort -k1,1 -k2,2n -o {bed_filepath} {bed_filepath}"
    res = subprocess.run(sort_cmd, capture_output=True, text=True, shell=True)
    return res
