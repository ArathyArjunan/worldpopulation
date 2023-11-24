The django application is prepared using both python-django and api

1)registraion
url:http://127.0.0.1:8000/
method:post
authorization:nill
body:username,email,password1,password2


2)login
url:http://127.0.0.1:8000/signin/
method:get
authorization:nill
body:username,password


3)populationn add
url:http://127.0.0.1:8000/population/
method:post
authorization:nill
body:place,pop1980,pop2000,pop2010,pop2022,pop2023,pop2050,country,area,landAreaKm,cca2,cca3,netChange,growthRate,worldPercentage,density,densityMi,rank

4)population list
url:http://127.0.0.1:8000/index/
method:get
authorization:nill
body:nill

5)population detail
url:http://127.0.0.1:8000/population/{id}
method:get
authorization:nill
body:nill


6)population update
url:http://127.0.0.1:8000/population/{id}/change
method:put
authorization:nill
body:place,pop1980,pop2000,pop2010,pop2022,pop2023,pop2050,country,area,landAreaKm,cca2,cca3,netChange,growthRate,worldPercentage,density,densityMi,rank



7)population delete
url:http://127.0.0.1:8000/population/{id}/remove
method:delete
authorization:nill
body:nill

==============API=================================
1)obtain token 
url:http://127.0.0.1:8000/token/
method:post
authorization:nill
body:username,password



2)retrieve user details
url:http://127.0.0.1:8000/api/user/me/
method:get
headers:Token
body:nill


3)populationn add api
url:http://127.0.0.1:8000/api/population
method:post
headers:token
body:place,pop1980,pop2000,pop2010,pop2022,pop2023,pop2050,country,area,landAreaKm,cca2,cca3,netChange,growthRate,worldPercentage,density,densityMi,rank

4)population list api
url:http://127.0.0.1:8000/api/population/
method:get
headers:token
body:nill

5)population detail api
url:http://127.0.0.1:8000/api/population/{id}
method:get
headers:toekn
body:nill


6)population update api
url:http://127.0.0.1:8000/api/population/{id}/
method:put
headers:token   
body:place,pop1980,pop2000,pop2010,pop2022,pop2023,pop2050,country,area,landAreaKm,cca2,cca3,netChange,growthRate,worldPercentage,density,densityMi,rank



7)population delete api
url:http://127.0.0.1:8000/api/population/{id}/
method:delete
headers:token
body:nill



