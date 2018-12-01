# Garden - A maze generation implementation

## Setting up and using it

### Setup
Setting up the project is easy. Follow these steps:

- Clone this repo
  `git clone https://github.com/nejdetckenobi/garden`

- Go to project directory
  `cd garden`

- Create a virtual environment
  `virtualenv -p $(which python3) venv`

- Activate the virtual environment
  `source venv/bin/activate`

- Install dependencies
  `pip install pillow imageio`


### Usage

- To generate a simple animation with 5 mazes, use:
  `python samplescript.py`

- After that, you'll get a file named `lab.gif`. This is the animation. It's unoptimized so before trying to upload anywhere, I recommend optimizing it via tools like `gifsicle`


**Note**: All implementation made in `imps.py`. You can check the algorithm and other things in there. For usage, examine `samplescript.py`

## Example

This is the result when you run `samplescript.py`

![opt](https://user-images.githubusercontent.com/4905664/49155447-043cbc80-f32c-11e8-87a8-bcecccf17c47.gif)

This is another maze with the size of 512 x 512

![lab](https://user-images.githubusercontent.com/4905664/49157317-9050e300-f330-11e8-9342-6be42cd44751.png)

Some other things with customized classes.

![opt2](https://user-images.githubusercontent.com/4905664/49330750-158ffe00-f5a4-11e8-9264-03efdf44de7e.gif)
