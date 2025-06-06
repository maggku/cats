# Testing

## Overview
This project includes both automated and manual testing to ensure all user stories and acceptance criteria are met.

## Automated Tests
- **Framework**: Django's built-in testing framework
- **Location**: `tests.py` files in each app
- **Coverage**: Models, views, forms, and URL routing

### Running Automated Tests
```bash
python manage.py test

````

# Test Coverage

User authentication and registration
Post creation, editing, and deletion
Comment functionality and approval system
URL routing and view responses

## Manual Testing
User Story Testing
Each user story has been manually tested against its acceptance criteria:
1. Open a Post
User Story: As a Site User, I can click on a post so that I can read the full text.

AC1: When a blog post title is clicked on a detailed view of the post is seen.
Test Result:  Pass - Clicking post title opens detailed view

2. View Comments
User Story: As a Site User/Admin I can view comments on an individual post so that I can read the conversation.

AC1: Given one or more user comments the admin can view them.
AC2: Then a site user can click on the comment thread to read the conversation.
Test Result:  Pass - Comments display correctly for both users and admins

3. Account Registration
User Story: As a Site User I can register an account so that I can comment on a post.

AC1: Given an email a user can register an account.
AC2: Then the user can log in.
AC3: When the user is logged in they can comment.
Test Result:  Pass - Registration, login, and commenting workflow functions correctly

Responsive Testing
Tested on various screen sizes:

Mobile (320px-768px)
Tablet (768px-1024px)
Desktop (1024px+)
