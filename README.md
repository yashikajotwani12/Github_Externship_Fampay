 <div align="center"> 
 <img width ="300" src="https://externship.github.in/assets/Logo/Logo%20Color.svg"/>
 </div>

<h1 align="center">
<img  width="30" src="https://user-images.githubusercontent.com/77020164/146640192-61300696-16fd-4e8d-be1e-226ba1f90c52.png"/>
Fampay - Backend Assignment Extern
</h1>


### Project Goal ✨

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

**Screenshots:**

| ![Add-1](API_Youtube/Images/Json_Format_.png)  |  ![ADD-2](API_Youtube/Images/API1.png) |
|:---:|:---:|
| Json format | HomePage |

| ![Add-1](API_Youtube/Images/Objects.png)  |  ![ADD-2](API_Youtube/Images/Search.png) |
|:---:|:---:|
| Database view | Filtering/Sorting |

| ![Add-1](API_Youtube/Images/YoutubeAPI.png)  |  ![ADD-2](API_Youtube/Images/admin.png) |
|:---:|:---:|
| YoutubeApi_keys | Single Video View |

## Setting Up 🔨

 <details>
  <summary><strong>Setup Steps</strong></summary>

- Clone the Repository
 ```
$ git clone https://github.com/yashikajotwani12/API_Youtube
 ```
- Go the the folder
 ```
$ cd API_Youtube
 ```
- Setup Virtual environment
 ```
$ python3 -m venv env
```
- Activate the virtual environment
```
$ source env/bin/activate
```
- Install dependencies using
```
$ pip install -r requirements.txt
```
- Modify settings.py File - Remove the existing keys and add your own YouTube Data API keys in the form [key1, key2, ...]:
```
$ API_KEYS = ['Google_API_Key_1', 'Google_API_Key_2','Google_API_Key_3',] 
```
- Make migrations using
```
$ python manage.py makemigrations
```
- Migrate Database
```
$ python manage.py migrate
```
- Create a superuser
```
$ python manage.py createsuperuser
```
- Run server using
```
$ python manage.py runserver
``` 
  
</details>


## Usage

Run the manage.py file:

```python
python3 manage.py runserver
```
## Reference:

    YouTube data v3 API: https://developers.google.com/youtube/v3/getting-started
    Search API reference: https://developers.google.com/youtube/v3/docs/search/list
    To fetch the latest videos you need to specify these: type=video, order=date, publishedAfter=<SOME_DATE_TIME>
    Without publishedAfter, it will give you cached results which will be too old


## Directory Structure
    
    API_Youtube            
    .
    ├── Contains       
    |   ├── Screenshots       # Contain screenshots of the project and other images
    │   ├── API               # The main Django app/api containing the models, views, serializers etc
    │   ├── API_Youtube       # All the settings and url routes settings of the REST API
    |   ├── db.sqlite3        # SQLite database housing the data of the videos fetched
    │   └── manage.py         # Python code used for starting the app by establishing DRF server
    |   └── requirements.txt  # Requirements file
    |______________________   
