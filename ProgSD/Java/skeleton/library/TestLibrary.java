package library;

/**
 * Test class for Library Management System
 *
 * This demonstrates all the patterns and features
 * Use this as a template for testing your exam solution!
 */
public class TestLibrary {

    public static void main(String[] args) {
        System.out.println("=== Library Management System Test ===\n");

        // Create library
        Library library = new Library();

        // TEST 1: Create books
        System.out.println("1. Creating books...");
        Book book1 = new Book("ISBN001", "Java Programming", BookCategory.SCIENCE, 2020);
        Book book2 = new Book("ISBN002", "The Great Novel", BookCategory.FICTION, 2018);
        Book book3 = new Book("ISBN003", "World History", BookCategory.HISTORY, 2015);
        Book book4 = new Book("ISBN004", "Python Basics", BookCategory.SCIENCE, 2022);
        Book book5 = new Book("ISBN005", "Mystery Story", BookCategory.FICTION, 2019);

        // Add books to library
        library.addBook(book1);
        library.addBook(book2);
        library.addBook(book3);
        library.addBook(book4);
        library.addBook(book5);
        System.out.println("✓ Added 5 books to library\n");

        // TEST 2: Create members
        System.out.println("2. Creating members...");
        Member member1 = new Member("M001", "Alice", 3);
        Member member2 = new Member("M002", "Bob", 5);

        library.addMember(member1);
        library.addMember(member2);
        System.out.println("✓ Added 2 members\n");

        // TEST 3: Display all books
        System.out.println("3. All books in library:");
        library.printAllBooks();
        System.out.println();

        // TEST 4: Display all members
        System.out.println("4. All library members:");
        library.printAllMembers();
        System.out.println();

        // TEST 5: Find book by ISBN (fast Map lookup)
        System.out.println("5. Finding book by ISBN...");
        Book found = library.findBookByIsbn("ISBN003");
        if (found != null) {
            System.out.println("✓ Found: " + found);
        }
        System.out.println();

        // TEST 6: Find books by category
        System.out.println("6. Finding all SCIENCE books...");
        for (Book book : library.findBooksByCategory(BookCategory.SCIENCE)) {
            System.out.println("  - " + book);
        }
        System.out.println();

        // TEST 7: Find available books
        System.out.println("7. Available books:");
        System.out.println("Available count: " + library.findAvailableBooks().size());
        System.out.println();

        // TEST 8: Borrow books (member borrows from library)
        System.out.println("8. Testing borrow operation...");
        boolean success1 = library.borrowBook("M001", "ISBN001");
        boolean success2 = library.borrowBook("M001", "ISBN002");
        boolean success3 = library.borrowBook("M002", "ISBN003");

        System.out.println("Alice borrows Java book: " + (success1 ? "✓ Success" : "✗ Failed"));
        System.out.println("Alice borrows Novel: " + (success2 ? "✓ Success" : "✗ Failed"));
        System.out.println("Bob borrows History book: " + (success3 ? "✓ Success" : "✗ Failed"));
        System.out.println();

        // TEST 9: Check member borrowed books
        System.out.println("9. Member borrowed books:");
        System.out.println("Alice has borrowed: " + member1.getBorrowedCount() + " books");
        System.out.println("Bob has borrowed: " + member2.getBorrowedCount() + " books");
        System.out.println();

        // TEST 10: Try to borrow unavailable book (should fail)
        System.out.println("10. Testing borrow unavailable book...");
        boolean failTest = library.borrowBook("M002", "ISBN001");
        System.out.println("Bob tries to borrow Alice's book: " + (failTest ? "✗ Unexpected success" : "✓ Correctly failed"));
        System.out.println();

        // TEST 11: Find oldest book
        System.out.println("11. Finding oldest book...");
        Book oldest = library.findOldestBook();
        if (oldest != null) {
            System.out.println("Oldest book: " + oldest.getTitle() + " (" + oldest.getPublicationYear() + ")");
        }
        System.out.println();

        // TEST 12: Find oldest available book in category
        System.out.println("12. Finding oldest available FICTION book...");
        Book oldestFiction = library.findOldestAvailableBookInCategory(BookCategory.FICTION);
        if (oldestFiction != null) {
            System.out.println("Found: " + oldestFiction.getTitle() + " (" + oldestFiction.getPublicationYear() + ")");
        }
        System.out.println();

        // TEST 13: Count available books
        System.out.println("13. Counting available books...");
        int available = library.countAvailableBooks();
        System.out.println("Available books: " + available + " out of " + library.getBooks().size());
        System.out.println();

        // TEST 14: Test member borrow limit
        System.out.println("14. Testing borrow limit...");
        System.out.println("Alice's limit: " + member1.getMaxBorrowLimit());
        System.out.println("Alice can borrow more: " + member1.canBorrowMore());
        System.out.println();

        // TEST 15: Return book
        System.out.println("15. Testing return operation...");
        boolean returned = member1.returnBook(book1);
        System.out.println("Alice returns Java book: " + (returned ? "✓ Success" : "✗ Failed"));
        System.out.println("Alice now has: " + member1.getBorrowedCount() + " books");
        System.out.println("Book is now available: " + book1.isAvailable());
        System.out.println();

        // TEST 16: Test validation (exception handling)
        System.out.println("16. Testing validation...");
        try {
            Book invalidBook = new Book("AB", "Short ISBN", BookCategory.FICTION, 2020);
            System.out.println("✗ Should have thrown exception!");
        } catch (IllegalArgumentException e) {
            System.out.println("✓ Correctly rejected invalid ISBN: " + e.getMessage());
        }

        try {
            Member invalidMember = new Member("M003", "X", 3);
            System.out.println("✗ Should have thrown exception!");
        } catch (IllegalArgumentException e) {
            System.out.println("✓ Correctly rejected short name: " + e.getMessage());
        }
        System.out.println();

        // TEST 17: Test equals and hashCode
        System.out.println("17. Testing equals and hashCode...");
        Book book1Copy = new Book("ISBN001", "Different Title", BookCategory.HISTORY, 1999);
        System.out.println("book1.equals(book1Copy): " + book1.equals(book1Copy) + " (same ISBN)");
        System.out.println("book1.hashCode() == book1Copy.hashCode(): " +
                          (book1.hashCode() == book1Copy.hashCode()));
        System.out.println();

        // FINAL: Display final state
        System.out.println("=== FINAL STATE ===");
        library.printAllBooks();
        System.out.println();
        library.printAllMembers();

        System.out.println("\n✓ All tests completed successfully!");
    }
}
