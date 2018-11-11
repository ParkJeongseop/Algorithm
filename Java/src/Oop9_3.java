
public class Oop9_3 {

  public static void main(String[] args) {
    System.out.print(solution(12, 0, 3));

  }

  public static int solution(int h, int m, int a) {
    int answer = 0;
    int h2 = h;
    int m2 = m;
    int passMin = 0;

    do {
      m++;
      m2 += a;
      passMin++;
      if (m > 59) {
        m = 0;
        h++;
      }
      if (m2 > 59) {
        m2 = 0;
        h2++;
      }
    } while (h != h2 || m != m2);
    System.out.println(passMin);
    answer = passMin + h + m;

    return answer;
  }

}
