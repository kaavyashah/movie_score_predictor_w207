# w207-final


<h1 align="center"><What Makes a MOVIE? 🎥 ></h1>
  
## Repository Structure
- [data](data) - Includes cleaned data files used in the project.

- [KNN_clustering.ipynb](KNN_clustering.ipynb) - IPython Notebook with code for k-NN Clustering

- [Machine Learning Modeling.ipynb](https://github.com/kaavyashah/w207-final/blob/5b1362c4888d9ce66e0facf4ee638cd5e78c9b3c/Machine%20Learning%20Modeling.ipynb) - IPython Notebook with code for modeling for this project

- [data_cleaning.py](data_cleaning.py) - Python file to do initial cleaning on TMDB dataset. Writes cleaned file into the data folder

- [get_vid_id.py](get_vid_id.py) - Uses Youtube API to get video_id based on the movies names in [data/cleaned_movies.csv](data/cleaned_movies.csv) and stores video_id's in [data/vid_stats.csv](data/vid_stats.csv).
  
- [get_vid_stats.py](get_vid_stats.py) - Uses Youtube API to get video stats based on video_id's stored in [data/vid_stats.csv](data/vid_stats.csv) and writes movie names and stats in the same file.
  
- [scrape_scripts.py](scrape_scripts.py) - Python file to scrape movie scripts
  
- [scripts.txt](scripts.txt) - Text file with scraped script text


### Contributors
Elías Saravia, Jenna Morabito, Joyce Li, Kaavya Shah, Kseniya Usovich
