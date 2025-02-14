# My Web App

This is a simple web application that interacts with mathematical functions defined in `mathprogram.py`. The application is built using Flask and provides a user-friendly interface to perform various mathematical operations.

## Project Structure

```
my-web-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── templates
│       └── index.html
├── static
│   ├── css
│   │   └── styles.css
│   └── js
│       └── scripts.js
├── mathprogram.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd my-web-app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```
   flask run
   ```

5. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Navigate to the main page to access the mathematical functions.
- Input the required parameters and submit the form to see the results.

## Contributing

Feel free to submit issues or pull requests for improvements or additional features.