def bnc_bck_frth(k):
    trig = 0
    num = 1
    def process():
        nonlocal num
        if trig == 0: num += 1
        if trig == 1: num -= 1
    def switch():
        nonlocal trig
        if trig == 0: trig = 1
        else: trig = 0
    for i in range(2, k+1):
        process()
        if i % 7 == 0 or "7" in list(str(i)):
            switch()
    return num

print("bnc_bck_frth(7) = ", bnc_bck_frth(7))
print("bnc_bck_frth(8) = ", bnc_bck_frth(8))
print("bnc_bck_frth(15) = ", bnc_bck_frth(15))
print("bnc_bck_frth(21) = ", bnc_bck_frth(21))
print("bnc_bck_frth(22) = ", bnc_bck_frth(22))
print("bnc_bck_frth(30) = ", bnc_bck_frth(30))
print("bnc_bck_frth(68) = ", bnc_bck_frth(68))
print("bnc_bck_frth(69) = ", bnc_bck_frth(69))
print("bnc_bck_frth(70) = ", bnc_bck_frth(70))
print("bnc_bck_frth(71) = ", bnc_bck_frth(71))
print("bnc_bck_frth(72) = ", bnc_bck_frth(72))
print("bnc_bck_frth(100) = ", bnc_bck_frth(100))