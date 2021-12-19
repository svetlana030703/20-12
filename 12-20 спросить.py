
def f(word):
	p = 0
	l = len(word) - 1
	
	while p >= l:
		if not word[l] == word[p]:
			return False
		l += 1
		p -= 1
	return True
print(f('gfhdjkfgj'))
