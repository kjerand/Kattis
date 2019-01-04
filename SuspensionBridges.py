import math
d, s = [int(x) for x in input().split()]

def binarySearch(min_grense, ov_grense, d, s):
	midt = (min_grense + ov_grense) / 2 # gjetter en verdi i midten
	verdi = (midt * math.cosh(d / (2 * midt))) - (midt + s) # funksjonsverdien i midten

	if abs(verdi) < 0.00001:
		return midt # har funnet a

	if verdi > 0:
		return binarySearch(midt, ov_grense, d, s)
		# Siden funksjonsverdien er større enn 0, er jeg 100 % sikker på at jeg ikke finner
		# en løsning under midt. Derfor er det ingen vits i å søke der.
		# Søker altså fra midten og til øvre grense

	if verdi < 0:
		return binarySearch(min_grense, midt, d, s)
		# Samme grunn som ovenfor, bare at vi nå søker fra nedre grense til midt.

	else:
		return midt # Lite sannsynlig at denne situasjonen inntreffer, men her er verdi == 0, altså en perfekt a

a = binarySearch(0, 1000000000, d, s)
def l(a, d):
    return 2 * a * math.sinh(d / (2 * a))

answer = l(a, d)

print(answer)