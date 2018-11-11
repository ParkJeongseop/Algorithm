// OOP Class EX#4
public class OopEx4RandIntArray {

  public static void main(String[] args) {
    int[] answer = solution(50);
    for (int i = 0; i < 50; i++) {
      System.out.print(answer[i] + ", ");
    }
  }

  public static int[] solution(int n) {
    int[] answer = new int[n];
    answer[0] = (int) (Math.random() * 100 + 1);
    for (int i = 1; i < n; i++) {
      boolean check = true;
      while (check) {
        int randInt = (int) (Math.random() * 100 + 1);
        System.out.println("test"+randInt);
        for (int j = 0; j < i; j++) {
          if (randInt == answer[j]) {
            System.out.println("True");
            check = true;
            break;
          } else {
            //System.out.println("False");
            check = false;
          }
        }
        answer[i] = randInt;
      }
    }

    return answer;
  }

}
