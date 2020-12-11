def sol2(data):
    """misunderstood the problem statement, but leaving this cuz is neat lol"""
    ind = PREAMBLE
    while ind < len(data):
        valid = False
        curr = data[ind]
        t = 0
        head = ind - PREAMBLE
        tail = t
        while head < ind:
            t += data[head]
            if t == curr:
                valid = True
                break
            elif t > curr:
                t -= tail
                tail += 1
                if tail > head:
                    head += 1
            else:
                head += 1
        if not valid:
            return curr

