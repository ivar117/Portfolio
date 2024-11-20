from flask import render_template
from app import app, db
import sqlalchemy as sa
from app.models import Project

@app.route('/')
@app.route('/index', endpoint='index')
def se():
    title = "Ivar Bjerling - Portfolio"

    teamProjects = []
    soloProjects = []
    query = sa.select(Project)
    projects = db.session.scalars(query).all()

    for project in projects:
        if (project.projectType == "solo"):
            soloProjects.append(project)
        elif (project.projectType == "team"):
            teamProjects.append(project)

    return render_template('index.html', title=title, teamProjects=teamProjects, soloProjects=soloProjects)
