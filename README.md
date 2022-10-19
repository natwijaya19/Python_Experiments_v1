# Heading 1
## Heading 2
### Heading 3
#### Heading 4 [](#heading-4)
##### Heading 5

When your Python project relies on external packages, you need to make sure you’re using the right version of each package. After an update, a package might not work as it did before the update. A dependency manager like Python Poetry helps you specify, install, and resolve external packages in your projects. This way, you can be sure that you always work with the right dependency version on every machine.

In this tutorial, you’ll learn how to:

Start a new Poetry project
Add Poetry to an existing project
Use the pyproject.toml file
Pin dependencies
Install dependencies with poetry.lock
Execute basic Poetry CLI commands
Using Poetry will help you start new projects, maintain existing ones, and master dependency management. You’ll be prepared to work with pyproject.toml files, which will be the standard for defining build requirements in Python projects.

To complete this tutorial and get the most out of it, you should have a basic understanding of virtual environments, modules and packages, and pip.

[Custom foo description](#foo)

While this tutorial focuses on dependency management, Poetry can also help you with building and packaging projects. If you want to share your work, then you can even publish your Poetry project to the Python Packaging Index (PyPI).

``` python
class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")
```
---
> **Note**: This tutorial uses Poetry 1.1.4. If you’re using a different version, you might see different output or behavior.

Relevant Terminology
If you’ve ever used an import statement in one of your Python scripts, then you’ve worked with modules. Some of these modules might have been Python files you wrote on your own. Others could have been built-in modules, like datetime. However, sometimes what Python provides isn’t enough. That’s when you might turn to external, packaged modules. When your Python code relies on external modules, you can say that these packages are dependencies of your project.

You can find packages that aren’t part of the Python standard library in PyPI. Before seeing how this works, you need to install Poetry on your system.

Python Poetry Installation
To use Poetry in your command line, you should install it system-wide. If you just want to try it out, then you can install it into a virtual environment using pip. But you should try this method with caution because Poetry will install its own dependencies, which can conflict with other packages you’re using in your project.

The recommended way to install Poetry is by using the official install-poetry script. You can either download and run this Python file manually or select your operating system below to use the appropriate command:


Relevant Terminology
If you’ve ever used an import statement in one of your Python scripts, then you’ve worked with modules. Some of these modules might have been Python files you wrote on your own. Others could have been built-in modules, like datetime. However, sometimes what Python provides isn’t enough. That’s when you might turn to external, packaged modules. When your Python code relies on external modules, you can say that these packages are dependencies of your project.

You can find packages that aren’t part of the Python standard library in PyPI. Before seeing how this works, you need to install Poetry on your system.

Python Poetry Installation
To use Poetry in your command line, you should install it system-wide. If you just want to try it out, then you can install it into a virtual environment using pip. But you should try this method with caution because Poetry will install its own dependencies, which can conflict with other packages you’re using in your project.

The recommended way to install Poetry is by using the official install-poetry script. You can either download and run this Python file manually or select your operating system below to use the appropriate command:


Relevant Terminology
If you’ve ever used an import statement in one of your Python scripts, then you’ve worked with modules. Some of these modules might have been Python files you wrote on your own. Others could have been built-in modules, like datetime. However, sometimes what Python provides isn’t enough. That’s when you might turn to external, packaged modules. When your Python code relies on external modules, you can say that these packages are dependencies of your project.

You can find packages that aren’t part of the Python standard library in PyPI. Before seeing how this works, you need to install Poetry on your system.

Python Poetry Installation
To use Poetry in your command line, you should install it system-wide. If you just want to try it out, then you can install it into a virtual environment using pip. But you should try this method with caution because Poetry will install its own dependencies, which can conflict with other packages you’re using in your project.

The recommended way to install Poetry is by using the official install-poetry script. You can either download and run this Python file manually or select your operating system below to use the appropriate command:

Relevant Terminology
If you’ve ever used an import statement in one of your Python scripts, then you’ve worked with modules. Some of these modules might have been Python files you wrote on your own. Others could have been built-in modules, like datetime. However, sometimes what Python provides isn’t enough. That’s when you might turn to external, packaged modules. When your Python code relies on external modules, you can say that these packages are dependencies of your project.

You can find packages that aren’t part of the Python standard library in PyPI. Before seeing how this works, you need to install Poetry on your system.

Python Poetry Installation
To use Poetry in your command line, you should install it system-wide. If you just want to try it out, then you can install it into a virtual environment using pip. But you should try this method with caution because Poetry will install its own dependencies, which can conflict with other packages you’re using in your project.

The recommended way to install Poetry is by using the official install-poetry script. You can either download and run this Python file manually or select your operating system below to use the appropriate command:

Relevant Terminology
If you’ve ever used an import statement in one of your Python scripts, then you’ve worked with modules. Some of these modules might have been Python files you wrote on your own. Others could have been built-in modules, like datetime. However, sometimes what Python provides isn’t enough. That’s when you might turn to external, packaged modules. When your Python code relies on external modules, you can say that these packages are dependencies of your project.

You can find packages that aren’t part of the Python standard library in PyPI. Before seeing how this works, you need to install Poetry on your system.

Python Poetry Installation
To use Poetry in your command line, you should install it system-wide. If you just want to try it out, then you can install it into a virtual environment using pip. But you should try this method with caution because Poetry will install its own dependencies, which can conflict with other packages you’re using in your project.

The recommended way to install Poetry is by using the official install-poetry script. You can either download and run this Python file manually or select your operating system below to use the appropriate command:

Relevant Terminology
If you’ve ever used an import statement in one of your Python scripts, then you’ve worked with modules. Some of these modules might have been Python files you wrote on your own. Others could have been built-in modules, like datetime. However, sometimes what Python provides isn’t enough. That’s when you might turn to external, packaged modules. When your Python code relies on external modules, you can say that these packages are dependencies of your project.

You can find packages that aren’t part of the Python standard library in PyPI. Before seeing how this works, you need to install Poetry on your system.

Python Poetry Installation
To use Poetry in your command line, you should install it system-wide. If you just want to try it out, then you can install it into a virtual environment using pip. But you should try this method with caution because Poetry will install its own dependencies, which can conflict with other packages you’re using in your project.

The recommended way to install Poetry is by using the official install-poetry script. You can either download and run this Python file manually or select your operating system below to use the appropriate command:

Relevant Terminology
If you’ve ever used an import statement in one of your Python scripts, then you’ve worked with modules. Some of these modules might have been Python files you wrote on your own. Others could have been built-in modules, like datetime. However, sometimes what Python provides isn’t enough. That’s when you might turn to external, packaged modules. When your Python code relies on external modules, you can say that these packages are dependencies of your project.

You can find packages that aren’t part of the Python standard library in PyPI. Before seeing how this works, you need to install Poetry on your system.

Python Poetry Installation
To use Poetry in your command line, you should install it system-wide. If you just want to try it out, then you can install it into a virtual environment using pip. But you should try this method with caution because Poetry will install its own dependencies, which can conflict with other packages you’re using in your project.

The recommended way to install Poetry is by using the official install-poetry script. You can either download and run this Python file manually or select your operating system below to use the appropriate command:

Relevant Terminology
If you’ve ever used an import statement in one of your Python scripts, then you’ve worked with modules. Some of these modules might have been Python files you wrote on your own. Others could have been built-in modules, like datetime. However, sometimes what Python provides isn’t enough. That’s when you might turn to external, packaged modules. When your Python code relies on external modules, you can say that these packages are dependencies of your project.

You can find packages that aren’t part of the Python standard library in PyPI. Before seeing how this works, you need to install Poetry on your system.

Python Poetry Installation
To use Poetry in your command line, you should install it system-wide. If you just want to try it out, then you can install it into a virtual environment using pip. But you should try this method with caution because Poetry will install its own dependencies, which can conflict with other packages you’re using in your project.

The recommended way to install Poetry is by using the official install-poetry script. You can either download and run this Python file manually or select your operating system below to use the appropriate command:

Relevant Terminology
If you’ve ever used an import statement in one of your Python scripts, then you’ve worked with modules. Some of these modules might have been Python files you wrote on your own. Others could have been built-in modules, like datetime. However, sometimes what Python provides isn’t enough. That’s when you might turn to external, packaged modules. When your Python code relies on external modules, you can say that these packages are dependencies of your project.

You can find packages that aren’t part of the Python standard library in PyPI. Before seeing how this works, you need to install Poetry on your system.

Python Poetry Installation
To use Poetry in your command line, you should install it system-wide. If you just want to try it out, then you can install it into a virtual environment using pip. But you should try this method with caution because Poetry will install its own dependencies, which can conflict with other packages you’re using in your project.

The recommended way to install Poetry is by using the official install-poetry script. You can either download and run this Python file manually or select your operating system below to use the appropriate command:

Relevant Terminology
If you’ve ever used an import statement in one of your Python scripts, then you’ve worked with modules. Some of these modules might have been Python files you wrote on your own. Others could have been built-in modules, like datetime. However, sometimes what Python provides isn’t enough. That’s when you might turn to external, packaged modules. When your Python code relies on external modules, you can say that these packages are dependencies of your project.

You can find packages that aren’t part of the Python standard library in PyPI. Before seeing how this works, you need to install Poetry on your system.

Python Poetry Installation
To use Poetry in your command line, you should install it system-wide. If you just want to try it out, then you can install it into a virtual environment using pip. But you should try this method with caution because Poetry will install its own dependencies, which can conflict with other packages you’re using in your project.

The recommended way to install Poetry is by using the official install-poetry script. You can either download and run this Python file manually or select your operating system below to use the appropriate command:

Relevant Terminology
If you’ve ever used an import statement in one of your Python scripts, then you’ve worked with modules. Some of these modules might have been Python files you wrote on your own. Others could have been built-in modules, like datetime. However, sometimes what Python provides isn’t enough. That’s when you might turn to external, packaged modules. When your Python code relies on external modules, you can say that these packages are dependencies of your project.

You can find packages that aren’t part of the Python standard library in PyPI. Before seeing how this works, you need to install Poetry on your system.

Python Poetry Installation
To use Poetry in your command line, you should install it system-wide. If you just want to try it out, then you can install it into a virtual environment using pip. But you should try this method with caution because Poetry will install its own dependencies, which can conflict with other packages you’re using in your project.

The recommended way to install Poetry is by using the official install-poetry script. You can either download and run this Python file manually or select your operating system below to use the appropriate command:

"Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you."

'Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.'

``` python
def function (number1, number2):
    return number1 + number2
```

Cross-reference within the same page

[this link is to the heading 4](#heading-4)

[link to heading 1](#heading-1)

## my heading text (#mht)

Some normal text here,
including a [link to the header](#mht).

