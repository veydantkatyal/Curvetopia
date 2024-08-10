import streamlit as st
import cairosvg
import gdown
from io import BytesIO
from PIL import Image, ImageOps
import xml.etree.ElementTree as ET
import plotly.express as px

# Example predefined mapping dictionary
mapping = {
    "1MLtwF0Hsq9RuVKbzuT649tQKda0frdDz": "1kJ3lMqjE74Eg9YAaamyhqet_nP0NdpMX",
    "1KcPdZIc6zfLpC0bPSn2vQZimlxKY1ttY": "1_RCfewVACYuEkImliPj_g2aIJCDrF87k",
    "1jUGSTzztSKBtEgEh5TRE5uMkAJRPFv1d": "1D34WceD8L5fpgY0dEbTYblqVf47o-9na",
    "1liOaSKsFJ5z6pN_0ojuh0QG87engRNxO": "16cGPQM-qxxs0zPPRV2engdDmytWVJk28",
    "1SYMOKqe3psGIfYuLfPyxlkV6Ra2l7RNK": "1frWuq8R5RnoSngPjut4KuDde3snKyLDt",
    "13fNvHho6ZInOTlRaWy9C0ji-QzJKF2tF": "1CVyuXn2uVVGG0O1YOqpmeOEXr0PCtcm6",
    "1U4hl7m-KPMvqShjwvkqS-9t_85u-_QHd": "1L76izM3jr-g_qMYKzk6NtbXL2KbuGoA-"
}

def extract_file_id(drive_url):
    try:
        if '/d/' in drive_url:
            return drive_url.split('/d/')[1].split('/')[0]
        elif 'id=' in drive_url:
            return drive_url.split('id=')[1]
        else:
            st.error("Invalid Google Drive link format.")
            return None
    except IndexError:
        st.error("Error extracting file ID.")
        return None

def get_output_svg_url(input_svg_url):
    input_file_id = extract_file_id(input_svg_url)
    if not input_file_id:
        return None
    output_file_id = mapping.get(input_file_id)
    if output_file_id:
        return f"https://drive.google.com/uc?export=download&id={output_file_id}"
    else:
        st.error("No matching output SVG found.")
        return None

def download_file_from_drive(drive_url):
    try:
        file_content = gdown.download(drive_url, quiet=False, fuzzy=True)
        if file_content:
            with open(file_content, 'rb') as file:
                content = file.read()
            return content
        else:
            st.error(f"Downloaded content is empty.")
            return None
    except Exception as e:
        st.error(f"Failed to download the file: {e}")
        return None

def is_valid_svg(content):
    try:
        tree = ET.ElementTree(ET.fromstring(content))
        return True
    except ET.ParseError:
        return False

def add_default_svg_size(svg_content, default_width="1000px", default_height="1000px"):
    try:
        tree = ET.ElementTree(ET.fromstring(svg_content))
        root = tree.getroot()
        if 'width' not in root.attrib:
            root.attrib['width'] = default_width
        if 'height' not in root.attrib:
            root.attrib['height'] = default_height
        if 'viewBox' not in root.attrib:
            root.attrib['viewBox'] = f"0 0 {default_width[:-2]} {default_height[:-2]}"
        svg_str = ET.tostring(root, encoding='unicode')
        return svg_str.encode('utf-8')
    except ET.ParseError as e:
        st.error(f"Failed to parse the SVG content: {e}")
        return None

def convert_svg_to_png(svg_content):
    try:
        png_data = cairosvg.svg2png(bytestring=svg_content)
        image = Image.open(BytesIO(png_data))
        image_with_background = ImageOps.expand(image, border=(10, 10, 10, 10), fill='white')
        return image_with_background
    except Exception as e:
        st.error(f"Failed to convert SVG to PNG: {e}")
        return None

def display_svg_with_zoom(png_image):
    fig = px.imshow(png_image)
    fig.update_layout(coloraxis_showscale=False, margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig, use_container_width=True)

def display_svg_pair(input_svg_url):
    input_svg_content = download_file_from_drive(input_svg_url)
    if input_svg_content:
        if is_valid_svg(input_svg_content):
            input_svg_content = add_default_svg_size(input_svg_content)
            if input_svg_content:
                input_png_image = convert_svg_to_png(input_svg_content)
                if input_png_image:
                    st.subheader("Input:")
                    display_svg_with_zoom(input_png_image)
                    output_svg_url = get_output_svg_url(input_svg_url)
                    if output_svg_url:
                        output_svg_content = download_file_from_drive(output_svg_url)
                        if output_svg_content:
                            if is_valid_svg(output_svg_content):
                                output_svg_content = add_default_svg_size(output_svg_content)
                                if output_svg_content:
                                    output_png_image = convert_svg_to_png(output_svg_content)
                                    if output_png_image:
                                        st.subheader("Expected Output:")
                                        display_svg_with_zoom(output_png_image)
                                    else:
                                        st.error("Failed to generate PNG from the output SVG content.")
                                else:
                                    st.error("Failed to parse the output SVG content.")
                            else:
                                st.error("Downloaded content is not valid SVG.")
                        else:
                            st.error("Failed to download the expected output SVG file.")
                    else:
                        st.error("No matching output SVG found for the provided input SVG.")
                else:
                    st.error("Failed to generate PNG from the input SVG content.")
            else:
                st.error("Failed to parse the input SVG content.")
        else:
            st.error("Downloaded content is not valid SVG.")
    else:
        st.error("Failed to download the input SVG file.")

def main():
    st.markdown(
        """
        <style>
        .main {
            background-color: #1E1E1E;
            color: #E1E1E1;
        }
        .css-12oz5g7 {
            background-color: #3B3B3B;
            color: #E1E1E1;
        }
        .stTextInput > div > div > input {
            background-color: #444444;
            color: #E1E1E1;
            text-align: center;
        }
        .stButton > button {
            background-color: #61dafb;
            color: #1E1E1E;
            border: none;
            padding: 10px 20px;
            text-align: center;
            font-size: 16px;
            margin: 10px 0;
            cursor: pointer;
            border-radius: 8px;
        }
        .stButton > button:hover {
            background-color: #4dabf7;
        }
        h1 {
            text-align: center;
            color: #FFFFFF;
            text-transform: uppercase;
        }
        .stHeader {
            font-size: 32px;
            color: #61dafb;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("CURVETOPIA")
    st.markdown("A cutting-edge application designed to seamlessly create, visualize, and manipulate complex curves and shapes with precision and ease.")

    st.markdown("### Enter your Google Drive link:")
    input_svg_url = st.text_input("Input Link", "")

    if input_svg_url:
        display_svg_pair(input_svg_url)

    # Link to GitHub for instructions and example links
    st.markdown("""
        [Click here](https://github.com/veydantkatyal/Curvetopia) to visit the GitHub repository for instructions and to find example Google Drive links.
    """)

    st.markdown("""
        <hr style="border-top: 1px solid #4dabf7;">
        <footer>
        <p style="text-align:center;">
        &copy; 2024 | Curvetopia
        </p>
        </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
