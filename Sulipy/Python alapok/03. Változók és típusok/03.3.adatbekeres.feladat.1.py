'''
Thonny fejlesztői környezetben készíts egy rövid programot,
amely a felhasználótól bekéri a kör sugarát,
és ennek alapján kiszámolja a kör kerületét és területét!
'''
r=int(input("Kérem adja meg a kör sugarát: "))
# print(r)
PI=3.14
K=2*r*PI
K=round(K,2)
T=r*r*PI
T=round(T,2)
kerulet="Az " + str(r) +  " cm sugarú kör kerülete: K = " + str(K) + " cm"
terulet="Az " + str(r) +  " cm sugarú kör területe: T = " + str(T) + " cm2"
print(kerulet)
print(terulet)