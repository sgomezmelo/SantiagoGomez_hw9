#include <iostream>
#include <ctime>

using std::cout;
using std::endl;

int fibonacci(int N);
float get_time(int N);

/*Funcion que calcula el N-esimo termino de la serie de fibonacci*/ 
int fibonacci(int N){
  int resp;
  if(N == 1 || N == 2){
    resp = 1;
  }
  else{
    resp = fibonacci(N-1) + fibonacci(N-2); 
  }
  return resp;
}

/*Funcion que da el tiempo de computacion necesario para la funcion anterior*/ 
float get_time(int N){
  clock_t t;
  t = clock();
  int r = fibonacci(N);
  t = clock() - t;
  float time = ((float)t)/CLOCKS_PER_SEC;
  return time;
}

int main(){
  int N = 35;
  for(int i = 1; i<N+1; i++){
    cout << i << " " << get_time(i) << endl; 
  }
  return 0;
}
