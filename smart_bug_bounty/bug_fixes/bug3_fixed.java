class Bug3Fixed {
    public static boolean isAdmin(String username) {
        return "admin".equals(username);
    }

    public static void main(String[] args) {
        String user1 = new String("admin");
        String user2 = "user";
        String user3 = new String("admin");

        if (!isAdmin(user1)) {
            throw new AssertionError("Admin user was not recognized");
        }
        if (isAdmin(user2)) {
            throw new AssertionError("Regular user was recognized as admin");
        }
        if (!isAdmin(user3)) {
            throw new AssertionError("Equal String content was not recognized");
        }
        if (isAdmin(null)) {
            throw new AssertionError("Null username should not be admin");
        }
        System.out.println("All Java tests passed.");
    }
}