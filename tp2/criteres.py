def s1(p, h, t1, t2, t3):
    return p and (h and t1 or t2) or h and t2 and not t3


def imp2(t2, t3):
    return int(not t3 and t2)


def s2(p, t2, t3):
    return p or imp2(t2, t3)


def racc():
    test_set = []
    test_cases_found = False
    # P est la clause majeure
    for h in range(2):
        for t1 in range(2):
            for t2 in range(2):
                for t3 in range(2):
                    pred1 = bool(s1(True, h, t1, t2, t3))
                    pred2 = bool(s1(False, h, t1, t2, t3))
                    if not test_cases_found and pred1 != pred2:
                        test_cases_found = True
                        d1 = f"<{{P = 1, H = {h}, T1 = {t1}, T2 = {t2}, T3 = {t3}}}, {{{pred1}}}>"
                        d2 = f"<{{P = 0, H = {h}, T1 = {t1}, T2 = {t2}, T3 = {t3}}}, {{{pred2}}}>"
                        if d1 not in test_set:
                            test_set.append(d1)
                        if d2 not in test_set:
                            test_set.append(d2)
    test_cases_found = False

    # H est la clause majeure
    for p in range(2):
        for t1 in range(2):
            for t2 in range(2):
                for t3 in range(2):
                    pred1 = bool(s1(p, True, t1, t2, t3))
                    pred2 = bool(s1(p, False, t1, t2, t3))
                    if not test_cases_found and pred1 != pred2:
                        test_cases_found = True
                        d1 = f"<{{P = {p}, H = 1, T1 = {t1}, T2 = {t2}, T3 = {t3}}}, {{{pred1}}}>"
                        d2 = f"<{{P = {p}, H = 0, T1 = {t1}, T2 = {t2}, T3 = {t3}}}, {{{pred2}}}>"
                        if d1 not in test_set:
                            test_set.append(d1)
                        if d2 not in test_set:
                            test_set.append(d2)
    test_cases_found = False

    # T1 est la clause majeure
    for p in range(2):
        for h in range(2):
            for t2 in range(2):
                for t3 in range(2):
                    pred1 = bool(s1(p, h, True, t2, t3))
                    pred2 = bool(s1(p, h, False, t2, t3))
                    if not test_cases_found and pred1 != pred2:
                        test_cases_found = True
                        d1 = f"<{{P = {p}, H = {h}, T1 = 1, T2 = {t2}, T3 = {t3}}}, {{{pred1}}}>"
                        d2 = f"<{{P = {p}, H = {h}, T1 = 0, T2 = {t2}, T3 = {t3}}}, {{{pred2}}}>"
                        if d1 not in test_set:
                            test_set.append(d1)
                        if d2 not in test_set:
                            test_set.append(d2)
    test_cases_found = False

    # T2 est la clause majeure
    for p in range(2):
        for h in range(2):
            for t1 in range(2):
                for t3 in range(2):
                    pred1 = bool(s1(p, h, t1, True, t3))
                    pred2 = bool(s1(p, h, t1, False, t3))
                    if not test_cases_found and pred1 != pred2:
                        test_cases_found = True
                        d1 = f"<{{P = {p}, H = {h}, T1 = {t1}, T2 = 1, T3 = {t3}}}, {{{pred1}}}>"
                        d2 = f"<{{P = {p}, H = {h}, T1 = {t1}, T2 = 0, T3 = {t3}}}, {{{pred2}}}>"
                        if d1 not in test_set:
                            test_set.append(d1)
                        if d2 not in test_set:
                            test_set.append(d2)
    test_cases_found = False

    # T3 est la clause majeure
    for p in range(2):
        for h in range(2):
            for t1 in range(2):
                for t2 in range(2):
                    pred1 = bool(s1(p, h, t1, t2, True))
                    pred2 = bool(s1(p, h, t1, t2, False))
                    if not test_cases_found and pred1 != pred2:
                        test_cases_found = True
                        d1 = f"<{{P = {p}, H = {h}, T1 = {t1}, T2 = {t2}, T3 = 1}}, {{{pred1}}}>"
                        d2 = f"<{{P = {p}, H = {h}, T1 = {t1}, T2 = {t2}, T3 = 0}}, {{{pred2}}}>"
                        if d1 not in test_set:
                            test_set.append(d1)
                        if d2 not in test_set:
                            test_set.append(d2)

    return test_set


