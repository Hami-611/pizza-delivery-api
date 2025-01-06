
# 🍕 Pizza Delivery API

This is a RESTful API for a Pizza Delivery Service built using **Django Rest Framweork**. The API allows users and admins to manage orders, track their statuses, and interact with the system for learning purposes.  

## 📚 Routes to Implement

| **Method** | **Route**                              | **Functionality**         | **Access**   |
|------------|----------------------------------------|---------------------------|--------------|
| **POST**   | `/auth/signup/`                        | Register a new user       | All users    |
| **POST**   | `/auth/login/`                         | Login user                | All users    |
| **POST**   | `/orders/`                             | Place an order            | All users    |
| **PUT**    | `/orders/order/update/{order_id}/`     | Update an order           | All users    |
| **PUT**    | `/orders/order/status/{order_id}/`     | Update order status       | Superuser    |
| **DELETE** | `/orders/order/delete/{order_id}/`     | Delete/Remove an order    | All users    |
| **GET**    | `/orders/user/orders/`                | Get user’s orders         | All users    |
| **GET**    | `/orders/`                             | List all orders made      | Superuser    |
| **GET**    | `/orders/{order_id}/`                  | Retrieve an order         | Superuser    |
| **GET**    | `/orders/user/order/{order_id}/`       | Get user’s specific order | All users    |
| **GET**    | `/docs/`                               | View API documentation    | All users    |

## 🚀 How to Run the Project

### Prerequisites

Ensure you have the following installed on your machine:
- [Python 3.8+](https://www.python.org/downloads/)

### Steps to Set Up the Project

1. Clone the project:
   ```bash
   git clone https://github.com/Hami-611/pizza-delivery-api.git
   cd pizza-delivery-api
   ```

2. Create a virtual environment:
   - Using `virtualenv`:
     ```bash
     python -m venv env
     source env/bin/activate  # On Windows, use `env\Scripts\activate`
     ```
   - Or using `pipenv`:
     ```bash
     pip install pipenv
     pipenv shell
     ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the PostgreSQL database:
   - Open the `database.py` file and set the PostgreSQL connection string:
     ```python
     engine = create_engine('postgresql://<username>:<password>@localhost/<db_name>', echo=True)
     ```
   - Replace `<username>`, `<password>`, and `<db_name>` with your database credentials.

5. Initialize the database:
   ```bash
   python init_db.py
   ```

## 🛠️ Future Enhancements

1. **Authentication Features**:  
   Add support for token-based authentication using JWT.
   
2. **Order History**:  
   Implement order history filtering and sorting options.
   
3. **Role-Based Access**:  
   Refine access controls for admin and user roles.

4. **Testing**:  
   Add unit tests and integration tests using `pytest`.

5. **Deployment**:  
   Containerize the application using Docker and deploy to platforms like AWS or Heroku.

