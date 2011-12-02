matchlist = []
filematch = "captureStore*"

# the below returns the number of items in /dev that match 'captureStore*'
if os.path.exists(src):
    for file in os.listdir(src):
        if fnmatch.fnmatch(file, filematch):
            #print file
            matchlist.append(file)
        else:
            matchlist = []

    file_count = len(matchlist)

    print file_count