def ricc():
    test_set = []
    true_pred_found = False
    false_pred_found = False

    # P est la clause majeure
    for h in range(2):
        for t1 in range(2):
            for t2 in range(2):
                for t3 in range(2):
                    pred1 = bool(s1(True, h, t1, t2, t3))
                    pred2 = bool(s1(False, h, t1, t2, t3))
                    if pred1 == pred2:
                        if pred1 and not true_pred_found:
                            true_pred_found = True
                            d1 = f"<{{P = 1, H = {h}, T1 = {t1}, T2 = {t2}, T3 = {t3}}}, {{{pred1}}}>"
                            d2 = f"<{{P = 0, H = {h}, T1 = {t1}, T2 = {t2}, T3 = {t3}}}, {{{pred2}}}>"
                            if d1 not in test_set:
                                test_set.append(d1)
                            if d2 not in test_set:
                                test_set.append(d2)
                        if not pred1 and not false_pred_found:
                            false_pred_found = True
                            d1 = f"<{{P = 1, H = {h}, T1 = {t1}, T2 = {t2}, T3 = {t3}}}, {{{pred1}}}>"
                            d2 = f"<{{P = 0, H = {h}, T1 = {t1}, T2 = {t2}, T3 = {t3}}}, {{{pred2}}}>"
                            if d1 not in test_set:
                                test_set.append(d1)
                            if d2 not in test_set:
                                test_set.append(d2)
    true_pred_found = False
    false_pred_found = False

    # H est la clause majeure
    for p in range(2):
        for t1 in range(2):
            for t2 in range(2):
                for t3 in range(2):
                    pred1 = bool(s1(p, True, t1, t2, t3))
                    pred2 = bool(s1(p, False, t1, t2, t3))
                    if pred1 == pred2:
                        if pred1 and not true_pred_found:
                            true_pred_found = True
                            d1 = f"<{{P = {p}, H = 1, T1 = {t1}, T2 = {t2}, T3 = {t3}}}, {{{pred1}}}>"
                            d2 = f"<{{P = {p}, H = 0, T1 = {t1}, T2 = {t2}, T3 = {t3}}}, {{{pred2}}}>"
                            if d1 not in test_set:
                                test_set.append(d1)
                            if d2 not in test_set:
                                test_set.append(d2)
                        if not pred1 and not false_pred_found:
                            false_pred_found = True
                            d1 = f"<{{P = {p}, H = 1, T1 = {t1}, T2 = {t2}, T3 = {t3}}}, {{{pred1}}}>"
                            d2 = f"<{{P = {p}, H = 0, T1 = {t1}, T2 = {t2}, T3 = {t3}}}, {{{pred2}}}>"
                            if d1 not in test_set:
                                test_set.append(d1)
                            if d2 not in test_set:
                                test_set.append(d2)
    true_pred_found = False
    false_pred_found = False

    # T1 est la clause majeure
    for p in range(2):
        for h in range(2):
            for t2 in range(2):
                for t3 in range(2):
                    pred1 = bool(s1(p, h, True, t2, t3))
                    pred2 = bool(s1(p, h, False, t2, t3))
                    if pred1 == pred2:
                        if pred1 and not true_pred_found:
                            true_pred_found = True
                            d1 = f"<{{P = {p}, H = {h}, T1 = 1, T2 = {t2}, T3 = {t3}}}, {{{pred1}}}>"
                            d2 = f"<{{P = {p}, H = {h}, T1 = 0, T2 = {t2}, T3 = {t3}}}, {{{pred2}}}>"
                            if d1 not in test_set:
                                test_set.append(d1)
                            if d2 not in test_set:
                                test_set.append(d2)
                        if not pred1 and not false_pred_found:
                            false_pred_found = True
                            d1 = f"<{{P = {p}, H = {h}, T1 = 1, T2 = {t2}, T3 = {t3}}}, {{{pred1}}}>"
                            d2 = f"<{{P = {p}, H = {h}, T1 = 0, T2 = {t2}, T3 = {t3}}}, {{{pred2}}}>"
                            if d1 not in test_set:
                                test_set.append(d1)
                            if d2 not in test_set:
                                test_set.append(d2)
    true_pred_found = False
    false_pred_found = False

    # T2 est la clause majeure
    for p in range(2):
        for h in range(2):
            for t1 in range(2):
                for t3 in range(2):
                    pred1 = bool(s1(p, h, t1, True, t3))
                    pred2 = bool(s1(p, h, t1, False, t3))
                    if pred1 == pred2:
                        if pred1 and not true_pred_found:
                            true_pred_found = True
                            d1 = f"<{{P = {p}, H = {h}, T1 = {t1}, T2 = 1, T3 = {t3}}}, {{{pred1}}}>"
                            d2 = f"<{{P = {p}, H = {h}, T1 = {t1}, T2 = 0, T3 = {t3}}}, {{{pred2}}}>"
                            if d1 not in test_set:
                                test_set.append(d1)
                            if d2 not in test_set:
                                test_set.append(d2)
                        if not pred1 and not false_pred_found:
                            false_pred_found = True
                            d1 = f"<{{P = {p}, H = {h}, T1 = {t1}, T2 = 1, T3 = {t3}}}, {{{pred1}}}>"
                            d2 = f"<{{P = {p}, H = {h}, T1 = {t1}, T2 = 0, T3 = {t3}}}, {{{pred2}}}>"
                            if d1 not in test_set:
                                test_set.append(d1)
                            if d2 not in test_set:
                                test_set.append(d2)
    true_pred_found = False
    false_pred_found = False

    # T3 est la clause majeure
    for p in range(2):
        for h in range(2):
            for t1 in range(2):
                for t2 in range(2):
                    pred1 = bool(s1(p, h, t1, t2, True))
                    pred2 = bool(s1(p, h, t1, t2, False))
                    if pred1 == pred2:
                        if pred1 and not true_pred_found:
                            true_pred_found = True
                            d1 = f"<{{P = {p}, H = {h}, T1 = {t1}, T2 = {t2}, T3 = 1}}, {{{pred1}}}>"
                            d2 = f"<{{P = {p}, H = {h}, T1 = {t1}, T2 = {t2}, T3 = 0}}, {{{pred2}}}>"
                            if d1 not in test_set:
                                test_set.append(d1)
                            if d2 not in test_set:
                                test_set.append(d2)
                        if not pred1 and not false_pred_found:
                            false_pred_found = True
                            d1 = f"<{{P = {p}, H = {h}, T1 = {t1}, T2 = {t2}, T3 = 1}}, {{{pred1}}}>"
                            d2 = f"<{{P = {p}, H = {h}, T1 = {t1}, T2 = {t2}, T3 = 0}}, {{{pred2}}}>"
                            if d1 not in test_set:
                                test_set.append(d1)
                            if d2 not in test_set:
                                test_set.append(d2)

    return test_set


