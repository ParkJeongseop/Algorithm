//ÇÏ³ª¾¿ 
public class OopEx5ReverseInt {

  public static void main(String[] args) {
    System.out.println(Solution(71432));

  }

  public static int Solution(int number) {
    int power = 0;
    int num = number;
    int answer = 0;
    while (num / 10 != 0) {
      power += 1;
      num /= 10;
    }
    num = number;
    while (num / 10 != 0) {
      answer += num % 10 * Math.pow(10, power);
      power -= 1;
      num /= 10;
    }
    answer += num;
    return answer;

  }

}
