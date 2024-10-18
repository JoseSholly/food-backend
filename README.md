# Recipe API

A RESTful API for managing food recipes, allowing users to perform CRUD operations on recipes and their ingredients.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/recipe-api.git
   cd recipe-api
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Accessing Endpoints

- **List Recipes**: `GET /api/v1/recipes/`
- **Create Recipe**: `POST /api/v1/recipes/`
- **Retrieve Recipe**: `GET /api/v1/recipes/{id}/`
- **Update Recipe**: `PUT /api/v1/recipes/{id}/`
- **Delete Recipe**: `DELETE /api/v1/recipes/{id}/`
- **Search Recipes**: `GET /api/v1/recipes/search/?q={query}`

Visit `http://localhost:{port}/api/v1/` in your browser or use tools like Postman to interact with the API.