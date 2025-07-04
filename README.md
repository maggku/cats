# Cat Talk 

Cat Talk is a responsive Django-based blog application developed on the base of a Code Institute tutorial project 3. Designed for cat lovers and curious pet owners, the site explores feline communication in a humorous yet engaging format. Users can register, browse blog posts, and submit comments—moderated through Django’s admin interface by a superuser. Built with Django's built-in authentication and admin tools, the project emphasizes secure interaction and content control. The site includes a mobile-friendly dropdown navigation menu to ensure usability across devices. While light-hearted in theme, Cat Talk demonstrates core web development principles and content management using an industry-standard framework.
Cat Talk bridges the communication gap between cats and their human companions through accessible, engaging content about feline behavior and body language. The platform serves both educational and community purposes, providing users with practical insights into cat communication while fostering a community of cat enthusiasts who can share experiences and learn from expert-curated content.
Value Proposition
### For Cat Owners:

Access to expert-curated content about feline behavior and communication patterns
Community-driven discussion through moderated commenting system
Mobile-responsive design enabling access to information anytime, anywhere

### For the Pet Care Community:

Centralized resource for understanding common cat behaviors
User-generated content and discussions that expand the knowledge base
Professional content moderation ensuring quality and reliability

## Key Components

### 1. User Authentication
- User registration and login/logout functionality.
- Comments are restricted to authenticated users.
- Admin-only moderation of comments via Django Admin.

### 2. Blog Functionality
- Blog post model with title, content, date, and author.
- Posts displayed on homepage and individual detail pages.
- Posts authored and managed via Django Admin.

### 3. Comment System
- Authenticated users can submit comments on posts.
- Comments are held for moderation and must be approved by the superuser.
- Comment form included on each post detail page.

### 4. Responsive Design
- Mobile-first design using responsive templates.
- Dropdown navigation menu for mobile view.
- Clean, user-friendly interface styled for readability.

### 5. Django Admin Integration
- Full content management (posts and comments) through Django Admin.
- Admin can approve or delete comments and create blog posts.

### 6. Template Structure
- Reusable templates using Django’s templating language.
- Base template includes navigation bar and footer.

### 7. Model Structure
- Custom models for blog posts and comments.
- Relational structure: each comment is tied to a specific post and user.


---

## Table of Contents

1. [Technologies Used](#technologies-used)
2. [Final View](#final-view)
3. [User Stories, Code Validation and  Testing](#user-stories-code-validation-and-testing)
4. [Deployment](#deployment)
5. [Acknowledgments](#acknowledgments)

---

## Technologies Used

- **Python** – Core programming language used for backend development.
- **Django 3.x / 4.x** – High-level Python web framework used to build the blog application.
- **HTML5** – Structure and markup for web pages.
- **CSS3** – Styling for the front-end layout and responsive design.
- **Bootstrap 5** – Used for responsive design and mobile-friendly dropdown navigation.
- **Django Templating Language (DTL)** – For rendering dynamic content in HTML pages.
- **SQLite3** – Default development database used with Django, used for testing.
- **PostgreSQL** – Main production database.
- **Django Admin** – Built-in admin panel used for managing posts and moderating comments.
- **Git & GitHub** – Version control and remote code repository.
- **Heroku** – Cloud platform used for deploying the live application.

---

### Key Design Choices:
1. **Minimalist Layout**: Focus on functionality with clean, modern aesthetics.
2. **Responsive Design**: Works seamlessly across devices (mobile, tablet, desktop).
3. **Color Palette**: Vibrant colors inspired by popular cryptocurrency themes.

---

## Final View

- [Final View](doc/final_view/final_view.md)


---

## User Stories, Code Validation and Testing

- [View Detailed Testing Report](doc/tests/tests.md)

### Key user stories include:
1. As a Site User I can register an account so that I can comment on a post.
2. As a Site User I can leave comments on a post so that I can be involved in the conversation
3. As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments

### Summary of Tests:
1. **Functional Testing**: Verified accurate currency conversion calculations.
2. **Responsiveness Testing**: Ensured compatibility across multiple devices and browsers.
3. **User Experience Testing**: Collected feedback for UI/UX improvements.

---

## Deployment

- [View Deployment Instructions](doc/deployment/deployment.md)

### Steps Taken:
1. Hosted the project on **Heroku**.
2. Configured the repository for static site deployment.
3. Verified live functionality after deployment.

Live site: [Cat Talk](https://testingtesting-51bfafd102d0.herokuapp.com/)

---

## Acknowledgments

- Resources and tutorials for Project 3 from the [Code Institute](https://codeinstitute.net/global/)

