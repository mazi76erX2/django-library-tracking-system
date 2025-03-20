# Task

# 📚 Library Tracking System

## **📌 Assignment Overview**

Welcome to the **Library Tracking System** technical assessment.

This assessment is designed to evaluate your proficiency in: - **Python, Django, Django REST Framework (DRF), and Celery** - **API Design & Optimization** - **Asynchronous Task Handling** with Celery

You will be working within a **pre-configured Docker environment**, allowing you to focus on implementation without worrying about setup complexities.

### **🔗 Repository URL:**

https://gitlab.com/search-atlas-interviews/django-library-tracking-system

---

## **🎯 Objectives**

- **Evaluate Technical Skills**: Work with Django models, views, serializers, and DRF to create robust APIs.
- **Asynchronous Task Handling**: Integrate Celery for background task processing.
- **API Design & Optimization**: Implement RESTful API principles, pagination, and query optimization.
- **Problem-Solving Under Time Constraints**: Complete tasks efficiently within the **55-minute** timeframe.

---

## 

## **🛠 Setup Instructions**

### **1️⃣ Clone the Repository**

git clone https://gitlab.com/search-atlas-interviews/django-library-tracking-system.git

cd django-library-tracking-system

---

### **2️⃣ Start the Django Environment**

docker-compose -f docker/docker-compose.yml up --build -d

---

This will start Django, PostgreSQL, and Celery.

### **3️⃣ Access Django Admin**

- **Admin Panel:** http://localhost:8000/admin
- **API Root:** http://localhost:8000/api/

### **4️⃣ Stopping & Cleaning Up**

docker-compose -f docker/docker-compose.yml down -v

---

---

## 

## **📌 Technical Assessment**

### **⏳ Time Limit: 55 Minutes**

The assessment includes three core skill tasks and three advanced tasks, with an optional fourth task.

**Manage your time wisely** to complete all tasks within the given timeframe.

| **Task** | **Time** | **Goal** |
| --- | --- | --- |
| Python Core Skills | 5 min | Test basic Python programming |
| Enhance Book Loaning Feature | 30 min | Implement Celery tasks & extend loan functionality |
| Optimize API Performance | 15 min | Optimize database queries & implement pagination |
| Bonus: Member Activity Report | Extra | Identify top active members |

---

## 

## **1️⃣ Python Core Skills (5 min)**

📌 **Description:**

Complete the following Python tasks in the core_skills.py file.

1. **Create a list of 10 random numbers between 1 and 20.**
2. **Filter Numbers Below 10 (List Comprehension)**
3. **Filter Numbers Below 10 (Using filter)**

---

## **2️⃣ Enhance the Book Loaning Feature (30 min)**

### **Add Overdue Loan Notification**

📌 **Description:**

Implement a **Celery task** that **runs daily** to check for **overdue book loans** and sends email notifications to members.

📍 **Requirements:**

1. **Update the Loan Model:**
    - Add a due_date field with a default value set to 14 days from the loan_date.
2. **Create a Celery Periodic Task:**
    - Define a task named check_overdue_loans that executes daily.
    - The task should:
        1. Query all loans where is_returned is False and due_date is past.
        2. Send an email reminder to each member with overdue books.
3. **Apply Migrations:**
    - Make and apply the necessary database migrations to accommodate the updated model.
4. **Verify Task Execution:**
    - Test the Celery task to ensure it correctly identifies overdue loans and sends notifications.
5. **Configure Celery Beat Scheduler / Crontab (optional):**
    - Ensure that the check_overdue_loans task is scheduled to run daily using Celery Beat or Crontab.
6. **Update docker-compose.yml (optional):**
    - Add a celery-beat service to handle the periodic tasks.

### **Implement Due Date Extension Endpoint**

📌 **Description:**

Create an API endpoint that allows members to extend their loan **before it’s overdue**.

📍 **Requirements:**

1. **Add a New Action to LoanViewSet:**
    - Implement an action named extend_due_date within the LoanViewSet.
    - **Endpoint**: POST /api/loans/{loan_id}/extend_due_date/

