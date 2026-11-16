class Bug3 {

    public static boolean isAdmin(String username) {
        String admin = new String("admin");

        if (username == admin) {
            return true;
        }

        return false;
    }

    public static void main(String[] args) {
        String user1 = new String("admin");
        String user2 = "user";

        System.out.println(isAdmin(user1));
        System.out.println(isAdmin(user2));
    }
}