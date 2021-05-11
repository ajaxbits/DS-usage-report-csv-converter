import csv

# For L2
# =IF(LEN(M2)>0,M2,(IF(A2=A1,L1,(IF(LEN(D2)>30,MID(D2,12,13),"")))))


def l_row_function(a1, a2, d2, l1, m2):
    if len(m2) > 0:
        return m2
    else:
        if a2 == a1:
            return l1
        else:
            if len(d2) > 30:
                return "midpoint of d2,12,13"
            else:
                return ""