**Payload**:

{

"additional_days": 7

}

---

1. **Endpoint Functionality:**
    - Validate that the loan is not already overdue.
    - Validate that the additional_days is a positive integer.
    - Extend the due_date by the specified number of days.
    - Return the updated loan details in the response.

**✅ Expected Outcome:**

- A functional Celery task that sends overdue notifications.
- An operational API endpoint that allows members to extend the due date of their loans, with appropriate validations and responses.

---

## **3️⃣ Optimize API Performance (15 min)**

### **Optimize Book List Endpoint**

📌 **Description:**

Enhance BookViewSet to minimize database queries **when retrieving books & authors**.

📍 **Requirements:**

1. **Optimize the ViewSet with a function:**
    - Modify the queryset in BookViewSet to use a more efficient data retrieval function.
2. **Verify Query Optimization:**
    - Use Django's debug tools or logging to ensure that the number of queries is minimized when accessing related Author data.

### **Add Pagination to Book List**

📌 **Description:**

Implement **pagination** in BookViewSet.

📍 **Requirements:**

1. **Configure DRF Pagination Settings:**
    - Update settings.py to include pagination configurations, such as setting a default page size.
2. **Ensure Pagination is Applied:**
    - Verify that the BookViewSet utilizes the configured pagination settings without additional modifications.
3. **Allow Client-Specified Page Sizes (Optional):**
    - Enable query parameters to allow clients to specify the number of items per page.

**✅ Expected Outcome:**

- An optimized BookViewSet that retrieves related author data with minimal database queries, improving API response times.
- A paginated BookViewSet that efficiently serves large numbers of book records, enhancing API usability and performance.

---

## **4️⃣ Bonus: Implement Member Activity Report Endpoint**

### **Create Top Active Members Endpoint**

📌 **Description:**

Develop an API to list the **top 5 members** with the most **active loans**.

📍 **Requirements:**

1. **Add a New Endpoint:**
    - **Endpoint**: GET /api/members/top-active/
    - **Functionality**:
        - Retrieve the top 5 members who currently have the most active loans (is_returned=False).
        - Return member details along with the count of their active loans.
2. **Ensure Efficient Querying:**
    - Use Django ORM's aggregation features (annotate, Count) to calculate the number of active loans per member.
3. **Response Format:**
    - The response should include:
        - Member ID
        - Username
        - Email
        - Number of Active Loans

📍 **Response Format:**

[

{"id": 1, "username": "JohnDoe", "active_loans": 5},

{"id": 2, "username": "JaneDoe", "active_loans": 4}

]

---

**✅ Expected Outcome:**

- A functional API endpoint that accurately identifies and returns the top 5 members based on their active loan counts.
- Efficient database queries that minimize load and response times.

---

## **📌 Submission Guidelines**

### **1️⃣ Fork the Public Repository (Before the Assessment Interview)**

- Fork this repository into your **GitHub/GitLab** account **before** the interview.
- Ensure your repository **remains public**.

### **2️⃣ Complete the Assessment**

- Implement **all required tasks**.
- Follow **best coding practices**.

### **3️⃣ Commit & Push Your Changes**

git add .

git commit -m "Completed technical assessment tasks"

git push origin main  # or your working branch

---

### **4️⃣ Submit Your Repository Link**

- Share the **public repo URL** with the **assessment coordinator**.

### **5️⃣ Final Verification**

- ✅ Ensure your repository is **public**.
- ✅ Verify that **all necessary files are included**.
- ✅ Test your code **before submission**.

---

## **📌 Additional Resources**

- **Django Documentation:** https://docs.djangoproject.com/en/4.2/
- **Django REST Framework:** https://www.django-rest-framework.org/
- **Celery Documentation:** https://docs.celeryproject.org/en/stable/
- **Docker Documentation:** https://docs.docker.com/
- **PostgreSQL Documentation:** https://www.postgresql.org/docs/

---

🚀 **Good Luck!** 🚀