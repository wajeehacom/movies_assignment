import math
from models import YearReportResult, GenreReportResult

class MovieReports:
    
    def movies_rating_by_year(self, movies, year):
 
        year_movies = [m for m in movies if m.year == year]
        if not year_movies:
         print(f"No movies foundd for year {year}")
         return None 
        highest = max(year_movies, key=lambda m: m.rating)
        lowest = min(year_movies, key=lambda m: m.rating)

        avg_runtime = (
            sum(m.runtime for m in year_movies) / len(year_movies)
        )
        return YearReportResult(
            highest_movie=highest.title,
            highest_rating=highest.rating,
            lowest_movie=lowest.title,
            lowest_rating=lowest.rating,
            average_runtime=round(avg_runtime, 2),
        )
    
    def movie_count_by_genre(self, movies, genre):
     genre_lower = genre.lower()
     genre_movies = [
        m for m in movies
        if any(g.strip().lower() == genre_lower for g in m.genres)
     ]

     if not genre_movies:
        print(f"No movies found for genre '{genre}'")
        return None

     avg_rating = sum(m.rating for m in genre_movies) / len(genre_movies)

     return GenreReportResult(
        movie_count=len(genre_movies),
        average_rating=round(avg_rating, 2)
     )
    
    def top_movies_by_votes(self, movies, year):
     year_movies = [m for m in movies if m.year == year]

     if not year_movies:
        print(f"No movies found for year {year}")
        return

     top_movies = sorted(
        year_movies,
        key=lambda m: m.votes,
        reverse=True
     )[:10]

     max_votes = top_movies[0].votes
     scale = math.ceil(max_votes / 80)

     for movie in top_movies:
        likes = math.ceil(movie.votes / scale)
        emojis = "😀" * likes
        print(f"{movie.title}")
        print(f"{emojis} {movie.votes}")




   