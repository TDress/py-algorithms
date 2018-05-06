from lib import assertion


def solveTowers(n, start, dest, buffer):
    if n == 1:
        dest.append(start.pop())
    elif n > 1:
        solveTowers(n - 1, start, buffer, dest)
        dest.append(start.pop())
        solveTowers(n - 1, buffer, dest, start)

# 3 towers; all discs start out on the starting disc.  A disc can 
# never rest on a smaller disc.  You can only move one disc at a time.
def towersOfHanoi(start, dest, spare):
    solveTowers(9, start, dest, spare)



def main():
    t1, t2, t3 = [9,8,7,6,5,4,3,2,1], [], []
    towersOfHanoi(t1, t3, t2)

    assertion.equals([9,8,7,6,5,4,3,2,1], t3)

if __name__ == '__main__':
    main()
