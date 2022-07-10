# **Artist Discography Generator**
With this script you will generate a dataset about every music's metadata of an artist in ***csv*** and ***json***

## **How it works:**
First of all you must login with your Spotify account in ***[Spotify for developers]***. After that, you must create an app. It will give you the ***client ID*** and ***client Secret***. These two parameters are necessary to run the script. You have to copy them in the variables in ***[create_dataset.py]*** archive.

You can generate ***csv*** and ***json*** files according to your preferences by running ***[to_csv.py]*** or ***[to_json.py]*** archives.

You can change the dataset by adding or excluding the music's metadatas. In this script I used the following metadatas:
1. "danceability"
2. "energy"
3. "key"
4. "loudness"
5. "mode"
6. "speechiness"
7. "acousticness"
8. "instrumentalness"
9. "liveness"
10. "valence"
11. "tempo"
12. "duration_ms"
13. "time_signature"

<br>This is a part of the .json file generated
```json
{
    "artist_name": "Cocteau Twins",
    "album_name": "Heaven or Las Vegas",
    "album_img": "https://i.scdn.co/image/ab67616d0000b2732be08c60dcb4b5608abbe61e",
    "album_year": 1990,
    "track_name": "Frou-frou Foxes in Midsummer Fires",
    "track_id": 9,
    "danceability": 0.405,
    "energy": 0.619,
    "key": 10,
    "loudness": -6.003,
    "mode": 1,
    "speechiness": 0.0264,
    "acousticness": 0.00996,
    "instrumentalness": 9.02e-05,
    "liveness": 0.212,
    "valence": 0.243,
    "tempo": 160.074,
    "duration_ms": 338053,
    "time_signature": 4
}
```

<br>This is a part of the .csv file generated
```csv
artist_name,album_name,album_img,album_year,track_name,track_id,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature
Cocteau Twins,Heaven or Las Vegas,https://i.scdn.co/image/ab67616d0000b2732be08c60dcb4b5608abbe61e,1990,Frou-frou Foxes in Midsummer Fires,9,0.405,0.619,10,-6.003,1,0.0264,0.00996,9.02e-05,0.212,0.243,160.074,338053,4
```

### **Used tools**
``Pandas``, ``Spotify API``

## **Author**
| [<img src="https://avatars.githubusercontent.com/u/105020039?v=4" width=115><br><sub>Guilherme</sub>](https://github.com/guimfs) |
| :---: |
| [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" width=115>](https://www.linkedin.com/in/guilherme-mfs/) |


## **License**
The MIT License ([MIT])

Copyright (c) 2021 Othneil Drew

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

[links]: <> (Links used in this README.md file)
[MIT]: https://choosealicense.com/licenses/mit/
[Spotify for developers]: https://developer.spotify.com/dashboard
[create_dataset.py]: https://github.com/guimfs/artist-discography-spotify/blob/main/create_dataset.py
[to_csv.py]: https://github.com/guimfs/artist-discography-spotify/blob/main/to_csv.py
[to_json.py]: https://github.com/guimfs/artist-discography-spotify/blob/main/to_json.py