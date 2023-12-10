public class twoSum2 {
    public int[] twoSum2(int[] numbers, int target) {
        int firstPoint = 0;
        int secondPoint = numbers.length - 1;

        while (firstPoint < secondPoint) {
            if (numbers[firstPoint] + numbers[secondPoint] == target) {
                return new int[]{firstPoint + 1, secondPoint + 1};
            } else if (numbers[firstPoint] + numbers[secondPoint] < target) {
                firstPoint ++;
                continue;
            } else {
                secondPoint --;
                continue;
            }
        }

        return null;
    }
}
