cpp_vs_python.png: times_python.csv times_cpp.csv 
	python SantiagoGomez_Graficas.py
times_python.csv:  
	python  SantiagoGomez_GenerarTiempos.py > times_python.csv
times_cpp.csv: gen_times.x
	./gen_times.x > times_cpp.csv
gen_times.x: 
	c++  SantiagoGomez_GenerarTiempos.cpp -o gen_times.x
