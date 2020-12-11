
import java.util.Scanner;
import java.util.Scanner;
public class Ejercicio_1 {​​​​​​​
public class Ejercicio_1 {​​​​​​​
public static void main(String[] arg) {​​​​​​​public static void main(String[] arg) {​​​​​​​
int numero, i, k;int numero, i, k;
double j, n;double j, n;
String salida;String salida;
boolean cont = false;boolean cont = false;
Scanner leo = new Scanner(System.in);Scanner leo = new Scanner(System.in);
System.out.print("Introduce un número impar y mayor o iguaSystem.out.print("Introduce un número impar y mayor o igual que 3: ");l que 3: ");
do {​​​​​​​ //Selecciondo {​​​​​​​ //Seleccion
numero = leo.nextInt();numero = leo.nextInt();
if (numero < 3) {​​​​​​​if (numero < 3) {​​​​​​​
System.out.print("Número incorrecto, introduce otro valor: ");System.out.print("Número incorrecto, introduce otro valor: ");
}​​​​​​​ else {​​​​​​​}​​​​​​​ else {​​​​​​​
if (numero % 2 == 0) {​​​​​​​if (numero % 2 == 0) {​​​​​​​
System.out.print("Número incorrecto, introduce otro valor: ");System.out.print("Número incorrecto, introduce otro valor: ");
}​​​​​​​ else {​​​​​​​}​​​​​​​ else {​​​​​​​
cont = true;cont = true;
}​​​​​​​}​​​​​​​
}​​​​​​​}​​​​​​​
}​​​​​​​ while (cont == false);}​​​​​​​ while (cont == false);
// Triangulo Superior// Triangulo Superior
for (i = 0; i < (numero / 2); i++) {​​​​​​​for (i = 0; i < (numero / 2); i++) {​​​​​​​
salida = "";salida = "";
for (j = (numero / 2) for (j = (numero / 2) -- i; j > 0; ji; j > 0; j----) {​​​​​​​) {​​​​​​​
salida += " ";salida += " ";
}​​​​​​​}​​​​​​​
for (k = 0; k < (2 * i + 1); k++) {​​​​​​​for (k = 0; k < (2 * i + 1); k++) {​​​​​​​
salida += " *";salida += " *";
}​​​​​​​}​​​​​​​
System.out.println(salida);System.out.println(salida);
}​​​​​​​}​​​​​​​
//Centro//Centro
salida = "";salida = "";
for (i = 0; i < numero; i++) {​​​​​​​for (i = 0; i < numero; i++) {​​​​​​​
salida += " *";salida += " *";
}​​​​​​​}​​​​​​​
System.out.println(salida);System.out.println(salida);
//Triangulo Inferior//Triangulo Inferior
for (n = (nfor (n = (numero / 2); n > 0; numero / 2); n > 0; n----) {​​​​​​​) {​​​​​​​
salida = "";salida = "";
for (j = (numero / 2) for (j = (numero / 2) -- n + 1; j > 0; jn + 1; j > 0; j----) {​​​​​​​) {​​​​​​​
salida += " ";salida += " ";
}​​​​​​​}​​​​​​​
for (k = 0; k < (2 * n for (k = 0; k < (2 * n -- 1); k++) {​​​​​​​1); k++) {​​​​​​​
salida += " *";salida += " *";
}​​​​​​​}​​​​​​​
System.out.println(salida);System.out.println(salida);
}​​​​​​​}​​​​​​​
CIFP
A Carballeira-Marcos Valcárcel
}​​​​​​​}​​​​​​​
}​​​​​​​
}​​​​​​​

