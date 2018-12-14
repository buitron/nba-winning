# NBA Winning

## Objective
Predict each NBA playoff team's final W count.

## About
21 years of regular season NBA team stats data was scraped, starting at 1997 till 2018. The scraped data was used in fitting the ML model. The SVM model is able to predict the final season's Win score per team with a mean STD of 3.5 wins. The model metrics information is stored at this location `./src/static/model/support_vector_machines.txt`. To see the entire data pre-processing and model selection that was used for this project you can clone this project and start this jupyter notebook: `./model_building.ipynb`

## Starting a Docker Container
#### Installation of DockerCE (Community Edition)

- For macOS:

  1. go to this link: [https://download.docker.com/mac/stable/Docker.dmg](https://download.docker.com/mac/stable/Docker.dmg) to initiate the latest stable version packaged download.
- For Windows:

  1. go to this link: [https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe) to initiate the latest stable version download.

- For Debian OS Linux:

  1. Update the `apt` package index.

     ```bash
     $ sudo apt-get update
     ```

  2. Install the _latest version_ of Docker CE, or go to the next step to install a specific version:

     ```bash
     $ sudo apt-get install docker-ce
     ```

#### Create the Docker image for this project

In your shell CLI (I am using bash) navigate to the root (where the `Dockerfile` is located).

```bash
$ cd into/this/projects/root/directory/
$ ls
... ... Dockerfile ...
```

Build the Docker image

```bash
$ docker build -t image-name .
Sending build context to Docker daemon [size]
Step 1/* : FROM [base]
...
Successfully built ************
Successfully tagged ***:latest
```

#### Run the Docker container from the image

```bash
$ docker run -dp 5000:5000 --rm image-name
**************************************
```

Check to see of the daemon process is working in the background

```bash
$ docker ps -a
ContainerID	Image	     Command	 Created   Status		    Ports				           Names
***********	image-name "/bin/sh" 3 seconds Up 3 seconds 0.0.0.0:5000->5000/tcp Rdm-name
```

## Sample
After successfully deploying the container to the port 5000 open up an Internet browser and type `http://localhost:5000` into the URL bar and the following webpage will magically appear.

![Sample GIF](./media/sample.gif)

to terminate the docker daemon process and then remove the image from your system:

```bash
$ docker stop (ContainerID or Name)
*************
$ docker rmi image-name
Deleted: sha256:*************************************
Deleted: sha256:*************************************
Deleted: sha256:*************************************
...
```

## Development Process
**Step 1 - Data Gathering and Cleaning**
* Data was collected from <a href="https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1">HERE</a>.
* Bonus, live score board
** The endpoint http://data.nba.net/10s/prod/v1/<today>/scoreboard.json

**Step 2 - ML Model Build**
The code and process I used for developing the various model's used in this application is located >> `./model_building.ipynb`

**Step 3 - Flask**
Python Flask is the framework used to establish the various routes, APIs, as well as the templating system to tie the backend with what you see in the browser application.

**Step 4 - Dockerizing**
This application has been configured to easily build a docker image from which you're able to containerize and launch. Everything needed to build the Docker ubuntu image is included inside of the `Dockerfile`.


### Credit
tbd
