import csv
from models import Movie
from dotenv import load_dotenv
import os
class MovieCSVParser:
    def __init__(self):
        load_dotenv()
        self.file_path =os.getenv("MOVIES_CSV_PATH")
        if not self.file_path:
            raise EnvironmentError("MOVIES_CSV_PATH nott found in env file")

    
    def parse(self):
        movies=[]
        with open(self.file_path,encoding="utf-8") as file:
            reader= csv.DictReader(file)
            for row in reader:
                try:
                    year= int(row["startYear"])
                    rating= float(row["rating"])
                    votes= int(row["numVotes"])

                    runtime=(
                        0 if row["runtimeMinutes"]=="\\N"
                        else int(row["runtimeMinutes"])
                    )
                
                    genres=row["genres"].split(",")
                    movie=Movie(
                        movie_id=row["id"],
                        title_type=row["titleType"],
                        title=row["originalTitle"],
                        year=year,
                        runtime=runtime,
                        genres=genres,
                        rating=rating,
                        votes=votes
                    )
                    movies.append(movie)
                except(ValueError,KeyError):
                    continue

        return movies


 
        

