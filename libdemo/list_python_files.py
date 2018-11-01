import os

files = os.walk(r"e:\classroom\python\oct1")

for dirname,dirs,files in files:
    if dirname.find(".git") > 0:
        continue

    filenames = []
    # files that end with .py
    for f in files:
        if f.endswith(".py"):
             filenames.append(f)
    
    if len(filenames) > 0:
        print(dirname)
        print("=" * len(dirname))
        for name in filenames:
            print(name)





