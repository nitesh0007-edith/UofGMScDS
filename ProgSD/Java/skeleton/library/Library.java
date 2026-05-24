package library;

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;

/**
 * PATTERN 4: MANAGER CLASS (manages multiple collections)
 * TIME: 18-22 minutes
 * MARKS: 15-18
 *
 * SKELETON for: Service, Manager, System, Controller
 *
 * KEY FEATURES:
 * - Manages multiple collections
 * - "Find best" algorithms
 * - Search and match operations
 * - Complex business logic
 */
public class Library {

    // TODO: Define collections based on exam question
    // Common patterns:
    // - List for ordered/duplicate items
    // - Set for unique items
    // - Map for quick lookup by ID/key

    private List<Book> books;              // All books in library
    private List<Member> members;          // All registered members
    private Map<String, Book> booksByIsbn; // Fast lookup by ISBN

    /**
     * Constructor - initialize all collections
     */
    public Library() {
        // IMPORTANT: Initialize ALL collections
        this.books = new ArrayList<>();
        this.members = new ArrayList<>();
        this.booksByIsbn = new HashMap<>();
    }

    /**
     * SIMPLE ADD - add item to collection
     */
    public void addBook(Book book) {
        // TODO: Add validation if needed
        if (book == null) {
            throw new IllegalArgumentException("Book cannot be null");
        }

        // Add to both collections
        books.add(book);
        booksByIsbn.put(book.getIsbn(), book);
    }

    public void addMember(Member member) {
        if (member == null) {
            throw new IllegalArgumentException("Member cannot be null");
        }
        members.add(member);
    }

    /**
     * FIND BY ID - lookup using Map for O(1) performance
     *
     * PATTERN: Use Map.get() for fast lookup
     */
    public Book findBookByIsbn(String isbn) {
        // TODO: Validate input
        if (isbn == null) {
            return null;
        }

        // Fast lookup using HashMap
        return booksByIsbn.get(isbn);
    }

    /**
     * FIND WITH CONDITION - search through collection
     *
     * PATTERN: Loop through collection, check condition, return when found
     */
    public Member findMemberById(String memberId) {
        // TODO: Search through collection
        for (Member member : members) {
            if (member.getMemberId().equals(memberId)) {
                return member;  // Found!
            }
        }

        // Not found
        return null;
    }

    /**
     * FIND ALL MATCHING - filter collection by criteria
     *
     * PATTERN: Loop, check condition, add to result list
     */
    public List<Book> findBooksByCategory(BookCategory category) {
        List<Book> result = new ArrayList<>();

        // TODO: Loop and filter
        for (Book book : books) {
            if (book.getCategory() == category) {
                result.add(book);
            }
        }

        return result;
    }

    /**
     * FIND AVAILABLE - filter by state
     */
    public List<Book> findAvailableBooks() {
        List<Book> result = new ArrayList<>();

        for (Book book : books) {
            if (book.isAvailable()) {
                result.add(book);
            }
        }

        return result;
    }

    /**
     * FIND BEST - "minimum" or "maximum" algorithm
     *
     * PATTERN: Track best so far, update when better found
     * TIME: This is the MOST IMPORTANT pattern - worth many marks!
     */
    public Book findOldestBook() {
        // TODO: Handle empty collection
        if (books.isEmpty()) {
            return null;
        }

        // Track the best found so far
        Book oldest = null;
        int minYear = Integer.MAX_VALUE;  // Start with extreme value

        // TODO: Loop through all items
        for (Book book : books) {
            // Check if this one is better
            if (book.getPublicationYear() < minYear) {
                minYear = book.getPublicationYear();
                oldest = book;
            }
        }

        return oldest;
    }

    /**
     * FIND BEST WITH CONDITIONS - filter then find minimum
     *
     * PATTERN: Nested conditions - check eligibility first, then compare
     */
    public Book findOldestAvailableBookInCategory(BookCategory category) {
        Book oldest = null;
        int minYear = Integer.MAX_VALUE;

        for (Book book : books) {
            // Check eligibility conditions first
            if (book.getCategory() == category && book.isAvailable()) {
                // Among eligible, find minimum
                if (book.getPublicationYear() < minYear) {
                    minYear = book.getPublicationYear();
                    oldest = book;
                }
            }
        }

        return oldest;
    }

    /**
     * COMPLEX OPERATION - business logic spanning multiple objects
     *
     * PATTERN: Find objects, check compatibility, perform action
     */
    public boolean borrowBook(String memberId, String isbn) {
        // STEP 1: Find the objects
        Member member = findMemberById(memberId);
        Book book = findBookByIsbn(isbn);

        // STEP 2: Validate they exist
        if (member == null) {
            throw new IllegalArgumentException("Member not found: " + memberId);
        }
        if (book == null) {
            throw new IllegalArgumentException("Book not found: " + isbn);
        }

        // STEP 3: Check business rules
        if (!book.isAvailable()) {
            return false;  // Book not available
        }

        if (!member.canBorrowMore()) {
            return false;  // Member at limit
        }

        // STEP 4: Perform the operation
        return member.borrowBook(book);
    }

    /**
     * SEARCH AND REMOVE - find item and remove it
     *
     * PATTERN: Loop through collection, find and remove when matched
     */
    public boolean removeBook(String isbn) {
        // Find the book
        Book book = findBookByIsbn(isbn);

        if (book == null) {
            return false;  // Not found
        }

        // Remove from both collections
        books.remove(book);
        booksByIsbn.remove(isbn);
        return true;
    }

    /**
     * COUNT WITH CONDITION
     */
    public int countAvailableBooks() {
        int count = 0;
        for (Book book : books) {
            if (book.isAvailable()) {
                count++;
            }
        }
        return count;
    }

    /**
     * DISPLAY ALL - print collection details
     */
    public void printAllBooks() {
        System.out.println("=== Library Books ===");
        for (int i = 0; i < books.size(); i++) {
            System.out.println((i + 1) + ". " + books.get(i));
        }
    }

    public void printAllMembers() {
        System.out.println("=== Library Members ===");
        for (int i = 0; i < members.size(); i++) {
            System.out.println((i + 1) + ". " + members.get(i));
        }
    }

    // Getters for collections (if needed)
    public List<Book> getBooks() {
        return books;
    }

    public List<Member> getMembers() {
        return members;
    }
}
