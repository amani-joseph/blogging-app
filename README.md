<!-- @format -->

# pitch-in-sixty

## Author

[Amani-Joseph(https://github.com/amani-joseph)

# Description

This is a blogging flask application that allows users to view blogs and to create blogs once they signup. Users are able to comment on blogs and have other users comment on their blogs too.

## Live Link

[https://amani-blogging-app.herokuapp.com/]

## Screenshot

<!-- <img src="https://github.com/amani-joseph/pitch-in-sixty/blob/master/app/static/images/pitch-in-sixty.herokuapp.com_signup.png?raw=true" >
<img src="https://github.com/amani-joseph/pitch-in-sixty/blob/master/app/static/images/pitch-in-sixty.herokuapp.com_login.png?raw=true" >
<img src="https://github.com/amani-joseph/pitch-in-sixty/blob/master/app/static/images/pitch-in-sixty.herokuapp.com_%20(1).png?raw=true" >
 -->

## User Story

<!-- * Comment on the different pitches posted py other uses.
* See the pitches posted by other uses.
* Vote on s pitch they have viewed by giving it a upvote or a down-vote.
* Register to be allowed to log in to the application
* View pitches from the different categories.
* Submit a pitch to a specific category of their choice. -->

## BDD

| Behavior              |                Input                |                                                                 Output |
| :-------------------- | :---------------------------------: | ---------------------------------------------------------------------: |
| Load the page         |          **On page load**           |                        Get all blogs, Select between sign-up and login |
| Select SignUp         | **Email**,**Username**,**Password** |                                                      Redirect to login |
| Select Login          |    **Username** and **password**    |                                            Redirect to page with Blogs |
| Select comment button |             **Comment**             |                                       Form that you input your comment |
| Click on submit       |                                     | Redirect to all comments template with your comment and other comments |

## Development Installation

To get the code..

1. Cloning the repository:

```bash
https://github.com/amani-joseph/blogging-app.git
```

2. Move to the folder and install requirements

```bash
cd pitch-world
pip install -r requirements.txt
```

3. Exporting Configurations

```bash
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
```

4. Running the application

```bash
python3 manage.py server
```

5. Testing the application

```bash
python3 manage.py test
```

Open the application on your browser `127.0.0.1:5000`.

## Technology used

- [Python3.8](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [Heroku](https://heroku.com)

## Known Bugs

- Still in development

## Contact Information

If you have any question or contributions, please email me at [mr.amanijoseph@gmail.com]

## License

- _MIT License:_
- Copyright (c) 2022 **Amani. J**
