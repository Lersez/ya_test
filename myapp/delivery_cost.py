
def delivery_cost_calculator(distance, dimensions, fragile, workload=1):
	# создаем переменную, в которой будет хранится стоимость доставки
	delivery_cost = 0
	# создаем переменную-флаг для далекой доставки хрупкого груза
	cant_deliver_fragile = False
	# также определяем коэффициенты нагрузки для службы доставки
	workload_rate = { 4: 1.6, 3: 1.4, 2: 1.2, 1: 1 } 
	
	# влияние дистанции на конечную сумму
	if distance > 30: delivery_cost += 300; cant_deliver_fragile = True
	elif distance > 10: delivery_cost += 200
	elif distance > 2: delivery_cost += 100
	else: delivery_cost += 50 ########raise ValueError("Exception 123 raised")
	
	# влияние габаритов
	if dimensions == 0: delivery_cost += 100
	elif dimensions == 1: delivery_cost += 200
	
	# влияние хрупкости
	if bool(fragile):
		if cant_deliver_fragile: return "Can't be delivered"
		else: delivery_cost += 300
	
	# влияние нагрузки
	delivery_cost = int(delivery_cost * workload_rate[workload])
	print(f'Debugging: {distance=}, {dimensions=}, {fragile=}, {workload=}\n{delivery_cost=}\n{10*"--"}')
	
	return delivery_cost if delivery_cost > 400 else 400
	