""" Build index from directory listing
Inspired by: https://stackoverflow.com/questions/39048654/how-to-enable-directory-indexing-on-github-pages

usage: python3 createStaticDirectoryListing.py [-h] [--indexPage INDEXPAGE] directory
"""

DEFAULT_TEMPLATE = {
    "outputFileName": "index.md",
    "icons": {
        "DIR": "📁",#":file_folder:",
        "FILE": "🗒", #":spiral_notepad:",
        "UP": "⤴", #":arrow_heading_up:"
    },
    "excludedFiles": ["index.md", "_config.yml", "_layouts", "README.md"],
    "template": r"""
# Index of ${path}
Files in this directory:
%for displayName, fileName, type in files:
- ${icons[type]} [${displayName}](${fileName})
% endfor
"""
}

import os, argparse
from mako.template import Template

def createDirectoryListing(baseDirectory, template, indexPage = None, subDirectory = ""):
    if baseDirectory.endswith("/"):
        baseDirectory = baseDirectory[:-1]

    thisDirectory = baseDirectory + "/" + subDirectory

    files = []

    if subDirectory:
        files.append((
            "Parent Directory",
            "../",
            "UP"
        ))

    for fileName in sorted(os.listdir(thisDirectory)):
        if fileName in template["excludedFiles"]:
            continue

        fileIsDir = os.path.isdir(thisDirectory + "/" + fileName)
        fileType = "DIR" if fileIsDir else "FILE"
        fileDisplayName = fileName + "/" if fileIsDir else fileName

        files.append((fileDisplayName, fileName, fileType))

        if fileIsDir:
            createDirectoryListing(baseDirectory, template, indexPage, subDirectory + "/" + fileName)

    displayPath = "/" if not subDirectory else subDirectory

    fileContents = Template(template["template"]).render(files=files, path=displayPath, icons=template["icons"])

    if not subDirectory and indexPage:
        with open(indexPage, "r") as indexPageFile:
            fileContents = indexPageFile.read() + fileContents
    
    with open(thisDirectory + "/" + template["outputFileName"], "w+") as file:
        file.write(fileContents)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    parser.add_argument("--indexPage", required=False, help="Provide a file which will be placed on the index page.")
    args = parser.parse_args()

    createDirectoryListing(args.directory, DEFAULT_TEMPLATE, args.indexPage)

if __name__ == '__main__':
    main()
