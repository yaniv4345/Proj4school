def id_checker(number):
    if len(number) < 9:
	addZeros = 9 - len(number)
	new_number = ""
	for i in range(0,addZeros):
		new_number = new_number + "0"
        new_number = new_number +  number
        number = new_number
    j = 1
    sum = 0
    for i in number:
        i = int(i)
        if j % 2 == 0:
            mul = 2
        else:
            mul = 1
        current = i * mul
        if current > 9 :
            current = current/10 + current%10
        sum = sum + current
        j = j + 1
    if sum % 10 == 0:
        return False
    else:
        return True
