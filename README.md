# 🎓 Django Student Management CRUD

A clean, simple, and responsive **Student Management System** built with **Django Model Forms**, **Bootstrap 5**, and **SQLite**.

This project demonstrates how to build a complete **CRUD (Create, Read, Update, Delete)** application in Django using Model Forms, Django templates, URL routing, and a Bootstrap-based user interface.

---

## 🚀 Features

* ✅ Add new students
* 📋 View all students
* 👤 View individual student details
* ✏️ Update student information
* 🗑️ Delete students with confirmation
* 📝 Django Model Forms
* 🎨 Responsive Bootstrap 5 UI
* 📱 Mobile-friendly design
* 🔗 Django URL namespaces
* ⚡ Django `get_object_or_404()`
* 💾 SQLite database
* 🧩 Reusable base template
* 🧭 Responsive navbar
* 📌 Sticky bottom footer
* 🔐 CSRF protection
* ❌ 404 handling for unavailable students

---

## 🛠️ Technologies Used

| Technology            | Purpose                |
| --------------------- | ---------------------- |
| 🐍 Python             | Backend Programming    |
| 🌐 Django             | Web Framework          |
| 📝 Django Model Forms | Form Handling          |
| 🎨 Bootstrap 5        | UI & Responsive Design |
| 🗄️ SQLite            | Database               |
| 🧱 HTML5              | Page Structure         |
| 🎯 Bootstrap Icons    | UI Icons               |
| 🔀 Django URL Routing | Application Navigation |

---

## 📂 Project Structure

```text
MODELFORM_CRUD/
│
├── manage.py
│
├── MODELFORM_CRUD/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── student/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── student_form.html
│   │   ├── student_list.html
│   │   ├── student_details.html
│   │   ├── student_success_msg.html
│   │   └── student_confrim_delete.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
└── README.md
```

---

## ⚙️ CRUD Operations

### ➕ Create Student

Students can be added using a Django Model Form.

```python
form = StudentForm()

if request.method == "POST":
    form = StudentForm(request.POST)

    if form.is_valid():
        form.save()
```

---

### 📋 Read Students

All students are retrieved from the database and displayed in a responsive Bootstrap table.

```python
students = StudentData.objects.all()
```

---

### 👤 Student Details

Individual student records can be viewed using the student's primary key.

```python
student = get_object_or_404(StudentData, pk=pk)
```

---

### ✏️ Update Student

Existing student information can be updated using the same Model Form.

```python
form = StudentForm(
    request.POST,
    instance=student
)

if form.is_valid():
    form.save()
```

---

### 🗑️ Delete Student

Students can be deleted after confirmation.

```python
if request.method == "POST":
    student.delete()
    return redirect("studentform:read_students")
```

---

## 🔗 Application URLs

| URL                     | Purpose              |
| ----------------------- | -------------------- |
| `/create_students/`     | Add a new student    |
| `/read_students/`       | View all students    |
| `/student_details/<id>` | View student details |
| `/update_students/<id>` | Update student       |
| `/student_delete/<id>`  | Delete student       |

---

## 🧑‍💻 Installation & Setup

Follow the steps below to run this project locally.

### 1. Clone the repository

```bash
git clone https://github.com/szofficiall/Django-Student-Management-CRUD.git
```

### 2. Navigate into the project

```bash
cd MODELFORM_CRUD
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install Django

```bash
pip install django
```

Or, if the project contains `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 6. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## 🖥️ User Interface

The project includes:

* Modern Bootstrap navbar
* Responsive student table
* Student details page
* Add student form
* Update student form
* Delete confirmation page
* Responsive footer
* Bootstrap Icons
* Clean card-based layouts

---

## 📸 Screenshots


### 🏠 Student List

```text
<img width="1598" height="772" alt="image" src="https://github.com/user-attachments/assets/c0f674c2-3bc2-479f-83dd-f7c0413728ae" />

```

### ➕ Add Student

```text
<img width="1600" height="775" alt="image" src="https://github.com/user-attachments/assets/49de4853-2d57-45c5-9e95-a124f4d3362a" />

```

### 👤 Student Details

```text
<img width="1600" height="775" alt="image" src="https://github.com/user-attachments/assets/cfaf435c-dcf0-4945-9b65-5f9ff85922e9" />

```

### ✏️ Update Student

```text
<img width="1600" height="774" alt="image" src="https://github.com/user-attachments/assets/991109d4-2a66-49bb-9310-b65486abc7b6" />

```

### 🗑️ Delete Confirmation

```text
<img width="1597" height="768" alt="image" src="https://github.com/user-attachments/assets/0101fdd3-49a4-43b6-ab78-b337921fbf59" />

```

---

## 🎯 Learning Objectives

This project was created to practice and demonstrate:

* Django project structure
* Django applications
* Models
* Model Forms
* CRUD operations
* Django template inheritance
* URL namespaces
* Dynamic URLs
* Primary keys
* `get_object_or_404()`
* HTTP GET and POST requests
* Form validation
* Database operations
* Bootstrap integration
* Responsive UI design

---

## 🔮 Future Improvements

Possible improvements for future versions:

* 🔐 User authentication
* 👥 User-specific student records
* 🔎 Student search
* 📄 Pagination
* 🔽 Sorting and filtering
* 📊 Dashboard with student statistics
* 📧 Email functionality
* 📤 Export students to CSV/PDF
* 🌙 Dark mode
* 🖼️ Student profile images
* 🔔 Toast notifications

---

## 🧪 Development

This project is intended for learning and practice with Django CRUD applications.

It can also be extended into a complete **Student Management System** with authentication, dashboards, reporting, and advanced filtering.

---

## 👨‍💻 Developer

**Sultan Zaib**

Software Engineer | Python Developer | Django Developer

Passionate about building clean, scalable, and practical web applications using Python and Django.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

It really helps and motivates me to build more projects.

---

## 📄 License

This project is available for educational and personal use.

You are free to use, modify, and improve the code for your own learning and projects.

---

## ❤️ Built With

**Built with ❤️ by Sultan Zaib**

> Learning Django one project at a time 🚀
