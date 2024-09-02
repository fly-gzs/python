"""
Készíts egy programot, amely a felhasználótól két külön kérdésben megkérdezi,
hogy az ikrek (Henrik és Hanna) jönnek-e ma kosrazni!
Például így: Jön Henrik ma kosarazni? (igen/nem).
A program írja ki, hogy melyik állítás igaz az alábbiak közül:
- egyikük sem jön kosarazni,
- mind a ketten jönnek kosarazni,
- csak az egyikük jön kosarazni.
"""

henrik = input("Henrik jön ma kosarazni? (igen/nem): ")
hanna = input("Hanna jön ma kosarazni? (igen/nem): ")
igen = ""

if (henrik == "igen"):
    igen = "HENRIK"
if (hanna == "igen"):
    igen = "HANNA"
    
if (henrik == "nem" and hanna == "nem"):
    print("Egyikük sem jön kosarazni.")
elif (henrik == "igen" and hanna == "igen"):
    print("Mind a ketten jönnek kosarazni.")
else:
    print("Csak " + igen + " jön kosarazni.")