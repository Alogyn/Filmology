# Filmology

Filmology is a movie recommendation web application that provides tailored movie suggestions based on user input. It leverages a combination of a content-based filtering approach and the TMDb API to deliver accurate movie details, including posters and recommendations.

## 🚀 Features

- **Tailored Recommendations**: Get movie recommendations based on similar titles.
- **Trending Movies**: Stay updated with the latest popular films.
- **Detailed Movie Insights**: Access comprehensive information about a movie, including cast, overview, and poster images.

## 🛠️ Installation

### Prerequisites

Before you can run Filmology, ensure you have the following installed:

- Python 3.x
- Flask
- Pandas
- Scikit-learn
- TMDbv3 API
- CountVectorizer (from `sklearn.feature_extraction.text`)
- TMDb API Key (available at [TMDb](https://www.themoviedb.org))

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Alogyn/filmology.git
   cd filmology
   ```

2. Install the required dependencies: If `requirements.txt` is provided, install dependencies with:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your TMDb API key:
Update the app.py file with your TMDb API key:
   ```bash
   tmdb.api_key = 'your_tmdb_api_key_here'
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the app:
Open your browser and navigate to `http://127.0.0.1:5000/`.

## 📂 Project Structure
   ```bash
.
├── dataset/
│   └── movies2.csv          # Movie dataset
├── preprocessing/
│   └── preprocessing.ipynb  # Preprocessing notebook
├── static/                  # Static assets (CSS, JS, images)
│   ├── styles/
│   ├── images/
│   └── scripts/
├── templates/               # HTML templates for Flask
│   ├── index.html           # Home page
│   ├── recommendation.html  # Recommendations page
│   └── movie_details.html   # Movie details page
├── app.py                   # Flask backend
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── .env                     # Environment variables (e.g., API keys)
  ```

## 🔍 How It Works
Filmology uses content-based filtering to recommend movies based on their metadata (genre, director, cast, etc.). The system calculates the cosine similarity between movies and returns a list of recommendations based on the user's input.

- Data Preprocessing: The preprocessing steps are outlined in the `preprocessing/preprocessing.ipynb` file.
- Recommendation Algorithm: The application uses `CountVectorizer` to process text data and calculate similarity scores using `cosine_similarity`.

## 🌐 API Integration
Filmology integrates with the TMDb [API](https://developer.themoviedb.org/reference/intro/getting-started) to fetch and display movie posters, ratings, and details.

### API Endpoints
- `/` (GET): Renders the homepage.
- `/recommendation` (POST): Provides movie recommendations based on user input.
- `/movie/<title>` (GET): Displays detailed information about a specific movie.

## 📈 Technologies Used
- Backend: Flask (Python)
- Data Processing: Pandas, Scikit-learn
- Frontend: HTML, CSS, JavaScript
- API: TMDb API for movie details

## 🎬 Demo Video

Watch the demo video of *Filmology* on YouTube:

[![Filmology Demo Video](https://img.youtube.com/vi/ULoDDD3dB70/maxresdefault.jpg)](https://www.youtube.com/watch?v=ULoDDD3dB70)

## 👨‍💻 Author
- Name: Mohamed Derfoufi
- GitHub: [Alogyn](https://github.com/Alogyn)
- Email: mohamed.derfoufi.dev@gmail.com

## 📝 License
This project is licensed under the MIT License. See the [LICENSE] file for more details.
