def koh(t, order, size):

	if order == 0:
		t.forward(size)
	else:
		koh(t, order-1, size/3)
		t.left(60)
		koh(t, order-1, size/3)
        t.right(120)
        koh(t, order-1, size/3)
        t.left(60)
        koh(t, order-1, size/3)