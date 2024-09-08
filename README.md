# easycredit-2024b

EasyCredit is a Django REST-based application designed to streamline the process of offering credit to customers for purchasing products. This platform enables businesses to provide flexible financing options, making it easier for customers to acquire desired products while managing their budget effectively.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Team Members](#team-members)
4. [License](#license)

## Installation

Ensure you have Python and pip installed on your system. Then, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/JesusGabrielCastro/easycredit-2024b.git
   cd easycredit-2024b
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

## Usage

To start the development server:

```
python manage.py runserver
```

Access the admin panel at `http://localhost:8000/admin/` (if you've created a superuser).


## Team Members

- [GABRRIEL CASTRO](https://github.com/JesusGabrielCastro) - BACKEND DEVELOPER
- [DIEGO ESPINOZA](https://github.com/DiegoMauricioEspinozaFernandez) - BACKEND DEVELOPER
- [JULIAN ASCANIO](https://github.com/JulianAscanio) - BACKEND DEVELOPER

## License

This project is licensed under the [Apache-2.0 license]. See the `LICENSE` file for details.