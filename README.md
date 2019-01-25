# Project Title

This is a short project examinging the distance learning dataset located here (https://analyse.kmi.open.ac.uk/open_dataset).  In this project I am building a model to predict the final exam score for a student in the "DDD" module using their past grades, demographics, and study habits.  

## Getting Started

* You will need to move a copy of the distance learning data located here (https://analyse.kmi.open.ac.uk/open_dataset) to the data/raw directory.  
* Then you will need to run src/data/features/preprocessing.py 
* You should be good to go, the only piece of code you wouldn need at that point is the StudentAnalysisAndModel.ipynb located in the notebooks directory 

### Prerequisites

You will need to install the following packages to run the code

```
conda install scikit-learn
conda install pandas
conda install numpy
conda install matplotlib
conda install seaborn
```



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── Valkyrie Presentation.pdf        <- Report for Valkyrie
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── features       <- Scripts to merge data and get the data (mostly) ready for modeling
    │   │   └── preprocessing.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
