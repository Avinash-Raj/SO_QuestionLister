# StackOverflow Question Listener

### Python script designed mainly for the people who are willing to answer questions(regarding any tag) on StackOverflow.

Python script which accepts a tag as parameter and do watching and printing all the newly posted questions according to that particular tag. If a new question appears
then it would produce a beep sound.

You don't need to look at your browser screen all the time for new questions. Just run this script in background and do your work. Whenever a new question appears on that particular tag, it should produce a beep sound.

#### Example:

`python so.py python`

#### Output:

```Python
-------------------------------------
Title : pyqt itemChanged and another var throught connect
Link  : http://stackoverflow.com//questions/33858291
Tags  : [python, pyqt, signals, connect]
-------------------------------------
Title : (Python) List of lists with one parameter that leads to another
Link  : http://stackoverflow.com//questions/33858271
Tags  : [python, python-2.7]
-------------------------------------
Title : Can't deploy django application with heroku
Link  : http://stackoverflow.com//questions/33858252
Tags  : [python, django, heroku]
-------------------------------------
Title : scipy.integrate.quad to integrate for gamma function
Link  : http://stackoverflow.com//questions/33858166
Tags  : [python, scipy, integration, gamma]
-------------------------------------
Title : how to enable mod_xsendfile in apache2 in case of using mod_wsgi-express and django
Link  : http://stackoverflow.com//questions/33858142
Tags  : [python, django, apache, ubuntu, mod-wsgi]
```