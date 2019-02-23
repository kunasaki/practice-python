# -*- coding: utf-8 -*-
def hanoi(n,a="a",b="b",c="c"):
	if n > 0 :
		hanoi(n-1,a,c,b)
		print("move a disc from %s to %s" % (a,c))
		hanoi(n-1,b,a,c)
hanoi(3,a,b,c)