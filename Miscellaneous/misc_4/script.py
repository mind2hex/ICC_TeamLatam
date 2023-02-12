#!/usr/bin/python3


message="933546130161408275468941458276407777538257142052827589758265461382521489415082461082521489238248142077774041454053828352823113235282142094408259404041824020236528824546824641825214408220525220485017171743406140828923826546136182107720451982682658268771746681147539234581391420516654753945233275098138665066596109740907"


matriz = """_ ' < P > ! R } V 4 f # 0 u h ( U . ) : a & [ s G - A ; , @ q m 5 O B Y 1 E j 6 e n X H Q g o x c = k 7 t ? 9 / ] W T b * r D | p y 2 + L ^ ` { \ ~ 8 d w l F Z C 3   I $ S % M K i J z N " v 0 0 0 0 0 """


result = []
counter = 0
for i in matriz:
    if counter == 0:
        result.append(i)
        counter = 1
    else:
        counter = 0

matriz = result


result = []
counter = 0
num = ""
for i in message:
    num += i
    if len(num) == 2:
        result.append(num)
        num = ""
        
message = result

for num in message:
    print(matriz[int(num)], end="")

print()
