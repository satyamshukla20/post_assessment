import os
import click

@click.command()
@click.argument('project_name')
def create_boilerplate(project_name):
    os.makedirs(project_name)
    os.chdir(project_name)
    os.makedirs('src')
    os.makedirs('db')
    os.makedirs('models')
    os.makedirs('config')
    os.makedirs('routes')
    with open('app.py', 'w') as f:
        f.write(f"print('This is my project name -> {project_name}')")

    print(f"{project_name} successfully created.")

if __name__ == '__main__':
    create_boilerplate()