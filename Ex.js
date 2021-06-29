package com.calc;

public class Calc {

  public static void main(String[] args) {
  
  //var
  int janeiro = 15000;
  int fevereiro = 23000;
  int março = 17000;
  int total = janeiro+fevereiro+março;
  float media = total / 3;
  
  //msg
  System.out.println("em tal trimestre o total de gasto foram"+ total + "\n sua media é de " + media);
  //condiçao
  if (total <= 55000) {
    System.out.print("os gastos sao superaveis");
  } else {
    System.out.println("os gasto ultrapassaram o limite");
  }
   
  }
}
