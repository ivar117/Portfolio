from flask import render_template
from app import app, db
import sqlalchemy as sa
from app.models import Project

@app.route('/')
@app.route('/about', endpoint='about')
@app.route('/se')
def se():
    title = "About me"
    return render_template('index.html', title=title)

@app.route('/contact')
def contact():
    title = "Contact"
    return render_template('contact.html', title=title)

@app.route('/projects')
def projects():
    title = "Projects"

    teamProjects = []
    soloProjects = []
    query = sa.select(Project)
    projects = db.session.scalars(query).all()

    for project in projects:
        if (project.projectType == "solo"):
            soloProjects.append(project)
        elif (project.projectType == "team"):
            teamProjects.append(project)
    
    return render_template('projects.html', title=title, teamProjects=teamProjects, soloProjects=soloProjects)
