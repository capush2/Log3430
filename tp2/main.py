from criteres import *

if __name__ == "__main__":
    print("Racc on S1: ")
    racc_test_cases = racc()

    for i in range(len(racc_test_cases)):
        print(f"d{i+1} = {racc_test_cases[i]}")

    print("Ricc on S1: ")
    ricc_test_cases = ricc()

    for i in range(len(ricc_test_cases)):
        print(f"d{i+1} = {ricc_test_cases[i]}")

    print("Vns on S2: ")
    vns_test_cases = vns()

    for i in range(len(vns_test_cases)):
        print(f"d{i+1} = {vns_test_cases[i]}")

    print("p h t1 t2 t3")
    for p in range(2):
        for h in range(2):
            for t1 in range(2):
                for t2 in range(2):
                    for t3 in range(2):
                        print(str(p) + " " + str(h) + " " + str(t1) + "  " + str(t2) + "  " + str(t3) + " " + str(
                            bool(s1(p, h, t1, t2, t3))))