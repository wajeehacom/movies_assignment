
import argparse
from csv_parser import MovieCSVParser
from reports import MovieReports

def main():

    
    arg_parser=argparse.ArgumentParser(
        description="Movies Report Generator "
    )
    arg_parser.add_argument(
        "-r","--year",type=int,help="Report by Year"
    )
    arg_parser.add_argument(
        "-g","--genre",type=str,help="Report by genre"
    )
    arg_parser.add_argument(
        "-v","--votes",type=int,help="Top Voted movies BY year"
    )
   
    args=arg_parser.parse_args()
    if not args.year and not args.genre and not args.votes:
        arg_parser.error("at least one report option is required")
    parser=MovieCSVParser()
    movies=parser.parse()
    reports=MovieReports()

    if args.year:
       result = reports.movies_rating_by_year(movies, args.year)
       if result is not None:
         print(f"Highest Rating: {result.highest_rating} - {result.highest_movie}")
         print(f"Lowest Rating: {result.lowest_rating} - {result.lowest_movie}")
         print(f"Average mean minutes: {result.average_runtime}")
       else:
         print(f"No movies found for year {args.year}")
    
    if args.genre:
        result=reports.movie_count_by_genre(movies,args.genre)
        print(f"Movies found:{result.movie_count}")
        print( f" Average mean rating:{result.average_rating}"
        )
    if args.votes:
        reports.top_movies_by_votes(movies,args.votes) 

if __name__=="__main__":
     main()


