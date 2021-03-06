import os

def loadfile(name):
    file = open(name, "r")
    f = file.readlines()
    mapKey = {}
    for ind in range(len(f)):
        f[ind]=f[ind].rstrip()
    for row in range(len(f)):
        for col in range(len(f[row])):
            if f[row][col] not in mapKey:
                mapKey[f[row][col]]=str((row,col))
            else:
                mapKey[f[row][col]]+=", " + str((row, col))
    save_path = '/Users/zzw_e/Desktop/Research/Recommender game/game-level-recommender-system/examples/output-indexes'
    output_name = os.path.join(save_path, "Index_"+name)
    output = open(output_name, "w")
    output.write("object : Index\n\n")
    for i in mapKey:
        output.write(i + " : "+mapKey[i]+"\n\n")
    file.close()
    output.close()


def main():
    path = "/Users/zzw_e/Desktop/Research/Recommender game/game-level-recommender-system/examples/gridphysics"
    directory = os.fsencode(path)
    fLst = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt") or filename.endswith(".py"):
            # print(os.path.join(directory, filename))
            fLst.append(filename)
        else:
            continue
        fLst.sort()
    print(fLst)
    for file in fLst:
        if "lvl" in file:
            loadfile(file)


main()