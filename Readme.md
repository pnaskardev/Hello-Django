
# DevHub

The Dev Blog App is a feature-rich web application tailored specifically for developers. It combines the power of Django, a robust and scalable web framework, with HTMX, a lightweight and intuitive library for seamless integration of AJAX and HTML. The app incorporates modern web development practices, making it a valuable tool for developers who want to showcase their technical expertise and connect with like-minded individuals.
## Tech Stack

**Client:** HTMX, Bootstrap

**Server:** Django

**Database:** SQLite3

**Storage:** Amazon S3 Bucket


## Features

- **User Authentication and Authorization**: User registration and login functionality to secure the application and enable personalized experiences.

- **Blog Post Management**: Create, edit, and delete blog posts using a user-friendly editor with markdown support for writing technical content.

- **File Storage: Amazon AWS S3**: The DevHub App utilizes the Amazon AWS S3 (Simple Storage Service) to store files uploaded by users. S3 offers scalable and secure object storage with high durability and availability. By storing files on S3, the app ensures efficient handling of media assets associated with blog posts.

- **categorization of Posts**: Categorize and tag blog posts to organize and enhance discoverability.

- **Commenting and Discussion:** Enable readers to engage in discussions by allowing comments on blog posts.

- **User Profiles and Social Interactions:** User profiles to showcase developer information, including bio, profile picture, and social media links.

- **Pagination**: The list of blog posts is split into separate pages, typically containing a predefined number of posts per page, each page displays a subset of the total blog posts, reducing the initial load time and optimizing server resources.

## Run Locally

Clone the project

```bash
  git clone https://github.com/pnaskardev/StoryHub.git
```

Go to the project directory

```bash
  cd StoryHub
```

Create a python virtual environement

```bash
  python -m venv venv
```

Start the virtual environement

```bash
  venv\Scripts\activate
```

install required packages

```bash
  pip install -r requirements.txt
```

Start the Server

```bash
  python manage.py runserver
```

Access the App at 

```bash
  http://127.0.0.1:8000/
```


## Authors

- [@pnaskardev](https://www.github.com/pnaskardev)

