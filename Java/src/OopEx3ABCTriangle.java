//OOP Class EX#3
public class OopEx3ABCTriangle {

  public static void main(String[] args) {
    solution('e');

  }
  
  public static void solution(char t) {
    char i = t;
    while((int)i >= (int)'a') {
      char j = 'a';
      while((int)j <= (int)i) {
        System.out.print(j);
        j = (char)((int)j+1);
      }
      System.out.println();
      i = (char)((int)i-1);
    }
  }

}
