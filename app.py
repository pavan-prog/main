import streamlit as st

# Home Page
def home_page():
    st.title("Face and Signature Authentication")

    if st.button("Authenticate Face"):
        st.subheader("Upload an Image")
        uploaded_face_image = st.file_uploader("Upload a face image", type=["jpg", "png"])

        if uploaded_face_image is not None:
            st.subheader("Proceed with Face Recognition")
            if st.button("Proceed"):
                # Perform face recognition here
                st.success("Face recognized: XXXXX")
                st.session_state.signature_button = True

# Signature Page
def signature_page():
    st.title("Signature Authentication")

    if st.button("Authenticate Signature"):
        st.subheader("Upload an Image")
        uploaded_signature_image = st.file_uploader("Upload a signature image", type=["jpg", "png"])

        if uploaded_signature_image is not None:
            # Perform signature verification here
            st.success("Signature is verified")
            st.success("Authentication successful")

def main():
    st.set_page_config(page_title="Authentication App", layout="centered")

    if "signature_button" not in st.session_state:
        st.session_state.signature_button = False

    home_page()

    if st.session_state.signature_button:
        signature_page()

if __name__ == "__main__":
    main()
