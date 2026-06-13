# My Pet Care App

## About

My Pet Care App is a web application designed to help pet owners organise and track essential information about their pets. It centralises medical records, weight tracking, photo galleries, and activity logs into a single platform.

The project was built to address a common challenge for pet owners: keeping health and care information accessible and well-organised over time.

---

## Key Features

### Pet Information Management
Record and manage pet details including species, breed, birth date, adoption date, microchip number, and insurance information.

### Photo Gallery
Upload and organise photos with optional titles and dates, displayed in chronological order.

### Health Trackers
- **Weight Tracker** – Log weight entries and visualise progress through graphs.
- **Vaccination Tracker** – Track vaccine names, administration dates, and next scheduled doses.
- **Deworming Tracker** – Maintain records for both internal and external deworming schedules.
- **Medication Tracker** – Manage medication schedules, including product names, next doses, and notes.

### Logs and Journals
Maintain a personal journal per pet for documenting medical visits, milestones, or observations.

### Responsive Design
Built with Bootstrap to ensure consistent presentation across desktop and mobile devices.

---

## Design Decisions

**Database Architecture** – SQLAlchemy is used as the ORM to interact with the database. Each data type (weight, vaccination, etc.) is stored in dedicated tables linked to the `Pet` model, keeping data structured and easy to query.

**User Interface** – Bootstrap provides a responsive and accessible layout. Navigation is organised through tabs for gallery, trackers, and logs, making it straightforward for users to find what they need.

**Security** – The application uses Flask-WTF for form validation and CSRF protection. Passwords are hashed before storage. File uploads are validated using `secure_filename()` to prevent unsafe filenames.

**Data Visualisation** – The weight tracker generates graphs using `matplotlib`, rendered as SVG for responsive display.

---

## Project Structure

### Core Application Files

**`app.py`** – Entry point. Initialises the Flask application by calling `init_app()` from `app_factory.py` and runs the server in debug mode when executed directly.

**`app_factory.py`** – Application factory following the Flask Factory Pattern. Responsibilities include:
- Loading environment variables via `dotenv`
- Configuring Flask settings (secret key, database URI, session management)
- Setting up the uploads folder with a 6MB file size limit
- Initialising extensions: SQLAlchemy, Flask-Migrate, Flask-Session, Flask-WTF
- Configuring Flask-Mail for email notifications
- Registering all route blueprints
- Disabling browser caching via response headers

**`extensions.py`** – Centralises extension initialisation to prevent circular imports. Initialises:
- `SQLAlchemy` – ORM for database interaction
- `Flask-Migrate` – Database schema migration management
- `Flask-WTF CSRFProtect` – CSRF attack prevention
- `Flask-Session` – Filesystem-based session management

**`models.py`** – Defines database models using SQLAlchemy: `User`, `Species`, `Breed`, `Pet`, `Photo`, `Log`, and tracker models for weight, vaccines, deworming, and medication. Each model includes relational links and serialisation methods.

**`forms.py`** – Flask-WTF form definitions for registration, authentication, pet management, logs, trackers, and photo uploads.

**`helpers.py`** – Utility functions and decorators:
- `login_required(f)` – Redirects unauthenticated users to the welcome page
- `inject_pets(f)` – Injects the current user's pets into the global `g` object for template access
- `error_message(message, code)` – Renders a custom error page based on HTTP status code
- `allowed_photo_file(filename)` – Validates image file extensions (png, jpg, jpeg, gif)
- `delete_pet_from_db(pet, db)` – Deletes a pet and all associated data (photos, logs, trackers)
- `create_weight_graph(...)` – Generates a weight progression graph using `matplotlib`, returned as an SVG

**`breeds.py`** – Contains the dictionary of valid dog and cat breeds used to populate the database during migrations.

**`requirements.txt`** – Lists all Python dependencies required to run the application.

---

### Routes

Routes are organised into separate blueprint files to maintain separation of concerns and improve readability.

**`auth_routes.py`**
- `login()` – Validates user credentials and creates a session
- `logout()` – Clears the session and redirects to the welcome page
- `register()` – Handles new user creation with email confirmation (token expires in 5 minutes)
- `restore_password()` / `reset_password()` – Email-based password recovery
- `delete_user()` – Removes the current user and all associated data

**`home_routes.py`**
- `welcome()` – Landing page for unauthenticated users
- `home()` – Dashboard displaying the user's pets

**`pet_routes.py`**
- `add_new_pet()` – Multi-step form for adding a new pet
- `edit_pet()` – Edit existing pet details
- `general_data()` – Detailed pet profile view
- `delete_pet()` – Deletes a pet and all related records
- `get_breeds()` – Returns breeds filtered by species (used via AJAX)

**`gallery_routes.py`**
- `gallery()` – Displays all photos for a pet
- `upload_photo()` – Handles photo upload with optional title and date
- `delete_photo()` – Removes a photo from the gallery

**`logs_routes.py`**
- `pet_logs()` – Lists log entries for a pet in chronological order
- `new_entry()` / `edit_entry()` – Create or modify a log entry
- `read_entry()` – Full view of a single log entry
- `delete_entry()` – Removes a log entry

**`trackers_routes.py`**
- `trackers_home()` – Displays all tracker tabs for a pet
- `add_tracker()` – Adds a new entry to a specific tracker
- `weight_graph()` – Renders the weight progression graph

---

### Templates

Located in `templates/`, each HTML file extends `layout.html` which defines the shared navigation, alert system, and footer.

| Template | Purpose |
|---|---|
| `welcome.html` | Landing page for unauthenticated users |
| `login.html` / `register.html` | Authentication forms |
| `restore_password.html` / `reset_password.html` | Password recovery forms |
| `index.html` | Pet dashboard with edit and delete options |
| `new_pet.html` / `edit_pet.html` | Pet creation and editing forms |
| `general_data.html` | Full pet profile view |
| `gallery.html` / `upload_photo.html` | Photo gallery and upload form |
| `trackers.html` / `tracker_add.html` | Tracker tabs and entry form |
| `weight_graph.html` | Weight progression graph |
| `logs.html` / `new_entry.html` / `edit_entry.html` / `entry.html` | Log management |
| `email_confirmation.html` / `password_reset_email.html` | Transactional email templates |
| `layout.html` | Base template with navbar and footer |
| `delete_confirmation_modal.html` / `pet_dropdown_menu.html` | Reusable components |
| `error.html` | Custom error page |

### Static Files

Located in `static/`:
- `css/styles.css` – Custom styles and theme variables
- `js/scripts.js` – Theme toggling, modals, and alert handling
- `images/` – Static UI images and favicon
- `uploads/` – User-uploaded pet photos

---

## Conclusion

My Pet Care App demonstrates the use of Flask with modular architecture, relational databases, user authentication, email integration, and dynamic data visualisation. The project prioritises clean code organisation, security best practices, and a professional user interface.
