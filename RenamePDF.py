import os
from pdfrw import PdfReader

import argparse

parser = argparse.ArgumentParser(description='Path for folder to change all PDF inside')
parser.add_argument("--path")

args = parser.parse_args()
path = args.path
print("Change all PDF names inside {}".format(path))
def renameFileToPDFTitle(path, fileName):
    fullName = os.path.join(path, fileName)
    # Extract pdf title from pdf file
    newName = PdfReader(fullName).Info.Title
    if newName is not None:
        # Remove surrounding brackets that some pdf titles have
        newName = newName.strip('()') + '.pdf'
        newFullName = os.path.join(path, newName)
        try:
            os.rename(fullName, newFullName)
        except Exception as e:
            print("File name too long = {}".format(fullName))
            pass
for fileName in os.listdir(path):
    # Rename only pdf files
    fullName = os.path.join(path, fileName)
    if (not os.path.isfile(fullName) or fileName[-4:] != '.pdf'):
        continue
    renameFileToPDFTitle(path, fileName)
