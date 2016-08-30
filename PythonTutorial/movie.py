#movie.py
#!/usr/bin/env python
#list of lists
movies=[['spotlight',120, 'Tom McCarthy'],
        ['The big short',110, 'Adam McKay']]
#list of the dict
movies2 = [{'name': 'spotlight','length': 120, 'director': 'Tom McCarthy'},
            {'name': 'The big short','length': 110, 'director': 'Adam McKay'}
            {'name': 'The Martian', 'length': 151, 'director': 'Scott'}]
#dict of dicts(tree)
movies3 = {'spotlight':{'length': 120, 'director': 'Tom McCarthy'},
           'The big short':{'length': 110, 'director': 'Adam McKay'}
           'The Martian': {'length': 151, 'director': 'Scott'}}
        
look_for = raw_input('Movie name: ')

for one_movie in movies:
    if one_movie[0] == look_for:
        print'found {}, {} minutes, dir {}'.format(one_movie[0],one_movie[1],one_movie[2])
        
    break
for one_movie in movies2:
    if one_movie['name'] == look_for:
        print'found {}, {} minutes, director: {}'.format(one_movie['name'],one_movie['length'],one_movie['director'])
    break
    
for one_movie in movies3:
    one_movies3 = movies[look_for]
    print "Got {}, {} min, dir {}".format(look_for, one_movie['length'], one_movie['director'])
    break
else:
    #we got to the natural end of the loop;without break
    print "Did not find {}".format(look_for)