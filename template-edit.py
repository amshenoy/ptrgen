for i in range(2, 9):
	ptr = open("SUMMER_CONSTANT").read()
	files = ["31" + str(n) for n in range(1, i+1)]
	count = 0
	ptr = ptr.replace("311", "blurgh")
	while True:
		if not "blurgh" in ptr:
			break
		ptr = ptr.replace("blurgh", files[count % i], 1)
		count += 1
	f = open("SUMMER_ALT_" + str(i), "w")
	f.write(ptr)
	f.close()
