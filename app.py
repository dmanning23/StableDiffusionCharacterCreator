
import streamlit as st
import webuiapi
import uuid
from rembg import new_session, remove

def main():
    st.set_page_config(
        page_title="Create Characters With Stable Diffusion",
        page_icon="😺")
    
    # create API client
    #api = webuiapi.WebUIApi()
    api = webuiapi.WebUIApi(host='127.0.0.1', port=7860)
    #api = webuiapi.WebUIApi(host='webui.example.com', port=443, use_https=True)
    
    #setup rembg to use the anime filter
    session = new_session("isnet-anime")

    container = st.container()
    with container:
        with st.form(key="my form", clear_on_submit=True):
            user_input  = st.text_area(label="Character Description: ", key="input", height = 100)
            submit_button = st.form_submit_button(label="Create!")

        if submit_button:

            if not user_input:
                user_input = 'Calico Jack is a 28 year old male, " A flamboyant and carefree pirate, known for his colorful clothes and love for music. He often leads a band of musicians during village celebrations."'
                
            with st.spinner("Thinking..."):
                st.write(f"Character Description: : {user_input}")

                #Build the prompt
                prompt = "game icon,mobile game ui,(head shot),((painterly)),white background,"
                prompt += user_input

                #create the character picture
                result = api.txt2img(prompt=prompt,
                    negative_prompt="tiling,poorly drawn hands,poorly drawn feet,poorly drawn face,out of frame,extra limbs,disfigured,deformed,body out of frame,bad anatomy,watermark,signature,cut off,low contrast,underexposed,overexposed,bad art,beginner,amateur,distorted face,bloodshot eyes,blurry,out of focus,circular border,",
                    cfg_scale=7,
                    width=512,
                    height=768,
                    save_images=True)
                
                #save the image to the sdresults folder
                filename = f"{uuid.uuid4()}.png"
                sdfilename = f"sdresults/{filename}"
                result.image.save(sdfilename, "PNG")

                #remove the background
                output_image = remove(result.image, session=session)

                #save the image to the nobackground folder
                nbfilename = f"nobackground/{filename}"
                output_image.save(nbfilename, "PNG")

                #display the image in StreamLit
                st.image(nbfilename)

if __name__ == "__main__":
    main()