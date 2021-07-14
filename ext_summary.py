
import os, sys


# Collect stats on file extensions
ext_dict = {}

for root, dirs, files in os.walk(u"F:/"):
    for file in files:
        f, e = os.path.splitext(file)

        if e not in ext_dict:
            ext_dict[e] = 1
        else:
            ext_dict[e] += 1

stats = sorted(ext_dict.items(), key=lambda x: x[1], reverse=True)
for ext in stats:
    print(f"{ext[0]} : {ext[1]}")

