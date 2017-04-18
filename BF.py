import sys, glob

post_path=sys.argv[1]
prior_path=sys.argv[2]
burnin=float(sys.argv[3])
anatolia_post = 0
steppes_post = 0
anatolia_prior = 0
steppes_prior = 0
noTrees_post = 0
noTrees_prior = 0

print("User gave a burnin of ", burnin)
for f1 in glob.iglob(post_path+"/*.run*p"):
    print("Opening file ", f1)
    lines = open(f1).readlines()
    noTrees_post += len(lines[2:])
    for line in lines[int(burnin*noTrees_post):]:
        line = line.replace("\n","")
        arr = line.split("\t")
        tree_height = float(arr[3])/float(arr[-1])
        if tree_height >=5500.0 and tree_height <= 6500.0:
            steppes_post+=1.0
        elif tree_height >=8000.0 and tree_height <= 9500.0:
            anatolia_post+=1.0

for f1 in glob.iglob(prior_path+"/*.run*p"):
    print("Opening file ", f1)
    lines = open(f1).readlines()
    noTrees_prior += len(lines[2:])
    for line in lines[int(burnin*noTrees_prior):]:
        line = line.replace("\n","")
        arr = line.split("\t")
        tree_height = float(arr[3])/float(arr[-1])
        if tree_height >=5500.0 and tree_height <= 6500.0:
            steppes_prior+=1.0
        elif tree_height >=8000.0 and tree_height <= 9500.0:
            anatolia_prior+=1.0

assert noTrees_post == noTrees_prior
num1 = steppes_post/(burnin*noTrees_post)
num2 = anatolia_post/(burnin*noTrees_post)
denom1 = steppes_prior/(burnin*noTrees_prior)
denom2 = anatolia_prior/(burnin*noTrees_prior)
BF = (num1/denom1)/(num2/denom2)
print("Steppes numbers ", steppes_post, steppes_prior, noTrees_post, num1, denom1)
print("Anatolia numbers ", anatolia_post, anatolia_prior, noTrees_prior, num2, denom2)
print("Bayes Factor for Steppes vs. Anatolia is ", BF)


