"""Helper methods for running a build and test."""

from subprocess import Popen, PIPE

GIT_COMMAND = 'git'
NPM_COMMAND = 'npm'


def process(command, **kw):
    """Create a Popen object for the given command."""
    kw['stdout'] = kw.get('stdout', PIPE)
    kw['stderr'] = kw.get('stderr', PIPE)
    return Popen(command, **kw)


def fetch(path, remote='origin'):
    """Fetch changes to the git repository at the given path."""
    return process([
        GIT_COMMAND,
        '-C', path,
        'fetch', remote
    ])


def clone(repo, path='.'):
    """Clone a repo into the given path"""
    return process([
        GIT_COMMAND, 'clone',
        '-l',
        repo, path
    ])


def clean(path):
    """Clean non git files from the given repo."""
    return process([
        GIT_COMMAND,
        '-C', path,
        'clean', '-fdx',
    ])


def checkout(path, commitish='master'):
    """Checkout out a given commit hash."""
    return process([
        GIT_COMMAND,
        '-C', path,
        'reset', '--hard', commitish
    ])


def npm(path, command='install', *args):
    """Execute an npm script in the given directory."""
    args = [NPM_COMMAND, command]
    args.extend(args)

    return process(args, cwd=path)


def configure(src, build, opts=[]):
    """Derp"""
