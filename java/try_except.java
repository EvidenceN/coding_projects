class DivideByZero {
    public static void main(String[] args) {
      int a = 27, b = 0;
      try {
        System.out.println("I'm executed first!");
        int c = a / b; // This will throw an exception
        System.out.println("I'm never executed!");
      } catch (ArithmeticException e) {
        System.out.println("Exception Caught!");
        e.printStackTrace();
      }
        System.out.println("Done!");
    }
  }
  