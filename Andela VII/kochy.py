def koch(t, order, size):

	if order == 0:
		t.forward(size)
	else:
		koch(t, order-1, size/3)
		t.left(60)
		koch(t, order-1, size/3)
		t.right(120)
		koch(t, order-1, size/3)
		t.left(60)
		koch(t, order-1, size/3)