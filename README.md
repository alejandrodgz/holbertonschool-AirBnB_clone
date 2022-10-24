# Tasks

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <p>
   <img alt="" loading="lazy" src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20221024%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20221024T192416Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=590f7e8010036c43d46a0e14d43730c1a2b3b970693a8f88a0cdcc26180b14f7" style=""/>
  </p>
  <h2>
   Background Context
  </h2>
  <h3>
   Welcome to the AirBnB clone project!
  </h3>
  <p>
   Before starting, please read the
   <strong>
    AirBnB
   </strong>
   concept page.
  </p>
  <p>
   <br/>
  </p>
  <iframe allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/E12Xc3H2xqo" width="560">
  </iframe>
  <p>
   <br/>
  </p>
  <h4>
   First step: Write a command interpreter to manage your AirBnB objects.
  </h4>
  <p>
   This is the first step towards building your first full web application: the
   <strong>
    AirBnB clone
   </strong>
   .
This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
  </p>
  <p>
   Each task is linked and will help you to:
  </p>
  <ul>
   <li>
    put in place a parent class (called
    <code>
     BaseModel
    </code>
    ) to take care of the initialization, serialization and deserialization of your future instances
   </li>
   <li>
    create a simple flow of serialization/deserialization: Instance &lt;-&gt; Dictionary &lt;-&gt; JSON string &lt;-&gt; file
   </li>
   <li>
    create all classes used for AirBnB (
    <code>
     User
    </code>
    ,
    <code>
     State
    </code>
    ,
    <code>
     City
    </code>
    ,
    <code>
     Place
    </code>
    …) that inherit from
    <code>
     BaseModel
    </code>
   </li>
   <li>
    create the first abstracted storage engine of the project: File storage.
   </li>
   <li>
    create all unittests to validate all our classes and storage engine
   </li>
  </ul>
  <h3>
   What’s a command interpreter?
  </h3>
  <p>
   Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
  </p>
  <ul>
   <li>
    Create a new object (ex: a new User or a new Place)
   </li>
   <li>
    Retrieve an object from a file, a database etc…
   </li>
   <li>
    Do operations on objects (count, compute stats, etc…)
   </li>
   <li>
    Update attributes of an object
   </li>
   <li>
    Destroy an object
   </li>
  </ul>
  <h2>
   Resources
  </h2>
  <p>
   <strong>
    Read or watch
   </strong>
   :
  </p>
  <ul>
   <li>
    <a href="https://docs.python.org/3.4/library/cmd.html" target="_blank" title="cmd module">
     cmd module
    </a>
   </li>
   <li>
    <strong>
     packages
    </strong>
    concept page
   </li>
   <li>
    <a href="https://docs.python.org/3.4/library/uuid.html" target="_blank" title="uuid module">
     uuid module
    </a>
   </li>
   <li>
    <a href="https://docs.python.org/3.4/library/datetime.html" target="_blank" title="datetime">
     datetime
    </a>
   </li>
   <li>
    <a href="https://docs.python.org/3.4/library/unittest.html#module-unittest" target="_blank" title="unittest module">
     unittest module
    </a>
   </li>
   <li>
    <a href="https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/" target="_blank" title="args/kwargs">
     args/kwargs
    </a>
   </li>
   <li>
    <a href="https://www.pythonsheets.com/notes/python-tests.html" target="_blank" title="Python test cheatsheet">
     Python test cheatsheet
    </a>
   </li>
  </ul>
  <h2>
   Learning Objectives
  </h2>
  <p>
   At the end of this project, you are expected to be able to
   <a href="https://fs.blog/feynman-learning-technique/" target="_blank" title="explain to anyone">
    explain to anyone
   </a>
   ,
   <strong>
    without the help of Google
   </strong>
   :
  </p>
  <h3>
   General
  </h3>
  <ul>
   <li>
    How to create a Python package
   </li>
   <li>
    How to create a command interpreter in Python using the
    <code>
     cmd
    </code>
    module
   </li>
   <li>
    What is Unit testing and how to implement it in a large project
   </li>
   <li>
    How to serialize and deserialize a Class
   </li>
   <li>
    How to write and read a JSON file
   </li>
   <li>
    How to manage
    <code>
     datetime
    </code>
   </li>
   <li>
    What is an
    <code>
     UUID
    </code>
   </li>
   <li>
    What is
    <code>
     *args
    </code>
    and how to use it
   </li>
   <li>
    What is
    <code>
     **kwargs
    </code>
    and how to use it
   </li>
   <li>
    How to handle named arguments in a function
   </li>
  </ul>
  <h2>
   Requirements
  </h2>
  <h3>
   Python Scripts
  </h3>
  <ul>
   <li>
    Allowed editors:
    <code>
     vi
    </code>
    ,
    <code>
     vim
    </code>
    ,
    <code>
     emacs
    </code>
   </li>
   <li>
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
   </li>
   <li>
    All your files should end with a new line
   </li>
   <li>
    The first line of all your files should be exactly
    <code>
     #!/usr/bin/python3
    </code>
   </li>
   <li>
    A
    <code>
     README.md
    </code>
    file, at the root of the folder of the project, is mandatory
   </li>
   <li>
    Your code should use the pycodestyle (version 2.7.*)
   </li>
   <li>
    All your files must be executable
   </li>
   <li>
    The length of your files will be tested using
    <code>
     wc
    </code>
   </li>
   <li>
    All your modules should have a documentation (
    <code>
     python3 -c 'print(__import__("my_module").__doc__)'
    </code>
    )
   </li>
   <li>
    All your classes should have a documentation (
    <code>
     python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    </code>
    )
   </li>
   <li>
    All your functions (inside and outside a class) should have a documentation (
    <code>
     python3 -c 'print(__import__("my_module").my_function.__doc__)'
    </code>
    and
    <code>
     python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    </code>
    )
   </li>
   <li>
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
   </li>
  </ul>
  <h3>
   Python Unit Tests
  </h3>
  <ul>
   <li>
    Allowed editors:
    <code>
     vi
    </code>
    ,
    <code>
     vim
    </code>
    ,
    <code>
     emacs
    </code>
   </li>
   <li>
    All your files should end with a new line
   </li>
   <li>
    All your test files should be inside a folder
    <code>
     tests
    </code>
   </li>
   <li>
    You have to use the
    <a href="https://docs.python.org/3.4/library/unittest.html#module-unittest" target="_blank" title="unittest module">
     unittest module
    </a>
   </li>
   <li>
    All your test files should be python files (extension:
    <code>
     .py
    </code>
    )
   </li>
   <li>
    All your test files and folders should start by
    <code>
     test_
    </code>
   </li>
   <li>
    Your file organization in the tests folder should be the same as your project
   </li>
   <li>
    e.g., For
    <code>
     models/base_model.py
    </code>
    , unit tests must be in:
    <code>
     tests/test_models/test_base_model.py
    </code>
   </li>
   <li>
    e.g., For
    <code>
     models/user.py
    </code>
    , unit tests must be in:
    <code>
     tests/test_models/test_user.py
    </code>
   </li>
   <li>
    All your tests should be executed by using this command:
    <code>
     python3 -m unittest discover tests
    </code>
   </li>
   <li>
    You can also test file by file by using this command:
    <code>
     python3 -m unittest tests/test_models/test_base_model.py
    </code>
   </li>
   <li>
    All your modules should have a documentation (
    <code>
     python3 -c 'print(__import__("my_module").__doc__)'
    </code>
    )
   </li>
   <li>
    All your classes should have a documentation (
    <code>
     python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    </code>
    )
   </li>
   <li>
    All your functions (inside and outside a class) should have a documentation (
    <code>
     python3 -c 'print(__import__("my_module").my_function.__doc__)'
    </code>
    and
    <code>
     python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    </code>
    )
   </li>
   <li>
    We strongly encourage you to work together on test cases, so that you don’t miss any edge case
   </li>
  </ul>
  <h3>
   GitHub
  </h3>
  <p>
   <strong>
    There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.
   </strong>
  </p>
  <h2>
   More Info
  </h2>
  <h3>
   Execution
  </h3>
  <p>
   Your shell should work like this in interactive mode:
  </p>
  <pre><code>$ ./console.py
(hbnb) help

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
</code></pre>
  <p>
   But also in non-interactive mode: (like the Shell project in C)
  </p>
  <pre><code>$ echo "help" | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
</code></pre>
  <p>
   All tests should also pass in non-interactive mode:
   <code>
    $ echo "python3 -m unittest discover tests" | bash
   </code>
  </p>
  <p>
   <img alt="" loading="lazy" src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20221024%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20221024T192416Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=959e89979b3e0dbcc985e39709223df6e1ac0fe4cf6d9357507dced545aeda40" style=""/>
  </p>
  <p>
   <br/>
  </p>
  <iframe allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/p00ES-5K4C8" width="560">
  </iframe>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/2185)
</html>