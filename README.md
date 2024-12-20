
# Book Review Application

A full-stack book review application built using Django REST Framework (DRF). This application allows users to sign up, log in, publish their own books, and leave reviews/comments on books published by other users. The application ensures secure endpoints with JWT-based authentication and proper permissions.

## Features

### 1. User Authentication and Authorization
- User sign-up and login functionality with Django REST Framework.
- JWT (JSON Web Token) authentication for securing endpoints.
- Only authenticated users can perform specific actions like publishing books or posting reviews.

### 2. Book Management
- **Publish a Book**: Authenticated users can publish books with details such as title, author, description, and cover image.
- **List All Books**: View all books published by users.
- **Retrieve a Specific Book**: Retrieve details of a book using its unique ID.
- **Update a Book**: Users can edit the details of the books they've published.
- **Delete a Book**: Users can delete books they've published.

### 3. Review and Comment System
- **Post a Review/Comment**: Users can post reviews/comments on books published by other users.
- **List Reviews for a Book**: Retrieve all reviews for a specific book.
- **Edit a Review/Comment**: Users can edit their own reviews/comments.
- **Delete a Review/Comment**: Users can delete their own reviews/comments.

### 4. Constraints and Rules
- Users can only comment on books published by others.
- Only the user who posted a review/comment can edit or delete it.
- Proper error handling for unauthorized actions (e.g., editing someone else’s comment).

### 5. Pagination
- Pagination implemented for listing books and reviews to handle large datasets efficiently.

## Technologies Used
- **Backend**: Django, Django REST Framework
- **Authentication**: JWT (JSON Web Token)
- **Database**: SQLite (can be replaced with PostgreSQL/MySQL)
- **Storage**: Local storage for cover images (can be extended to use cloud services like AWS S3)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/minahil57/Book-Management-Application-Using-Django.git
   cd book-review-app
