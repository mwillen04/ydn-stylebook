# YDN Stylebook
*Built by Michael Willen, Yale University, 2026.*

This website is designed to host the copy stylebook of the Yale Daily News. The current stylebook lives on an unwieldy, 85-page Google Document that is slow to load, slow to search, and overall difficult to use. This site provides an easier means of accessing and searching the Stylebook, with plans to expand its capabilities to include direct editing of the Stylebook and CAS-integrated login, among other features.

## How to Run

### Backend
```
cd backend\src
pip install -r requirements.txt
python .\stylebook.py
```

### Frontend
```
cd frontend
npm install
npm start
```

## Recent Changes

* Restructuring of original HTML site to include Flask; HTML replaced with React
* Implemented search bar with specific search varieties
* Replaced SQLite queries with SQLAlchemy
* Improved code documentation with better docstrings and comments
* Largely completed a major, full revision of the stylebook content

## Next Steps

* Add remaining old HTML pages to routing and templates
* Fix remaining CSS errors caused by switching to React
* Shift database away from SQLite

## Longer-Term Steps

* CAS Integration => Login, Profile, and Admin features
* On-site editing of the stylebook => both direct revision and a suggestion list
* Option to export stylebook data
* Web hosting
