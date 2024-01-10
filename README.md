# StableDiffusionCharacterCreator
Use generative AI to create characters for your projects

This app uses Stable Diffusion, StreamLit, and Python to create and easy-to-use interface for creating character profile images.

## Setup

1. Follow the steps to setup a local instance of Stable Diffusion:
https://github.com/AUTOMATIC1111/stable-diffusion-webui

2. Make sure to use the --api flag when running the web server:
```
./webui.sh --api
```

OR 

1.1 Find an instance of Stable Diffusion running out in the wild and hook up to it in the app.py file

3. Clone this repo

3. Use the "run and debug" button in VSCode to start the app

OR 

3.1 In your terminal use the command `streamlit run app.py`

4. Type in a short description into the txt box and hit the "Create!" button

5. Go get a cup of coffee

6. Enjoy the generated profile pic! 

The images created are stored in the `sdresults` folder, and images with background removed are stored in `nobackground`