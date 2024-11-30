import random

def main():
    list = random.sample(range(1,50),7)
    method = input("How should these be sorted? ")

    def sortedasc():
        for i in range(0, len(list)):
            for j in range(i+1, len(list)):
                if list[i] >= list[j]:
                    list[i], list[j] = list[j], list[i]

    def sorteddesc():
        for i in range(0, len(list)):
            for j in range(i+1, len(list)):
                if list[i] <= list[j]:
                    list[i], list[j] = list[j], list[i]
    
    def sort():
        if "Asc" in method:
            sortedasc()
            print("Here ya go! \n",list)
        elif "asc" in method:
            sortedasc()
            print("Here ya go! \n",list)
        elif "Desc" in method:
            sorteddesc()
            print("Ecellent choice! \n",list)
        elif "desc" in method:
            sorteddesc()
            print("Ecellent choice! \n",list)
        else:
            print("Awww bummer:(\n",list)

    sort()
            
main()