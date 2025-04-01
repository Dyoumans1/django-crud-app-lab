from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# views.py

class Movie:
    def __init__(self, name, director, genre, description, year):
        self.name = name
        self.director = director
        self.breed = genre
        self.description = description
        self.age = year


movies = [
    Movie(
        'Monty Python And The Holy Grail', 
        'Terry Gilliam',
        'Comedy', 
        'Monty Python and the Holy Grail is a quirky, comedic take on the legend of King Arthur and his knights as they embark on a quest to find the Holy Grail. Filled with absurd humor, memorable characters, and iconic scenes, it blends medieval adventure with surreal and satirical comedy.',
        1975
    ),

    Movie(
        'STAND BY ME',
        'Rob Reiner', 
        'Adventure', 
        'Stand by Me is a heartfelt coming-of-age film about four boys who embark on a journey to find the body of a missing child. Set in the 1950s, the film explores friendship, loss, and growing up, as the boys face both physical and emotional challenges along the way.',
        1986
    ),

    Movie(
        'HOT ROD',
        'Akiva Schaffer',
        'Comedy',
        'Hot Rod is a quirky comedy about an aspiring stuntman, Rod Kimble, who dreams of proving himself by performing an epic jump to raise money for his stepfather’s surgery. With over-the-top stunts, absurd humor, and a lovable cast, the film delivers a mix of heart and hilarity.',
        2007
    ),

    Movie(
        'A Knight\'s Tale',
        'Brian Helgeland',
        'Adventure',
        'A Knight\'s Tale is a fun, action-packed film about a peasant named William who poses as a knight to compete in jousting tournaments. With modern rock music and an adventurous spirit, the movie blends medieval action with contemporary flair, all while exploring themes of honor and identity.',
        2001
    ),

    Movie(
        'I Am Legend',
        'Francis Lawrence',
        'Thriller',
        'I Am Legend is a post-apocalyptic thriller following Robert Neville, a scientist who may be the last human alive after a virus wipes out most of humanity. As he searches for a cure, he faces danger from mutant creatures and the haunting loneliness of survival.',
        2007
    ),

    Movie(
        'Braveheart',
        'Mel Gibson',
        'Drama',
        'Braveheart is a historical epic about William Wallace, a Scottish warrior who leads a rebellion against English oppression in the 13th century. The film is a stirring tale of courage, sacrifice, and the fight for freedom, marked by epic battles and unforgettable moments.',
        1995
    ),

    Movie(
        'Bee Movie',
        'Steve Hickner, Simon J. Smith',
        'Comedy',
        'Bee Movie is a quirky animated comedy about a bee named Barry who sues the human race for exploiting bees. The film is filled with odd humor, surreal moments, and a satirical look at the world through the eyes of a bee.',
        2007
    ),

    Movie(
        '21 & Over',
        'Jon Lucas, Scott Moore',
        'Comedy',
        '21 & Over follows two friends as they take their straight-laced college buddy out to celebrate his 21st birthday. What begins as a fun night of partying turns into a chaotic, hilarious adventure with wild antics and unexpected moments.',
        2013
    ),

    Movie(
        'Law Abiding Citizen',
        'F. Gary Gray',
        'Thriller',
        'Law Abiding Citizen is a gripping thriller about a man seeking justice after his wife and daughter are brutally murdered. The film delves into themes of revenge and justice as the protagonist takes matters into his own hands, causing chaos and challenging the system.',
        2009
    ),

    Movie(
        'American Gangster',
        'Ridley Scott',
        'Crime Drama',
        'American Gangster tells the true story of Frank Lucas, a heroin kingpin in 1970s New York, and the cop determined to bring him down. The film explores power, crime, and morality, with powerful performances by Denzel Washington and Russell Crowe.',
        2007
    )
]



# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def movie_index(request):
    return render(request, 'movies/index.html', {'movies': movies})