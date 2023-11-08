txt = open("intro.txt")

counts = dict()

for lin in txt:
    lin = lin.rstrip()
    wds = lin.split()
    print(wds)
    for w in wds:
        # idiom: retrieve/create/update counter
        counts[w] = counts.get(w, 0) + 1

# find most common word
mostcommon = None
for key in counts:
    if mostcommon is None:
        mostcommon = [key, counts[key]]
    elif mostcommon[1] < counts[key]:
        mostcommon = [key, counts[key]]
    else:
        continue
    
print("most common word is: ", mostcommon)

print("top 3 word-tuples are: ", sorted([(v, k) for k, v in counts.items()], reverse=True)[:3])