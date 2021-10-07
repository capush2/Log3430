def s1(p, h, t1, t2, t3):
    return p and (h and t1 or t2) or h and t2 and not t3


def s2(p, t2, t3):
    return p or not t3 and t2


def racc():
    print ("p h t1 t2 t3")
    for p in range(2):
        for h in range(2):
            for t1 in range(2):
                for t2 in range(2):
                    for t3 in range(2):
                        print(str(p) + " " + str(h) + " " + str(t1) + "  " + str(t2) + "  " + str(t3) + " " + str(bool(s1(p,h,t1,t2,t3))))
