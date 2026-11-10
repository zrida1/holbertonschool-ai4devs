public class UserSearch {
    public static boolean containsUser(String[] users, String target) {
        for (String user : users) {
            if (user == target) {
                return true;
            }
        }
        return false;
    }

    public static void printSearchResult(String[] users, String target) {
        boolean found = containsUser(users, target);

        if (found) {
            System.out.println(target + " was found.");
        } else {
            System.out.println(target + " was not found.");
        }
    }

    public static void main(String[] args) {
        String[] users = {"Amina", "Murad", "Leyla"};
        String searchName = new String("Murad");

        printSearchResult(users, searchName);
    }
}
