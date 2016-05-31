# OpenBikes browser frontend

- React
- Sass
- Webpack with hot reloading
- [Airbnb style conventions](https://github.com/airbnb/javascript)

## Installation

You can install **Node JS** through this [download page](https://nodejs.org/en/download/).
If you're on Mac OS X, follow these steps :

1. Install **Homebrew**  
    ```sh
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```
2. Update `brew`  
    This will update brew to the latest version :  
    ```sh
    brew update
    ```
3. Upgrade `brew` packages  
    Upgrade all of your brew packages with :  
    ```sh
    brew upgrade
    ```
4. Install **Node JS**  
    Next, install **node** (`npm` will be installed with `node`):  
    ```sh
    brew install node
    ```

Or you can just run `make install`.

Then you need to download our repo using `git` :  
```sh
git clone https://github.com/OpenBikes/openbikes.co.git
```

## Usage

Install **node** depencies with : `npm install` (or `make dev`).  
Finally, run `npm start` (or `make run`).