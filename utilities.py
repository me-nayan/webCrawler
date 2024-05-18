import os

# Each website visited is a project (folder) created 
def createProjectDirectory(directory):
    if not os.path.exists(directory):
        print("Creating project: " + directory)
        os.makedirs(directory)

# Create queue and crawled files (if not created)
def createDataFiles(projectName, baseUrl):
    queue = projectName + "/queue.txt"
    crawled = projectName + "/crawled.txt"
    if not os.path.isfile(queue):
        writeFile(queue, baseUrl)
    if not os.path.isfile(crawled):
        writeFile(crawled, "")

# Create new file
def writeFile(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()

# Add data to existing file
def appendToFile(path, data):
    with open(path, "a")as file:
        file.write(data + "\n")

# Delete contents of a file
def deleteFileContents(path):
    with open(path, "w"):
        pass

# Read a file and convert each line to a set item
def fileToSet(fileName):
    results = set()
    with open(fileName, "rt") as f:
        for line in f:
            results.add(line.replace("\n", ""))

# Iterate through a set, each item in set will be a new line in the file
def setToFile(links, file):
    deleteFileContents(file)
    for link in sorted(links):
        appendToFile(file, link)