public class dog_years {
    public static void main(String[] args) {
        int myAge = 27;

        double earlyYears = 2;

        earlyYears *= 10.5;

        int laterYears = myAge - 2;

        laterYears += 4;

        System.out.println(String.format("Early years %1$s \nLater years %2$s", earlyYears, laterYears));

        double myAgeInDogYears = earlyYears + laterYears;

        String myName = "Evidence".toLowerCase();

        System.out.println(String.format("My name is %1$s. I am %2$s years old in human years which is %3$s years old in dog years.", myName, myAge, myAgeInDogYears));
    }
}


