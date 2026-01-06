# 🍽️ Food Safety Awareness & Services Website

## 📌 Project Overview

This project is a **Food Safety Awareness and Service Request website** designed to help a food safety professional promote their services and allow clients to easily request assistance online.

The website is publicly accessible and allows users to:
- Learn about food safety services
- Request a food safety service by submitting their contact information
- Automatically notify the service provider via **email** when a request is made

The goal is to provide a **simple, professional, and free-to-access platform** that works across Florida and beyond.

---

## 🎯 Purpose of the Project

This project solves a real-world business need by:
- Giving a small business an online presence
- Automating client inquiries
- Eliminating manual follow-ups
- Providing a fast and reliable way for customers to request services

From a technical perspective, this project demonstrates:
- Full-stack web development
- API-based communication
- Python backend development
- Clean separation between frontend and backend
- Cloud-ready architecture

---

## 🧑‍💼 Who This Website Is For

### Non-Technical Users
- Food business owners
- Restaurant managers
- Event organizers
- Anyone needing food safety consultation

They can simply:
1. Visit the website
2. Click **Request Service**
3. Enter their name and phone number
4. Get contacted by the service provider

### Technical Users / Developers
- Students learning full-stack development
- Python developers learning FastAPI
- Anyone interested in building and deploying real-world web applications

---

## 🛠️ Tech Stack Overview

This project uses a **modern, lightweight, and scalable tech stack**.

### Frontend (Client Side)
- **HTML** – Website structure
- **CSS** – Styling and layout
- **JavaScript** – User interaction and API requests

The frontend:
- Displays the user interface
- Collects user input (name and phone number)
- Sends requests to the backend API

---

### Backend (Server Side)
- **Python**
- **FastAPI** – Web framework for handling API requests
- **Pydantic** – Data validation
- **SMTP (Gmail)** – Email notifications

The backend:
- Receives service requests from the frontend
- Validates the submitted data
- Sends an email notification to the service provider
- Returns success or error messages to the frontend

---

### Notifications
- **Gmail SMTP**
- Uses a secure **Gmail App Password**
- Sends a notification email whenever a service request is submitted

This keeps the system **100% free** while remaining reliable.

---

## 🏗️ Project Architecture (High-Level)

