
# Flask Patient Data Management

This project is a web application using Flask integrated with an SQLite database. It allows users to view their patient data and check if it's present in the system. If the data is not available, the app will prompt the user to input their details.

## Requirements

- Python 3.7 or higher
- Flask
- SQLite

## Installation

1. Install the dependencies using pip
   

2. Make sure the SQLite database is created correctly.

## How to Use

1. Run the application with the following command:
    ```bash
    python app.py
    ```

2. Upon opening the app, the user will be prompted to check if their data exists in the database. If the data is found, it will be displayed. If not, the user will be asked to enter their data.

## Project Structure

- `app.py`: Contains the main application logic.
- `Patients.db`: Contains database.
- `templates/`: Folder containing HTML files for the user interface.


## Notes

- This project uses a simple SQLite database to store patient data.
- You can modify the database and the interface to meet the needs of your application.

## Contributions

If you'd like to improve the project or add new features, feel free to open an issue or submit a pull request.

## License

Open source project under the MIT license.
