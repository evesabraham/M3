#perceived risk
female_mult = 3
male_mult = 1.28
young = 0.177
middle = 0.672
old = 1.4
elder = 0.706
perceived_risk = 0

age = int(input("age:"))
gender = input("gender M/F: ")

def rp(a, g):
    if a <= 35 and a >= 18:
        perceived_risk = young
    elif a <= 50 and a >= 36:
        perceived_risk = middle
    elif a <= 70 and a >= 51:
        perceived_risk = old
    elif a >= 71:
        perceived_risk = elder

    if g == "M":
        return perceived_risk*male_mult
    elif g == "F":
        return perceived_risk*female_mult


final_rp=rp(age,gender)

#total risk tolerance
f_mult = 1
m_mult = 1.55
has_children = input("children y/n: ")
married = input("married y/n: ")
gambling_xp = int(input("years of gambling experience: "))


def rf(c, m):
    if c == "y":
        return 0.304
    elif m == "y":
        return 0.494
    else:
        return 1

def rl(gambler):
    if gambler < 1:
        return 0
    elif gambler >=1 and gambler<=5:
        return 0.25
    else:
        return 0.5

family = rf(has_children, married)
xp = rl(gambling_xp)


def rt(f, x, s, per):
    if s == "M":
        temp_total = f+x
        temp_total = temp_total*m_mult
        temp_total = temp_total/per
        return temp_total
    else:
        temp_total = f+x
        temp_total = temp_total*f_mult
        temp_total = temp_total/per
        return temp_total

final_rt = rt(family, xp, gender, final_rp)
print(final_rt)

