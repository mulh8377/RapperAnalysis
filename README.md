# RapperAnalysis
A fun python data science project that just analyzes lyrics and albums from various artists.
Will be using some natural language processing libraries to help with analysis (spaCy, nltk). 
Hopefully, I can train a model that can score an artist's discography --

## Libraries Still Needing to Be Installed on Virtual Environment
    - spacy
    - sqlite3
    - waiting to be added...

## Database
Tables:
    Artist
        (Artist Name, Artist Directory, Artist URL)
    Album
        (Artist Hash, Album Name, Album Path, Total Songs)
    Song
        (Artist Hash, Song Name, Song Path, Album Hash)  
    