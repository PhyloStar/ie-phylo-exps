import sys, glob

post_path=sys.argv[1]
for f1 in glob.iglob(post_path+"/*.run*p"):
    f1w = f1+".age"
    fw = open(f1w, "w")
    print("Opening file ", f1)
    lines = open(f1).readlines()
    for i, line in enumerate(lines):
        if i==0:
            fw.write(line)
            continue
        elif i==1:
            line = line.replace("\n","")
            fw.write(line+"\t"+"Root_Age"+"\n")
            continue
        line = line.replace("\n","")
        arr = line.split("\t")
        tree_height = float(arr[3])/float(arr[-1])
        fw.write(line+"\t"+str(tree_height)+"\n")
    fw.close()


