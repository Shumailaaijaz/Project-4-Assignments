import streamlit as st
import pandas as pd
import base64

# Set page configuration
st.set_page_config(
    page_title="Homeopathic Medical System",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to convert an image URL to base64 for CSS backgrounds
def get_base64_from_url(url):
    return f"url({url})"

# Background images
bg_main = get_base64_from_url("https://placeholder.svg?height=1080&width=1920&text=Herbal+Background")
bg_remedies = get_base64_from_url("https://placeholder.svg?height=1080&width=1920&text=Remedies+Background")
bg_principles = get_base64_from_url("https://placeholder.svg?height=1080&width=1920&text=Principles+Background")

# Enhanced CSS for better styling
st.markdown("""
<style>
    /* Main Styles */
    .stApp {
        background-image: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.9)), """ + bg_main + """;
        background-size: cover;
        background-attachment: fixed;
    }
    
    /* Typography */
    .main-header {
        font-size: 3rem;
        color: #1B5E20;
        text-align: center;
        margin-bottom: 1.5rem;
        font-family: 'Georgia', serif;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        padding: 1rem;
        border-bottom: 2px solid #81C784;
    }
    
    .sub-header {
        font-size: 2rem;
        color: #2E7D32;
        margin-top: 2rem;
        font-family: 'Georgia', serif;
        border-left: 4px solid #81C784;
        padding-left: 1rem;
    }
    
    .info-text {
        font-size: 1.1rem;
        line-height: 1.8;
        color: #212121;
        font-family: 'Roboto', sans-serif;
    }
    
    /* Cards and Containers */
    .remedy-card {
        background-color: rgba(241, 248, 233, 0.8);
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #81C784;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .remedy-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    
    .feature-container {
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: rgba(232, 245, 233, 0.85) !important;
    }
    
    /* Custom backgrounds for different pages */
    .home-bg {
        background-image: linear-gradient(rgba(255, 255, 255, 0.92), rgba(255, 255, 255, 0.92)), """ + bg_main + """;
        padding: 2rem;
        border-radius: 15px;
    }
    
    .remedies-bg {
        background-image: linear-gradient(rgba(255, 255, 255, 0.92), rgba(255, 255, 255, 0.92)), """ + bg_remedies + """;
        padding: 2rem;
        border-radius: 15px;
    }
    
    .principles-bg {
        background-image: linear-gradient(rgba(255, 255, 255, 0.92), rgba(255, 255, 255, 0.92)), """ + bg_principles + """;
        padding: 2rem;
        border-radius: 15px;
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #43A047;
        color: white;
        border-radius: 30px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        border: none;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #2E7D32;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        transform: translateY(-2px);
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: rgba(129, 199, 132, 0.2);
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        color: #1B5E20;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        padding: 1.5rem;
        background-color: rgba(46, 125, 50, 0.1);
        border-radius: 10px;
        margin-top: 2rem;
    }
    
    /* Icon styling */
    .icon {
        font-size: 2.5rem;
        color: #43A047;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    /* Quote styling */
    .quote {
        font-style: italic;
        padding: 1.5rem;
        background-color: rgba(129, 199, 132, 0.15);
        border-left: 4px solid #43A047;
        margin: 1.5rem 0;
        border-radius: 0 10px 10px 0;
    }
    
    /* Divider styling */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(to right, transparent, #81C784, transparent);
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Create enhanced navigation sidebar with icons
st.sidebar.markdown("<h1 style='text-align: center; color: #1B5E20;'>🌿 Navigation</h1>", unsafe_allow_html=True)
page = st.sidebar.radio("", ["🏠 Home", "💊 Common Remedies", "🔍 Remedy Finder", "📚 Principles", "ℹ️ About"])

# Remove the icon prefix for page logic
page = page.split(" ", 1)[1] if " " in page else page

# Home page
if page == "Home":
    st.markdown("<div class='home-bg'>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-header'>🌿 Homeopathic Medical System</h1>", unsafe_allow_html=True)
    
    # Featured quote
    st.markdown("<div class='quote'>\"The highest ideal of cure is the speedy, gentle, and enduring restoration of health by the most trustworthy and least harmful way.\" — Samuel Hahnemann, founder of Homeopathy</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
        st.markdown("<p class='info-text'>Homeopathy is a holistic medical system based on the belief that the body can cure itself. It uses highly diluted natural substances to stimulate the body's natural healing processes. Developed in the late 1700s by German physician Samuel Hahnemann, homeopathy is based on two unconventional theories:</p>", unsafe_allow_html=True)
        
        st.markdown("<h2 class='sub-header'>Key Principles</h2>", unsafe_allow_html=True)
        st.markdown("""
        <ul class='info-text'>
            <li><strong>Like Cures Like</strong> - A substance that causes symptoms in a healthy person can treat those same symptoms in a sick person</li>
            <li><strong>Law of Minimum Dose</strong> - The lower the dose of medication, the greater its effectiveness</li>
        </ul>
        """, unsafe_allow_html=True)
        
        st.markdown("<h2 class='sub-header'>How Homeopathy Works</h2>", unsafe_allow_html=True)
        st.markdown("<p class='info-text'>Homeopathic practitioners select treatments based on a total assessment of the person, considering their physical, mental, and emotional states. They tailor remedies to each individual, focusing on the whole person rather than just addressing specific symptoms or disease labels.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
        st.markdown("<div class='icon'>🌱</div>", unsafe_allow_html=True)
        st.image("https://placeholder.svg?height=300&width=300&text=Homeopathic+Remedies", use_column_width=True)
        
        st.markdown("<div class='remedy-card'><strong>Did you know?</strong><br>Homeopathy is used by over 200 million people worldwide and is recognized by the World Health Organization as the second largest therapeutic system in use.</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Featured remedies section
    st.markdown("<h2 class='sub-header'>Featured Remedies</h2>", unsafe_allow_html=True)
    
    featured_cols = st.columns(3)
    
    with featured_cols[0]:
        st.markdown("""
        <div class='remedy-card'>
            <div class='icon'>🌼</div>
            <h3 style='text-align: center; color: #2E7D32;'>Arnica Montana</h3>
            <p>The go-to remedy for bruises, injuries, and trauma. Helps reduce pain, swelling, and promotes healing.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with featured_cols[1]:
        st.markdown("""
        <div class='remedy-card'>
            <div class='icon'>🌶️</div>
            <h3 style='text-align: center; color: #2E7D32;'>Belladonna</h3>
            <p>Used for sudden, intense symptoms with redness, heat, and throbbing pain. Often used for fevers and headaches.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with featured_cols[2]:
        st.markdown("""
        <div class='remedy-card'>
            <div class='icon'>🍯</div>
            <h3 style='text-align: center; color: #2E7D32;'>Apis Mellifica</h3>
            <p>Derived from honey bee, used for swelling, stinging pain, and inflammation, especially from insect bites.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Common Remedies page
elif page == "Common Remedies":
    st.markdown("<div class='remedies-bg'>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-header'>💊 Common Homeopathic Remedies</h1>", unsafe_allow_html=True)
    
    # Introduction to remedies
    st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
    st.markdown("<p class='info-text'>Homeopathic remedies are derived from natural substances including plants, minerals, and animals. Each remedy has specific indications based on its unique symptom profile. Below are some of the most commonly used homeopathic remedies and their applications.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Create a dataframe of common remedies with more details
    remedies_data = {
        "Remedy": ["Arnica Montana", "Belladonna", "Calendula", "Chamomilla", "Nux Vomica", "Pulsatilla", "Rhus Toxicodendron", "Bryonia"],
        "Source": ["Mountain daisy", "Deadly nightshade plant", "Marigold flower", "Chamomile plant", "Poison nut", "Windflower", "Poison ivy", "White bryony"],
        "Common Uses": [
            "Bruises, muscle soreness, trauma",
            "Fever with hot, red skin; throbbing headaches",
            "Cuts, scrapes, skin irritations",
            "Teething pain, irritability, colic",
            "Digestive issues, hangover, irritability",
            "Colds, ear infections, changeable symptoms",
            "Joint pain that improves with movement",
            "Dry coughs, joint pain worse with movement"
        ],
        "Emotional Symptoms": [
            "Shock, fear after injury, denial of being ill",
            "Agitation, delirium, fearfulness",
            "Not typically used for emotional symptoms",
            "Anger, irritability, impatience",
            "Irritability, hypersensitivity, critical attitude",
            "Weepiness, desire for sympathy, changeability",
            "Restlessness, anxiety, fear of being alone",
            "Irritability, desire to be left alone"
        ],
        "Potency": [
            "6C, 30C, 200C, 1M",
            "6C, 30C, 200C",
            "Typically used as topical tincture",
            "6C, 30C, 200C",
            "6C, 30C, 200C",
            "6C, 30C, 200C",
            "6C, 30C, 200C",
            "6C, 30C, 200C"
        ]
    }
    
    remedies_df = pd.DataFrame(remedies_data)
    
    # Display remedies in an expandable format with enhanced styling
    for i, row in remedies_df.iterrows():
        with st.expander(f"🌿 {row['Remedy']} ({row['Source']})"):
            cols = st.columns([1, 2])
            
            with cols[0]:
                st.image(f"https://placeholder.svg?height=150&width=150&text={row['Remedy'].replace(' ', '+')}", use_column_width=True)
                
            with cols[1]:
                st.markdown(f"<p class='info-text'><strong>Source:</strong> {row['Source']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='info-text'><strong>Common Uses:</strong> {row['Common Uses']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='info-text'><strong>Emotional Symptoms:</strong> {row['Emotional Symptoms']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='info-text'><strong>Common Potencies:</strong> {row['Potency']}</p>", unsafe_allow_html=True)
    
    # Additional information about potencies
    st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Understanding Potencies</h2>", unsafe_allow_html=True)
    
    potency_cols = st.columns(3)
    
    with potency_cols[0]:
        st.markdown("""
        <div class='remedy-card'>
            <h3 style='text-align: center; color: #2E7D32;'>Low Potencies (6C, 12C)</h3>
            <p>Used for physical symptoms and acute conditions. May need to be taken more frequently.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with potency_cols[1]:
        st.markdown("""
        <div class='remedy-card'>
            <h3 style='text-align: center; color: #2E7D32;'>Medium Potencies (30C)</h3>
            <p>Versatile potency suitable for both physical and emotional symptoms. Most commonly used potency.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with potency_cols[2]:
        st.markdown("""
        <div class='remedy-card'>
            <h3 style='text-align: center; color: #2E7D32;'>High Potencies (200C, 1M)</h3>
            <p>Used for conditions with strong mental/emotional components. Typically taken less frequently.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Remedy Finder page
elif page == "Remedy Finder":
    st.markdown("<div class='home-bg'>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-header'>🔍 Homeopathic Remedy Finder</h1>", unsafe_allow_html=True)
    
    # Introduction
    st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
    st.markdown("<p class='info-text'>Answer a few questions to find potential homeopathic remedies that might help with your condition. This interactive tool will guide you through common symptoms and suggest remedies based on homeopathic principles.</p>", unsafe_allow_html=True)
    st.markdown("<p class='info-text' style='color: #D32F2F;'><strong>Disclaimer:</strong> This is for informational purposes only and does not replace professional medical advice.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Create tabs for different symptom categories
    tabs = st.tabs(["Physical Symptoms", "Emotional Symptoms", "Modalities", "Results"])
    
    # Physical symptoms tab
    with tabs[0]:
        st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
        st.subheader("What physical symptoms are you experiencing?")
        
        symptom_cols = st.columns(2)
        
        with symptom_cols[0]:
            pain = st.checkbox("Pain")
            if pain:
                pain_type = st.radio("What type of pain?", ["Sharp", "Dull/Aching", "Throbbing", "Burning", "Shooting"])
                pain_location = st.multiselect("Where is the pain located?", ["Head", "Joints", "Muscles", "Stomach", "Throat", "Ears", "Chest", "Back"])
            
            fever = st.checkbox("Fever")
            if fever:
                fever_intensity = st.slider("How high is your fever?", 99.0, 104.0, 100.0, 0.1)
                fever_symptoms = st.multiselect("Associated symptoms", ["Sweating", "Chills", "Flushed face", "Thirst", "No thirst"])
        
        with symptom_cols[1]:
            digestive = st.checkbox("Digestive Issues")
            if digestive:
                digestive_type = st.multiselect("What type of digestive issues?", ["Nausea", "Vomiting", "Diarrhea", "Constipation", "Bloating", "Heartburn", "Gas"])
            
            respiratory = st.checkbox("Respiratory Issues")
            if respiratory:
                respiratory_type = st.multiselect("What respiratory symptoms?", ["Cough", "Runny nose", "Congestion", "Sneezing", "Sore throat", "Shortness of breath"])
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: right;'><p>Click on 'Emotional Symptoms' tab to continue →</p></div>", unsafe_allow_html=True)
    
    # Emotional symptoms tab
    with tabs[1]:
        st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
        st.subheader("What emotional symptoms are you experiencing?")
        
        emotional = st.checkbox("Emotional Symptoms")
        if emotional:
            emotional_type = st.multiselect("Select all that apply:", ["Anxiety", "Irritability", "Sadness", "Restlessness", "Fear", "Anger", "Weepiness", "Indifference", "Oversensitivity"])
            
            if "Anxiety" in emotional_type:
                anxiety_detail = st.multiselect("What triggers your anxiety?", ["Unknown causes", "Health concerns", "Social situations", "Future events", "Past trauma"])
            
            if "Fear" in emotional_type:
                fear_detail = st.multiselect("What are you afraid of?", ["Being alone", "Crowds", "Death", "Disease", "Unknown", "Specific phobia"])
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: right;'><p>Click on 'Modalities' tab to continue →</p></div>", unsafe_allow_html=True)
    
    # Modalities tab (factors that make symptoms better or worse)
    with tabs[2]:
        st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
        st.subheader("What makes your symptoms better or worse?")
        
        better_worse_cols = st.columns(2)
        
        with better_worse_cols[0]:
            st.markdown("### Makes Better")
            better_factors = st.multiselect("Select all that apply:", ["Warmth", "Cold applications", "Pressure", "Movement", "Rest", "Fresh air", "Eating", "Drinking"])
        
        with better_worse_cols[1]:
            st.markdown("### Makes Worse")
            worse_factors = st.multiselect("Select all that apply:", ["Warmth", "Cold", "Pressure", "Movement", "Rest", "Noise", "Light", "Before storms", "At night", "In morning"])
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: right;'><p>Click on 'Results' tab to see recommendations →</p></div>", unsafe_allow_html=True)
    
    # Results tab
    with tabs[3]:
        st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
        st.subheader("Your Personalized Remedy Recommendations")
        
        # Add a button to find remedies
        if st.button("Generate Recommendations"):
            st.markdown("<h3 class='sub-header'>Potential Remedies</h3>", unsafe_allow_html=True)
            
            # Simple logic to suggest remedies based on symptoms
            suggested_remedies = []
            
            # Check if variables exist before using them
            if 'pain' in locals() and pain:
                if 'pain_type' in locals() and 'pain_location' in locals():
                    if pain_type == "Sharp" and "Head" in pain_location:
                        suggested_remedies.append(("Belladonna", "For sharp, throbbing headaches that come on suddenly", "🔴"))
                    if pain_type == "Dull/Aching" and any(loc in pain_location for loc in ["Joints", "Muscles"]):
                        suggested_remedies.append(("Arnica Montana", "For sore muscles and joint pain, especially after injury or overexertion", "🌼"))
                    if pain_type == "Burning":
                        suggested_remedies.append(("Cantharis", "For burning pains, especially in the urinary tract", "🔥"))
                    if pain_type == "Shooting" and "Nerves" in pain_location:
                        suggested_remedies.append(("Hypericum", "For shooting nerve pain, injuries to nerve-rich areas", "🌿"))
            
            if 'fever' in locals() and fever:
                if 'fever_intensity' in locals() and 'fever_symptoms' in locals():
                    if fever_intensity > 101.5 and "Flushed face" in fever_symptoms:
                        suggested_remedies.append(("Belladonna", "For high fevers with hot, red skin and throbbing sensations", "🔴"))
                    elif "Sweating" in fever_symptoms:
                        suggested_remedies.append(("Ferrum Phosphoricum", "For mild fevers with sweating", "🧪"))
                    elif "Chills" in fever_symptoms:
                        suggested_remedies.append(("Aconitum Napellus", "For sudden fevers with chills, especially after exposure to cold", "❄️"))
            
            if 'digestive' in locals() and digestive:
                if 'digestive_type' in locals():
                    if "Nausea" in digestive_type or "Vomiting" in digestive_type:
                        suggested_remedies.append(("Ipecacuanha", "For persistent nausea with or without vomiting", "🌱"))
                    if "Constipation" in digestive_type:
                        suggested_remedies.append(("Nux Vomica", "For constipation with ineffectual urging", "🌰"))
                    if "Diarrhea" in digestive_type:
                        suggested_remedies.append(("Arsenicum Album", "For diarrhea with burning sensations, especially after food poisoning", "⚗️"))
            
            if 'emotional' in locals() and emotional:
                if 'emotional_type' in locals():
                    if "Anxiety" in emotional_type:
                        suggested_remedies.append(("Aconite", "For sudden anxiety and panic, especially after shock", "🌀"))
                    if "Irritability" in emotional_type:
                        suggested_remedies.append(("Chamomilla", "For irritability and impatience, especially with pain", "🌼"))
                    if "Weepiness" in emotional_type:
                        suggested_remedies.append(("Pulsatilla", "For weepiness, desire for sympathy, and changeable symptoms", "🌸"))
            
            # Display the suggested remedies with enhanced styling
            if suggested_remedies:
                for remedy, description, emoji in suggested_remedies:
                    st.markdown(f"""
                    <div class='remedy-card'>
                        <h3 style='text-align: center; color: #2E7D32;'>{emoji} {remedy}</h3>
                        <p style='text-align: center;'>{description}</p>
                        <hr style='width: 50%; margin: 1rem auto;'>
                        <p style='text-align: center; font-size: 0.9rem;'>Typical potency: 30C, taken 3-4 times daily for acute conditions</p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No specific remedies found for your combination of symptoms. Please consult with a qualified homeopathic practitioner for personalized advice.")
            
            st.markdown("""
            <div style='background-color: rgba(255, 248, 225, 0.8); padding: 1rem; border-radius: 10px; border-left: 5px solid #FFA000; margin-top: 2rem;'>
                <h4 style='color: #F57C00;'>Important Reminder</h4>
                <p>This tool provides general information only. For proper homeopathic treatment, consult with a qualified homeopathic practitioner who can take your full case history and prescribe the most appropriate remedy.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Fill out the symptom information in the previous tabs, then click 'Generate Recommendations' to see suggested remedies.")
        
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Principles page
elif page == "Principles":
    st.markdown("<div class='principles-bg'>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-header'>📚 Principles of Homeopathy</h1>", unsafe_allow_html=True)
    
    # Introduction
    st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
    st.markdown("<p class='info-text'>Homeopathy is founded on several key principles that guide its practice and philosophy. These principles were established by Dr. Samuel Hahnemann in the late 18th century and continue to form the foundation of homeopathic medicine today.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Core principles with icons
    principles_cols = st.columns(2)
    
    with principles_cols[0]:
        st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
        st.markdown("<div class='icon'>🔄</div>", unsafe_allow_html=True)
        st.markdown("<h2 class='sub-header'>The Law of Similars</h2>", unsafe_allow_html=True)
        st.markdown("<p class='info-text'>The principle of 'like cures like' (similia similibus curentur) is the foundation of homeopathy. It suggests that a substance that causes symptoms in a healthy person can treat similar symptoms in a sick person.</p>", unsafe_allow_html=True)
        st.markdown("<p class='info-text'>For example, while cutting an onion causes watery eyes and a runny nose, a homeopathic preparation of onion (Allium cepa) might be used to treat cold or allergy symptoms that include watery eyes and a runny nose.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with principles_cols[1]:
        st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
        st.markdown("<div class='icon'>⚗️</div>", unsafe_allow_html=True)
        st.markdown("<h2 class='sub-header'>The Principle of Dilution</h2>", unsafe_allow_html=True)
        st.markdown("<p class='info-text'>Homeopathic remedies are prepared through a process of serial dilution and succussion (vigorous shaking). The more diluted a substance becomes, the more potent its healing properties are believed to be.</p>", unsafe_allow_html=True)
        st.markdown("<p class='info-text'>This process, known as potentization, is thought to release the dynamic force of the substance while removing its potentially harmful effects.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    principles_cols2 = st.columns(2)
    
    with principles_cols2[0]:
        st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
        st.markdown("<div class='icon'>👤</div>", unsafe_allow_html=True)
        st.markdown("<h2 class='sub-header'>Individualization of Treatment</h2>", unsafe_allow_html=True)
        st.markdown("<p class='info-text'>Homeopathy treats the person as a whole, not just the disease. Two people with the same condition might receive different remedies based on their specific symptoms, constitution, and emotional state.</p>", unsafe_allow_html=True)
        st.markdown("<p class='info-text'>This individualized approach is central to homeopathic practice and requires a detailed case-taking process to understand the unique symptom picture of each person.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with principles_cols2[1]:
        st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
        st.markdown("<div class='icon'>💧</div>", unsafe_allow_html=True)
        st.markdown("<h2 class='sub-header'>Minimum Dose</h2>", unsafe_allow_html=True)
        st.markdown("<p class='info-text'>Homeopathy uses the minimum dose needed to stimulate the body's self-healing response. This approach aims to avoid side effects while triggering the body's natural healing mechanisms.</p>", unsafe_allow_html=True)
        st.markdown("<p class='info-text'>Practitioners often start with lower potencies and move to higher ones as needed, always seeking the smallest amount necessary to stimulate healing.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Holistic approach with visual representation
    st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
    st.markdown("<div class='icon'>🌍</div>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Holistic Approach</h2>", unsafe_allow_html=True)
    
    holistic_cols = st.columns([1, 2])
    
    with holistic_cols[0]:
        st.image("https://placeholder.svg?height=300&width=300&text=Holistic+Health", use_column_width=True)
    
    with holistic_cols[1]:
        st.markdown("<p class='info-text'>Homeopathy considers physical, mental, and emotional aspects of a person's health. It recognizes the interconnectedness of body systems and the influence of mental and emotional states on physical health.</p>", unsafe_allow_html=True)
        
        st.markdown("""
        <p class='info-text'>The holistic approach considers:</p>
        <ul class='info-text'>
            <li><strong>Physical symptoms</strong> - Their exact nature, location, and modalities (what makes them better or worse)</li>
            <li><strong>Mental state</strong> - Thought patterns, cognitive function, and mental symptoms</li>
            <li><strong>Emotional state</strong> - Feelings, reactions, and emotional tendencies</li>
            <li><strong>Environmental factors</strong> - How external conditions affect the person</li>
            <li><strong>Constitution</strong> - The inherent nature and tendencies of the individual</li>
        </ul>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Visual representation of potentization
    st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>The Potentization Process</h2>", unsafe_allow_html=True)
    
    potency_steps = st.columns(4)
    
    with potency_steps[0]:
        st.markdown("""
        <div style='text-align: center;'>
            <div class='icon'>🌿</div>
            <h4>1. Source Material</h4>
            <p>Starting with raw plant, mineral, or animal substance</p>
        </div>
        """, unsafe_allow_html=True)
    
    with potency_steps[1]:
        st.markdown("""
        <div style='text-align: center;'>
            <div class='icon'>🧪</div>
            <h4>2. Extraction</h4>
            <p>Creating mother tincture through extraction process</p>
        </div>
        """, unsafe_allow_html=True)
    
    with potency_steps[2]:
        st.markdown("""
        <div style='text-align: center;'>
            <div class='icon'>💧</div>
            <h4>3. Dilution</h4>
            <p>Serial dilution in water/alcohol solution</p>
        </div>
        """, unsafe_allow_html=True)
    
    with potency_steps[3]:
        st.markdown("""
        <div style='text-align: center;'>
            <div class='icon'>🔄</div>
            <h4>4. Succussion</h4>
            <p>Vigorous shaking between each dilution</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# About page
elif page == "About":
    st.markdown("<div class='home-bg'>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-header'>ℹ️ About Homeopathy</h1>", unsafe_allow_html=True)
    
    # Introduction with timeline
    st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
    st.markdown("<p class='info-text'>Homeopathy was developed in the late 18th century by Samuel Hahnemann, a German physician who was dissatisfied with the harsh medical practices of his time, which included bloodletting and the use of toxic chemicals.</p>", unsafe_allow_html=True)
    
    # Timeline
    st.markdown("<h2 class='sub-header'>Historical Timeline</h2>", unsafe_allow_html=True)
    
    timeline_cols = st.columns(4)
    
    with timeline_cols[0]:
        st.markdown("""
        <div class='remedy-card'>
            <h3 style='text-align: center; color: #2E7D32;'>1755-1843</h3>
            <p>Samuel Hahnemann's lifetime. German physician who founded homeopathy after becoming disillusioned with conventional medicine of his time.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with timeline_cols[1]:
        st.markdown("""
        <div class='remedy-card'>
            <h3 style='text-align: center; color: #2E7D32;'>1796</h3>
            <p>First publication on the principle of "like cures like" after Hahnemann's experiments with cinchona bark (quinine).</p>
        </div>
        """, unsafe_allow_html=True)
    
    with timeline_cols[2]:
        st.markdown("""
        <div class='remedy-card'>
            <h3 style='text-align: center; color: #2E7D32;'>1810</h3>
            <p>Publication of the "Organon of the Healing Art," Hahnemann's comprehensive text on homeopathic principles.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with timeline_cols[3]:
        st.markdown("""
        <div class='remedy-card'>
            <h3 style='text-align: center; color: #2E7D32;'>1825-1900</h3>
            <p>Rapid spread of homeopathy throughout Europe and to America, where it became highly popular.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # History section
    st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>History</h2>", unsafe_allow_html=True)
    
    history_cols = st.columns([1, 2])
    
    with history_cols[0]:
        st.image("https://placeholder.svg?height=300&width=300&text=Samuel+Hahnemann", use_column_width=True)
        st.markdown("<p style='text-align: center; font-style: italic;'>Samuel Hahnemann (1755-1843)<br>Founder of Homeopathy</p>", unsafe_allow_html=True)
    
    with history_cols[1]:
        st.markdown("<p class='info-text'>Hahnemann discovered the principle of 'like cures like' when he found that cinchona bark, which was used to treat malaria, produced malaria-like symptoms when taken by healthy individuals. This observation led him to develop the homeopathic system of medicine.</p>", unsafe_allow_html=True)
        
        st.markdown("<p class='info-text'>Through systematic experimentation, Hahnemann developed a method of 'proving' remedies by testing them on healthy volunteers and recording all symptoms produced. These detailed symptom pictures became the basis for matching remedies to patients' symptoms.</p>", unsafe_allow_html=True)
        
        st.markdown("<p class='info-text'>Homeopathy spread rapidly throughout Europe and to America in the 19th century, with dedicated hospitals and medical schools. By the early 20th century, there were 22 homeopathic medical schools and over 100 homeopathic hospitals in the United States alone.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Scientific perspective and current practice
    science_cols = st.columns(2)
    
    with science_cols[0]:
        st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
        st.markdown("<h2 class='sub-header'>Scientific Perspective</h2>", unsafe_allow_html=True)
        st.markdown("<p class='info-text'>It's important to note that the scientific community has varying views on homeopathy. Many conventional scientists and medical practitioners question its effectiveness beyond placebo effects, particularly due to the high dilutions used in remedies, which often contain no detectable amount of the original substance.</p>", unsafe_allow_html=True)
        
        st.markdown("<p class='info-text'>The mechanism of action proposed by homeopathy does not align with current understanding of chemistry and physics, which has led to scientific skepticism. However, research continues, with some studies suggesting effects beyond placebo for certain conditions.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with science_cols[1]:
        st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
        st.markdown("<h2 class='sub-header'>Current Practice</h2>", unsafe_allow_html=True)
        st.markdown("<p class='info-text'>Despite scientific debates, homeopathy remains popular in many countries and is integrated into national health systems in places like India, Switzerland, and parts of Europe. Many people report benefits from homeopathic treatments, and research continues to explore its mechanisms and effectiveness.</p>", unsafe_allow_html=True)
        
        st.markdown("<p class='info-text'>Today, homeopathy is practiced by licensed physicians, naturopathic doctors, and specialized homeopathic practitioners. It is often used as a complementary approach alongside conventional medicine, particularly for chronic conditions, pediatric care, and cases where conventional treatments have limitations.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Disclaimer
    st.markdown("<div class='feature-container' style='background-color: rgba(255, 243, 224, 0.9);'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Disclaimer</h2>", unsafe_allow_html=True)
    st.markdown("<p class='info-text'>This website is for informational purposes only. It is not intended to provide medical advice or to replace consultation with a qualified healthcare professional. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.</p>", unsafe_allow_html=True)
    
    st.markdown("<p class='info-text'>The information presented here aims to provide an educational overview of homeopathy as a medical system. It does not endorse or reject homeopathy as a treatment option, and readers are encouraged to research and consult with healthcare providers to make informed decisions about their health.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Footer with enhanced styling
st.markdown("<div class='footer'>", unsafe_allow_html=True)
st.markdown("<p>© 2025 Homeopathic Medical System Information | Educational Purposes Only</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 0.9rem; margin-top: 0.5rem;'>Created with Streamlit | All rights reserved</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)