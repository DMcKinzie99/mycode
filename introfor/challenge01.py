#!/usr/bin/env python3

def main():

    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
    userinput=input("What is the name of the farm you want to learn about? ")
    if userinput== farms[1]:
        print(for x in farms:
                print(x.get("name")))

    for x in farms:
        print(x.get("name", "Unknown Farm"), end=":\n")
        for agri in x.get("agriculture"):
            print(" -", agri)
if __name__ == "__main__":
    main()





        

