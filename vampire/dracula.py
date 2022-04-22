#!/usr/bin/env python3
count = 0
zoink= open("vampytimes.txt", "w")
with open("345-0.txt","r") as foo:
    for line in foo:
        if "vampire" in line.lower():
            print(line)
            count += 1
            zoink.write(line)
zoink.close()
print(count)


