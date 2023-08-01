import sys
import subprocess

checksum_type = sys.argv[1]
filename = sys.argv[2]
correct_checksum = sys.argv[3]


def sha256(filename):
    checksum = f"sha256sum {filename}"
    res = subprocess.getoutput(checksum)
    return res.split(" ")[0]


def sha1(filename):
    checksum = f"sha1sum {filename}"
    res = subprocess.getoutput(checksum)
    return res.split(" ")[0]


def md5(filename):
    checksum = f"md5sum {filename}"
    res = subprocess.getoutput(checksum)
    return res.split(" ")[0]


def calculate():
    if (checksum_type == "sha256"):
        calculated_checksum = sha256(filename)
    elif (checksum_type == "sha1"):
        calculated_checksum = sha1(filename)
    elif (checksum_type == "md5"):
        calculated_checksum = md5(filename)

    if (correct_checksum == calculated_checksum):
        print("CheckSum Matched")
    else:
        print("CheckSum Not Matching")


calculate()
