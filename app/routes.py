from flask import render_template, request
from app import app 
from pathlib import Path
from jinja2 import FileSystemLoader, Environment
import flask
import yaml
import subprocess
import importlib
import sys

@app.route('/')
@app.route('/index')
def index():

    # Load up all the scripts from the user directory
    p = Path('./repos')
    script_data = [
        {"name": x.parts[-1], 
         "id": x.parts[-1],
         "path": x} for x in p.iterdir() if x.is_dir()]

    #print(render_template('base.html', scripts=script_data))
    return render_template('base.html', scripts=script_data)

@app.route('/script/<script>')
def script_start_point(script):
    return render_template('script_start.html', script_name=script)

@app.route('/run_script/<script>', methods=['GET', 'POST'])
def run_script(script):
    if flask.request.method == 'GET':
        file_path = Path(".") / "repos" / script / "main.py"
        file_path = file_path.resolve()

        spec = importlib.util.spec_from_file_location('main', file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules['main'] = module
        main = importlib.import_module('main')

        variables = main.pre()

        return ui(script, "ui.yml", **variables)

    elif flask.request.method == 'POST': 
        file_path = Path(".") / "repos" / script / "main.py"
        file_path = file_path.resolve()

        spec = importlib.util.spec_from_file_location('main', file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules['main'] = module
        main = importlib.import_module('main')
        form_data = request.form.to_dict()

        output = main.main(**form_data)

        return render_template('output.j2', data=output)


def ui(script, ui_name, **kwargs):
    ui_details = {}
    templateLoader = FileSystemLoader(searchpath=f'./repos/{script}')
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template(ui_name)
    raw_ui = template.render(**kwargs)

    try:
        ui_details = yaml.safe_load(raw_ui)
    except yaml.YAMLError as exc:
        return "Unable to parse the script launcher"

    print(ui_details) 
    template = render_template("ui_template.j2", details=ui_details, script=script) 
    return(template)
