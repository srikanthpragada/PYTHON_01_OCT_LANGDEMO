import os

files = os.walk(r"e:\classroom\python\oct1")

for dirname,dirs,files in files:
    if dirname.find(".git") > 0:
        continue

    print(dirname)
    print("=" * len(dirname))

    # files that end with .py
    for f in files:
        if f.endswith(".py"):
            print(f)



