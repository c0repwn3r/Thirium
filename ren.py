import os

directory_to_check = "/home/core/thirium/" # Which directory do you want to start with?

def my_function(directory):
    print("Renaming: " + directory)
    os.system('rename -v "thirium" thirium *')

def frn_pass():
    # Get all the subdirectories of directory_to_check recursively and store them in a list:
    directories = [os.path.abspath(x[0]) for x in os.walk(directory_to_check)]
    directories.remove(os.path.abspath(directory_to_check)) # If you don't want your main directory included
    for i in directories:
        os.chdir(i)         # Change working Directory
        my_function(i)      # Run your function

print("Thirium - Rename tool v1.1")
print("Status: Prepping")
# no prep to be done
print("Status: File content subsitution")
print("FCS rst rs1 nstart")
print("[1/7] (1) FCS -fRWE Thirium->Thirium")
os.system("find ./ -type f -readable -writable -exec sed -i \"s/Thirium/Thirium/g\" {} \\;")
print("[2/7] (1) FCS -fRWE ThirIum->ThirIum")
os.system("find ./ -type f -readable -writable -exec sed -i \"s/ThirIum/ThirIum/g\" {} \\;")
print("[3/7] (1) FCS -fRWE THI->THI")
os.system("find ./ -type f -readable -writable -exec sed -i \"s/THI/THI/g\" {} \\;")
print("[4/7] (1) FCS -fRWE thirium->thirium")
os.system("find ./ -type f -readable -writable -exec sed -i \"s/thirium/thirium/g\" {} \\;")
print("[5/7] (1) FCS -fRWE thiriumd->thiriumd")
os.system("find ./ -type f -readable -writable -exec sed -i \"s/thiriumd/thiriumd/g\" {} \\;")
print("FCS rs1 completed, rs2 nstart")
print("[6/7] (2) FCS -fRWE thiries->thiries")
os.system("find ./ -type f -readable -writable -exec sed -i \"s/thiries/thiries/g\" {} \\;")
print("[7/7] (2) FCS -fRWE thires->thires")
os.system("find ./ -type f -readable -writable -exec sed -i \"s/thires/thires/g\" {} \\;")
print("FCS rs2 completed, rst nend")
print("Status: File renaming")
print("FRN rst rs1 nstart")
print("Pass 1")
try:
    frn_pass()
except:
    print("Pass 1 met prerenamed file")
print("FRN rs1 completed, rs2 nstart")
try:
    frn_pass()
except:
    print("Pass 2 met prerenamed file")
print("FRN rs2 completed, rs3 nstart")
try:
    frn_pass()
except:
    print("Pass 3 met prerenamed file")
print("FRN rs3 completed, rs4 nstart")
try:
    frn_pass()
except:
    print("Pass 4 met prerenamed file")
print("FRN done")
