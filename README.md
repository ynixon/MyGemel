# Best Investment Suggester

## Overview

The Best Investment Suggester is a Streamlit app that provides users with the best investment options across different categories. The app fetches data from [MyGemel.net](https://www.mygemel.net/קופת-גמל-להשקעה), processes it, and presents a summary table of the investment options with the highest potential returns.

## Features

- Displays the best investment options across various categories.
- Shows the 1-year, 3-year, and 5-year Return on Investment (ROI) for each option.
- Calculates the total ROI for each option based on the mentioned periods.
- Provides a link to the original webpage as the data source.

## Try It Online

Access the Best Investment Suggester app online: [https://mygemel.streamlit.app/](https://mygemel.streamlit.app/)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ynixon/MyGemel.git
   cd MyGemel
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the app:
   ```sh
   streamlit run app.py
   ```

## Usage

1. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).

2. The app interface will display the best investment options sorted by total ROI. The summary table provides insights into investment opportunities across different categories.

3. Click on the source link to access the original webpage for more details.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The app fetches data from [MyGemel.net](https://www.mygemel.net/קופת-גמל-להשקעה).
- The data is processed and presented using the [Streamlit](https://www.streamlit.io/) library.

