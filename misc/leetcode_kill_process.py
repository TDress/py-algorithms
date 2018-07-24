from lib import assertion

def _killPIDS(childmap, killed, kill):
    if kill in childmap:
        killed.append(kill)
        children = childmap.pop(kill)
        for pid in children:
            _killPIDS(childmap, killed, pid)

def killProcess(pid, ppid, kill):
    """
    :type pid: List[int]
    :type ppid: List[int]
    :type kill: int
    :rtype: List[int]
    """
    childmap, res = {}, []
    childmap[0] = []

    for i in range(len(pid)):
        childmap.setdefault(pid[i], [])
        try:
            childmap[ppid[i]].append(pid[i])
        except KeyError:
            childmap[ppid[i]] = [pid[i]]

    if not len(childmap[0]):
        raise TypeError('no root process in pids')
    if childmap[0].pop() == kill:
        return pid 
    childmap.pop(0)
    print(childmap)
    _killPIDS(childmap, res, kill)
    return res

def main():
    pid = [1,3,10,5]
    ppid = [3,0,5,3]
    kill = 5
    assertion.equals([5, 10], killProcess(pid, ppid, kill))

    pid = [1]
    ppid = [0]
    kill = 1
    assertion.equals([1], killProcess(pid, ppid, kill))

if __name__ == "__main__":
    main()