def vns():
    test_set = []

    # PPF pour clause P
    test_cases_found = False
    for p in range(2):
        for t2 in range(2):
            for t3 in range(2):
                pred1 = s2(p, t2, t3)
                if not test_cases_found and not pred1 and s2(not p, t2, t3):
                    test_cases_found = True
                    test_case = f"<{{P = {p}, T2 = {t2}, T3 = {t3}}}, {{Z = {bool(pred1)}}}>"
                    if test_case not in test_set:
                        test_set.append(test_case)

    # PPF pour clause T2
    test_cases_found = False
    for p in range(2):
        for t2 in range(2):
            for t3 in range(2):
                pred1 = s2(p, t2, t3)
                if not test_cases_found and not pred1 and s2(p, not t2, t3):
                    test_cases_found = True
                    test_case = f"<{{P = {p}, T2 = {t2}, T3 = {t3}}}, {{Z = {bool(pred1)}}}>"
                    if test_case not in test_set:
                        test_set.append(test_case)

    # PPF pour clause T3
    test_cases_found = False
    for p in range(2):
        for t2 in range(2):
            for t3 in range(2):
                pred1 = s2(p, t2, t3)
                if not test_cases_found and not pred1 and s2(p, t2, not t3):
                    test_cases_found = True
                    test_case = f"<{{P = {p}, T2 = {t2}, T3 = {t3}}}, {{Z = {bool(pred1)}}}>"
                    if test_case not in test_set:
                        test_set.append(test_case)

    # PUV pour implicant P
    test_cases_found = False
    for p in range(2):
        for t2 in range(2):
            for t3 in range(2):
                pred1 = s2(p, t2, t3)
                if not test_cases_found and p and not imp2(t2, t3):
                    test_cases_found = True
                    test_case = f"<{{P = {p}, T2 = {t2}, T3 = {t3}}}, {{Z = {bool(pred1)}}}>"
                    if test_case not in test_set:
                        test_set.append(test_case)

    # PPF pour implicant ~T3*T2
    test_cases_found = False
    for p in range(2):
        for t2 in range(2):
            for t3 in range(2):
                pred1 = s2(p, t2, t3)
                if not test_cases_found and not p and imp2(t2, t3):
                    test_cases_found = True
                    test_case = f"<{{P = {p}, T2 = {t2}, T3 = {t3}}}, {{Z = {bool(pred1)}}}>"
                    if test_case not in test_set:
                        test_set.append(test_case)

    return test_set
