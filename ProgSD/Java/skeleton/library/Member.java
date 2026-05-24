package library;

import java.util.Objects;
import java.util.ArrayList;
import java.util.List;

/**
 * PATTERN 3: DATA CLASS with COLLECTION (one-to-many relationship)
 * TIME: 15-18 minutes
 * MARKS: 12
 *
 * SKELETON for: Customer, User, Player, Person with items
 *
 * KEY DIFFERENCE from simple data class:
 * - Contains a collection (List, Set, Map)
 * - Methods to add/remove from collection
 * - May have business logic (limits, validation)
 */
public class Member {

    // Simple fields
    private String memberId;
    private String name;
    private int maxBorrowLimit;

    // COLLECTION field - represents "has many" relationship
    // TODO: Choose collection type based on requirements:
    // - List<Book> if order matters or duplicates allowed
    // - Set<Book> if no duplicates and order doesn't matter
    // - Map<String, Book> if need quick lookup by key
    private List<Book> borrowedBooks;

    /**
     * Constructor
     */
    public Member(String memberId, String name, int maxBorrowLimit) {
        // TODO: Validate simple fields
        if (memberId == null || memberId.length() < 3) {
            throw new IllegalArgumentException("Member ID must be at least 3 characters");
        }

        if (name == null || name.length() < 2) {
            throw new IllegalArgumentException("Name must be at least 2 characters");
        }

        if (maxBorrowLimit < 1 || maxBorrowLimit > 10) {
            throw new IllegalArgumentException("Borrow limit must be between 1 and 10");
        }

        this.memberId = memberId;
        this.name = name;
        this.maxBorrowLimit = maxBorrowLimit;

        // IMPORTANT: Initialize collection in constructor!
        this.borrowedBooks = new ArrayList<>();
    }

    // Basic getters
    public String getMemberId() {
        return memberId;
    }

    public String getName() {
        return name;
    }

    public int getMaxBorrowLimit() {
        return maxBorrowLimit;
    }

    public List<Book> getBorrowedBooks() {
        return borrowedBooks;
    }

    /**
     * COLLECTION METHOD: Add item to collection
     *
     * PATTERN: Check business rules before adding
     * - Check null
     * - Check not already present (if duplicates not allowed)
     * - Check limits/capacity
     * - Check compatibility/validity
     */
    public boolean borrowBook(Book book) {
        // TODO: Validate input
        if (book == null) {
            throw new IllegalArgumentException("Book cannot be null");
        }

        // TODO: Check business rule 1 - not already borrowed
        if (borrowedBooks.contains(book)) {
            return false;  // Already borrowed
        }

        // TODO: Check business rule 2 - limit not exceeded
        if (borrowedBooks.size() >= maxBorrowLimit) {
            return false;  // Limit reached
        }

        // TODO: Check business rule 3 - book is available
        if (!book.isAvailable()) {
            return false;  // Book not available
        }

        // All checks passed - add to collection
        borrowedBooks.add(book);
        book.setAvailable(false);  // Update book state
        return true;
    }

    /**
     * COLLECTION METHOD: Remove item from collection
     *
     * PATTERN: Search and remove, handle not found case
     */
    public boolean returnBook(Book book) {
        // TODO: Validate input
        if (book == null) {
            throw new IllegalArgumentException("Book cannot be null");
        }

        // TODO: Try to remove from collection
        if (borrowedBooks.remove(book)) {
            // Successfully removed
            book.setAvailable(true);  // Update book state
            return true;
        }

        // Not found in collection
        return false;
    }

    /**
     * QUERY METHOD: Get information about collection
     */
    public int getBorrowedCount() {
        return borrowedBooks.size();
    }

    public boolean canBorrowMore() {
        return borrowedBooks.size() < maxBorrowLimit;
    }

    @Override
    public String toString() {
        return "Member{id='" + memberId + "', name='" + name +
               "', borrowed=" + borrowedBooks.size() + "/" + maxBorrowLimit + "}";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Member member = (Member) o;
        return Objects.equals(memberId, member.memberId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(memberId);
    }
}
