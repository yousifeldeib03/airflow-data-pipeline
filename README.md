# Airflow Email Pipeline 🚀

## 📖 Overview

This project implements an automated data pipeline using Apache Airflow and Docker.
The pipeline performs two main tasks sequentially:

- Sending automated emails using Gmail SMTP
- Writing a list of names to a shared output file

---

## 🏗️ Architecture

1. Docker Compose (runs all services)
2. Apache Airflow (orchestrates the pipeline)
3. PostgreSQL (Airflow metadata database)
4. Gmail SMTP (email delivery)
5. Shared Volume (file output)

---

## ⚙️ Pipeline Tasks

### 🔹 Task 1 – Send Email
- Uses Airflow's `EmailOperator`
- Sends an automated email via Gmail SMTP
- Destination: `yousif.eldeib@ejust.edu.eg`

### 🔹 Task 2 – Write Names to File
- Uses Airflow's `PythonOperator`
- Writes a list of names to `shared/output.txt`

---

## 🔁 DAG Flow

```
send_email → write_names_to_file
```

---

## 📸 Screenshots

### 🟢 DAG Graph (both tasks success)
![DAG Graph](photos/dag_graph.png)

### 🟢 DAGs List
![DAGs List](photos/dag_list.png)

### 🟢 Email Result
![Email received](photos/email.png)

---

## ✅ Results

- Automated email sent successfully via Gmail SMTP
- Names written successfully to `shared/output.txt`
- Both tasks completed with status: **success**

---

## 📂 Output

After Dag2 runs, `shared/output.txt` contains:

```
Gamal
Menna
Ahmed
Omar
Hossam
```

---

## 🗂️ Project Structure

```
airflow/
├── dags/
│   ├── dag1.py
│   └── dag2.py
├── shared/
│   └── output.txt
├── photos/
│   ├── dag_graph.png
│   ├── dag_list.png
│   └── email.png
├── depi.yaml
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📌 Notes

- Use Gmail App Password not your regular Gmail password
- SMTP credentials must be added to both `airflow-webserver` and `airflow-scheduler`
- Shared folder maps to `/data` inside the container
