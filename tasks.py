from invoke import task


@task
def aloita(ctx):
    ctx.run("python3 src/shakki.py", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_raportti(ctx):
    ctx.run("coverage html", pty=True)

@task()
def testit(ctx):
    ctx.run("pytest src", pty=True)