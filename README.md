# 💉 Vaccination Management System API

A secure, role-based RESTful API built with Django + DRF for managing vaccination campaigns, bookings, patient-doctor interactions, and campaign reviews. Features include email authentication, Cloudinary-powered profile picture uploads, JWT login, and Supabase PostgreSQL as the backend database.



## 🚀 Features

- 🧑‍⚕️ Role-based user system (Doctor / Patient)
- 🔐 JWT authentication with email confirmation (via Djoser)
- 📧 Password reset & activation via email
- 💉 Doctors manage vaccine campaigns
- 🗓 Patients can book one dose per campaign (auto-generates dose 2 date)
- ✍️ Patients can leave reviews on campaigns they booked
- 🖼 Profile picture uploads using Cloudinary
- 🧾 Swagger documentation via drf-yasg
- 🌐 Deployable to Vercel + Supabase PostgreSQL
- 📦 Static file support with WhiteNoise


## 🛠 Tech Stack

| Layer       | Tech                     |
|-------------|--------------------------|
| Backend     | Django, Django REST Framework |
| Auth        | Simple JWT, Djoser       |
| Email       | SMTP (Gmail)             |
| Media       | Cloudinary               |
| DB          | Supabase PostgreSQL      |
| Deployment  | Vercel                   |
| Docs        | drf-yasg (Swagger/OpenAPI) |
| Static      | WhiteNoise               |



## ⚙️ Setup Instructions (Local)

1. **Clone the repo**

```bash
git clone https://github.com/your-username/vaccination-system.git
cd vaccination-system

```

2.  **Create and activate virtual environment**
    

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)

```

3.  **Install dependencies**
    

```bash
pip install -r requirements.txt

```

4.  **Create `.env` or set environment variables**
    

```env
DEBUG=True
DJANGO_SECRET_KEY=your-secret
DATABASE_URL=your-supabase-db-url
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

```

5.  **Run migrations**
    

```bash
python manage.py makemigrations
python manage.py migrate

```

6.  **Create superuser (optional)**
    

```bash
python manage.py createsuperuser

```

7.  **Collect static files**
    

```bash
python manage.py collectstatic

```

8.  **Run locally**
    

```bash
python manage.py runserver

```


## 🚀 Deploy to Vercel (Backend API)

1.  Push your code to GitHub.
    
2.  Go to [vercel.com](https://vercel.com/), import project from GitHub.
    
3.  Set environment variables (same as `.env`).
    
4.  Use a `vercel.json` and top-level `wsgi.py`:
    

### `vercel.json`

```json
{
	"builds": [{
		"src": "vaccination_system/wsgi.py",
		"use": "@vercel/python",
		"config": { "maxLambdaSize": "15mb", "runtime": "python3.11.3" }
	}],
	"routes": [{
		"src": "/(.*)",
		"dest": "vaccination_system/wsgi.py"
	}]
}
```

### `wsgi.py`

```python
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vaccination_system.settings')
app = get_wsgi_application()

```



## 🔐 API Authentication

Endpoint

Description

`/auth/jwt/create/`

Login

`/auth/users/`

Register

`/auth/users/activation/`

Email activation

`/auth/users/reset_password/`

Forgot password

`/auth/users/reset_password_confirm/`

Reset confirmation

`/auth/users/me/`

Get current user



## 🧪 API Functionalities

Resource

Endpoint

Description

Campaigns

`/campaigns/`

Public list & detail

Bookings

`/bookings/`

Patient-only booking

Reviews

`/campaigns/<id>/reviews/`

Nested reviews

Profiles

`/doctor/profile/`, `/patient/profile/`

Role-specific profiles

Swagger Docs

`/swagger/`

Full API docs



## 🖼 Profile Picture Upload

-   Cloudinary is used to store images
    
-   Doctors can upload via:
    
    -   `PATCH /api/v1/doctor/profile/` with `multipart/form-data`
        
-   Images appear at `profile_picture_url`
    



## ✅ Future Improvements

-   Patient-side image upload
    
-   Admin photo previews
    
-   Role-based Swagger tags
    



## 📄 License

This project is open source and free to use for educational and non-commercial purposes.

----------

## ✨ Author

Developed by **[Dabananda Mitra](https://www.linkedin.com/in/dabananda/)**

```
Let me know if you'd like me to:
- Add a badge section (e.g., build passing, deploy preview)
- Add screenshots of the Swagger docs
- Tailor the README for academic submission (e.g., student ID, course name)
```

---

<div align="center">
<h1> Dabananda Mitra </h1>
</div>

<div align="center">
  <img src="https://res.cloudinary.com/djz3p8sux/image/upload/v1742125099/dabananda_mitra_formal_Small_1x1_o8uxit.png" width="250" height="250" style="border-radius: 50%">
</div>

<h3 align="center">Software Engineer | Problem Solver | Open Source Enthusiast</h3>

---

### 🌐 Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dabananda) [![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dabananda) [![Twitter](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/dabanandamitra) [![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.om/imdmitra/) [![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/8801304080014) [![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discordapp.com/users/dabanandamitra)

---

### 💻 Online Judge Profiles

[![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge)](https://leetcode.com/u/dabananda/) [![Codeforces](https://img.shields.io/badge/-Codeforces-1F8ACB?style=for-the-badge)](https://codeforces.com/profile/dabananda) [![CodeChef](https://img.shields.io/badge/-CodeChef-5B4638?style=for-the-badge)](https://www.codechef.com/users/dabananda) [![HackerRank](https://img.shields.io/badge/-HackerRank-00EA64?style=for-the-badge)](https://www.hackerrank.com/profile/dabananda) [![CodingNinjas](https://img.shields.io/badge/-Coding_Ninjas-FFA500?style=for-the-badge)](https://www.naukri.com/code360/profile/48a35475-0af2-4d4e-8f26-2d793b64843a) [![UVa](https://img.shields.io/badge/-UVa-00B388?style=for-the-badge)](https://uhunt.onlinejudge.org/id/1167157) [![Beecrowd](https://img.shields.io/badge/-Beecrowd-009688?style=for-the-badge)](https://judge.beecrowd.com/en/profile/467832) [![Vjudge](https://img.shields.io/badge/-Vjudge-8A2BE2?style=for-the-badge)](https://vjudge.net/user/dabanandamitra)