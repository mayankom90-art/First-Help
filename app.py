import streamlit as st

st.header("Welcome!")
st.title("Indian Red Cross First Aid")

video_data = {
    "asthma": "https://youtu.be/CAcwoaylH9o?si=sGFn_-wG-e2fmKFZ",
    "allergies": "https://youtu.be/r_qNTFa13uQ?si=nk6wyfNaSle6b3Qq",
    "bites and stings": "https://youtu.be/7Fh3v5c6FY4?si=vPJ95iVTLc17fMI7",
    "bleeding": "https://youtu.be/V8KiNURVjgk?si=yKr3W57zUGlO2P8m",
    "bone, muscle and joint injuries": "https://youtu.be/N-FY78--JWw?si=XVu890Za0yss0gQO",
    "burns and scalds": "https://youtu.be/TLr2qsEhpC8?si=7bCZyaXTqYAANGK9",
    "chest pain": "https://youtu.be/ZhO-c4z-lDM?si=_Z-tHvH8fjVB4K3W",
    "choking": "https://youtu.be/j45WfhxK_Hs?si=-KoeCNxfOPymsyea",
    "head injuries": "https://youtu.be/KeZXgE9q6eo?si=k7iqpRGmgJgIUAPh",
    "treat shock": "https://youtu.be/61urGQrmeNM?si=59Nsjsx8-6_RpGKb",
    "cpr": "https://youtu.be/HoInMN9E9Yk?si=UlMVYR0bzIxhuAS3",
    "snake bite": "https://youtu.be/nH8o-bgwo_g?si=AY8upKFEcTaI5HGI",
    "dog bite": "https://youtu.be/J5AeWWQ3eN0?si=I-m0Ve4G6M7kEjfc",
    "seizure": "https://youtu.be/Ovsw7tdneqE?si=71ndEow2QxaM7DbE",
    "dislocation/fracture": "https://youtu.be/sPzXAVNVJr0?si=E-WJGCa5O0mTLl0l"
}


query = st.text_input("Type any first-aid topic (example: asthma, bleeding, CPR, dog bite...)")

if st.button("Search"):
    key = query.strip().lower()

    if key in video_data:
        url = video_data[key]

        if "youtu.be" in url:
            video_id = url.split("/")[-1].split("?")[0]
        else:
            video_id = url.split("v=")[-1].split("&")[0]

        st.video(f"https://www.youtube.com/embed/{video_id}", autoplay=True)

    else:
        st.error("No video found. Please type one of the listed first-aid topics.")
