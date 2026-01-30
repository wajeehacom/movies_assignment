class Movie:
     def __init__(
               self,
               movie_id,
               title_type,
               title,
               year,
               runtime,
               genres,
               rating,
               votes
     ):
          self.movie_id =movie_id
          self.title_type= title_type
          self.title=title
          self.year=year
          self.runtime=runtime
          self.genres=genres
          self.rating=rating
          self.votes=votes  

  
class YearReportResult:
     def __init__(
        self,
        highest_movie,
        highest_rating,
        lowest_movie,
        lowest_rating,
        average_runtime     
     ): 
        self.highest_movie=highest_movie
        self.highest_rating=highest_rating
        self.lowest_movie=lowest_movie
        self.lowest_rating=lowest_rating
        self.average_runtime = average_runtime



class GenreReportResult:
     def __init__(
               self,
               movie_count,
               average_rating
               
     ):
          self.movie_count=movie_count
          self.average_rating=average_rating
     