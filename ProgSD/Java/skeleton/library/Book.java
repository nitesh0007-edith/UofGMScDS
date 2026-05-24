package library;

import java.util.Objects;

/**
 * PATTERN 2: DATA CLASS with validation and identity
 * TIME: 12-15 minutes
 * MARKS: 10
 *
 * SKELETON for: Book, Item, Product, Resource, etc.
 *
 * KEY COMPONENTS:
 * - Fields with validation constraints
 * - Constructor with validation
 * - Getters (always needed)
 * - Setters (with validation!)
 * - toString() for display
 * - equals() and hashCode() for identity
 */
public class Book {

    // TODO: Define fields based on exam question
    // Common fields: id, name, category, price, etc.
    private String isbn;          // Unique identifier
    private String title;         // Name/description
    private BookCategory category; // Type/category (use enum)
    private int publicationYear;  // Numeric property
    private boolean isAvailable;  // State flag

    /**
     * Constructor with FULL VALIDATION
     *
     * VALIDATION CHECKLIST:
     * - Check null for objects
     * - Check length/range for strings/numbers
     * - Check enum values are valid
     * - Check related field constraints (min <= max)
     */
    public Book(String isbn, String title, BookCategory category, int publicationYear) {
        // TODO: Validate isbn
        // Pattern: if (isbn == null || isbn.length() < X) throw exception
        if (isbn == null || isbn.length() < 5) {
            throw new IllegalArgumentException("ISBN must be at least 5 characters");
        }

        // TODO: Validate title
        // Pattern: Check null AND minimum length
        if (title == null || title.length() < 1) {
            throw new IllegalArgumentException("Title cannot be empty");
        }

        // TODO: Validate enum
        // Pattern: Check not null
        if (category == null) {
            throw new IllegalArgumentException("Category cannot be null");
        }

        // TODO: Validate year
        // Pattern: Check range (min <= value <= max)
        if (publicationYear < 1000 || publicationYear > 2025) {
            throw new IllegalArgumentException("Invalid publication year");
        }

        // Assign validated values
        this.isbn = isbn;
        this.title = title;
        this.category = category;
        this.publicationYear = publicationYear;
        this.isAvailable = true;  // Default state
    }

    // GETTERS - Always needed for private fields
    public String getIsbn() {
        return isbn;
    }

    public String getTitle() {
        return title;
    }

    public BookCategory getCategory() {
        return category;
    }

    public int getPublicationYear() {
        return publicationYear;
    }

    public boolean isAvailable() {
        return isAvailable;
    }

    // SETTERS - Only if exam requires "modifiable" fields
    // IMPORTANT: Must validate just like constructor!

    public void setTitle(String title) {
        // TODO: Copy validation from constructor
        if (title == null || title.length() < 1) {
            throw new IllegalArgumentException("Title cannot be empty");
        }
        this.title = title;
    }

    public void setAvailable(boolean available) {
        this.isAvailable = available;
    }

    // TODO: Add more setters if needed (validate each one!)

    /**
     * toString() - For display/printing
     *
     * PATTERN: "ClassName{field1=value1, field2=value2, ...}"
     */
    @Override
    public String toString() {
        // TODO: Include relevant fields for display
        return "Book{isbn='" + isbn + "', title='" + title +
               "', category=" + category + ", year=" + publicationYear +
               ", available=" + isAvailable + "}";
    }

    /**
     * equals() - For object comparison
     *
     * PATTERN: Compare by unique identifier(s)
     * RULE: Use SAME fields as hashCode()!
     */
    @Override
    public boolean equals(Object o) {
        // Check if same object
        if (this == o) return true;

        // Check if null or different class
        if (o == null || getClass() != o.getClass()) return false;

        // Cast and compare
        Book book = (Book) o;

        // TODO: Compare by unique identifier (usually one field like ID/ISBN)
        return Objects.equals(isbn, book.isbn);
    }

    /**
     * hashCode() - Required when overriding equals()
     *
     * PATTERN: Hash the SAME fields used in equals()
     */
    @Override
    public int hashCode() {
        // TODO: Use same fields as equals()
        return Objects.hash(isbn);
    }
}
