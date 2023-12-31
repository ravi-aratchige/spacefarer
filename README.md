# Spacefarer :rocket:

<img src="./assets/banner.png">

Ever wondered what role you would play if you were a cosmic voyager, adventuring through space with your resourceful crew members?

Spacefarer uses machine learning to determine what type of astronaut you would be, based on your responses to a series of questions about your personality.

<img src="./assets/home.png">

You can be one of the following types of astronauts:

1. **Navigator** - steers and guides the spacecraft in the vast depths of space.
2. **Communicator** - maintains contact with stations and other spacecrafts.
3. **Explorer** - ventures boldly into uncharted realms and territories.
4. **Commander** - leading the spacecraft, its crew and their operation.
5. **Scientist** - conducting research and unraveling the mysteries of the cosmos.

Spacefarer asks you a series of 20 space-themed questions; 4 questions each for the 5 personality traits of the <a href="https://mettl.com/glossary/b/big-five-personality-test/#:~:text=The%20Big%20Five%20personality%20test%2C%20also%20known%20as%20the%20OCEAN,making%20the%20acronym%20%E2%80%93%20OCEAN).">**Big Five Personality Test**</a>:

1. Openness
2. Neuroticism
3. Conscientiousness
4. Agreeableness
5. Extraversion

The answers provided to these questions are passed to a trained and deserialized model, which predicts your personality type, which is in turn mapped to a type of astronaut.

<img src="./assets/result.png">

Spacefarer is built as a <a href="https://flask.palletsprojects.com">Flask</a> web app, styled with <a href="https://tailwindcss.com/">TailwindCSS</a> and powered by a <a href="https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html">`LogisticRegression`</a> model trained on a small (approx. 700 samples) dataset from <a href="https://www.kaggle.com/datasets/pavlorymarchuk/test3434">Kaggle</a>. The model has an accuracy of **81.53%**.

## Setup

### Prerequisites

Spacefarer has very few prerequisites, which are probably already installed on your system:

1. <a href="https://git-scm.com/">Git</a> version control system
2. <a href="https://www.python.org/">Python</a> (recommended to have a version greater than 3.9.0)
3. <a href="https://nodejs.org/en">Node.js</a> (recommended to have a version greater than 18.0.0)

To run Spacefarer locally on your machine, follow these steps:

### 1. Clone Project

Clone Spacefarer to a desired location (folder) on your machine by opening up a terminal from the folder and entering the following command:

```shell
git clone https://github.com/ravi-aratchige/spacefarer.git
```

Next, move into the `spacefarer` project directory:

```shell
cd spacefarer
```

### 2. Activate Virtual Environment

A virtual environment will help you keep Spacefarer's dependencies isolated from the global system of Python packages. To setup your virtual environment, first ensure that `virtualenv` is installed on your system:

```shell
pip install virtualenv
```

To create and activate a virtual environment, enter the following commands after moving into the `spacefarer` folder as done in the previous step:

```shell
# Create a virtual environment named 'env':
python -m venv env

# Activate the virtual environment (Windows):
env\Scripts\activate.bat

# Activate the virtual environment (MacOS / Linux):
source env/bin/activate
```

Your terminal will now include an `(env)` prefix, indicating a successful activation of the virtual environment:

```shell
# On Windows:
(env) drive:\folder\...spacefarer>

# On MacOS and Linux
(env) user@computer:~/...spacefarer$
```

To deactivate the virtual environment (and remove the `(env)` prefix):

```shell
deactivate
```

### 3. Install Dependencies

After activating the virtual environment, you can install all of the necessary dependencies with a single command:

```shell
pip install -r requirements.txt
```

<a href="https://github.com/ravi-aratchige/spacefarer/blob/main/requirements.txt">`requirements.txt`</a> includes all of the project's dependencies and their respective versions.

### 4. Start Flask App

Move from the root of the project into the `app` directory (where the Flask app is stored in):

```shell
cd app
```

Then, install the necessary NPM packages. This is essential for TailwindCSS:

```shell
npm install

# or

npm i
```

Finally, start up the Flask server:

```shell
python app.py

# or

python3 app.py
```

Flask will then serve Spacefarer on <a>http://localhost:5000</a> (development server).

## Contribution

This project is fully open-source (including data and the model). Contributions are always welcome; you may fork this project, work on it and submit a pull request.

**IMPORTANT**: during development, the TailwindCSS build process must be started (for automatic purging and optimization).

For this, first enter the `app` folder in the project directory (after activating the virtual environment):

```shell
cd app
```

Then, run the following command:

```shell
npm run create-css
```

This project is still underway, so you can expect changes often!

### To-Do

- [ ] Create 'About page' (`/about`)
- [ ] Add <a href="https://vincentgarreau.com/particles.js/">particles.js</a> to background of Flask app
- [ ] Optimize `form.html` using loops in Jinja blocks

---

Made with :heart: by Ravindu Aratchige. Licensed under the <a href="https://github.com/ravi-aratchige/spacefarer/blob/main/LICENSE">Apache License<a>.
