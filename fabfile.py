from fabric.decorators import task

@task
def hello():
    print("I'm alive!")
