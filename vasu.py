import streamlit as st

# Title of the application
st.title("Vasu Organics Healthcare Chatbot")

# Welcome message with color
st.markdown(
    "<h2 style='color: #4CAF50;'>Welcome to the Vasu Organics Healthcare Chatbot!</h2>",
    unsafe_allow_html=True
)
st.write("How can I assist you today?")

# Company information
company_info = (
    "### Raising a Hope in the Hearts of Millions\n"
    "A strong heritage of nearly three decades adds impetus to Vasu Group’s colossal success. "
    "A pioneer in pharmaceutical distribution, the group's strength lies in delivering top-of-the-line customer service through quality management, "
    "quick response, and on-time delivery. Vasu Group has ventured into new verticals to distribute healthcare and specialty products of many reputed companies.\n\n"
    
    "### The Evolution\n"
    "The humble beginnings of this organization trace back to 'Vasu Medical & General Store.' "
    "Mr. Bhanu Murthy, the dynamic visionary, launched the store at the young age of 21 in 1985, with the inspiration and assistance of Sri Gudala Krishnamurthy Garu.\n"
    
    "As the business flourished, it required more hands, leading to partnerships and expansion. "
    "Vasu Group's commitment to quality and service has helped carve a niche in the industry.\n\n"
    
    "### Our Team\n"
    "The dedication of the team, combined with experience and international exposure in the pharmaceutical industry, has been vital to our success.\n\n"
    
    "### Contact Us\n"
    "Vasu Organics Pvt. Ltd,  \n"
    "Vasu's Pharma House,  \n"
    "#3-6-516/4, 5th Floor, St. No.6,  \n"
    "Himayath Nagar, Hyderabad - 500 029  \n"
    "Fax: 040 - 27676163  \n"
    "Email: [info@vasuorganics.com](mailto:info@vasuorganics.com)"
)

# Function to display company information
def display_company_info():
    st.markdown(company_info)

# Function to display product information
def display_products():
    st.subheader("Vasu Organics Medicines List")

    medicines = {
        "Digestive Medicines": [
            "Liver Detox: Herbal capsules for liver health and detoxification.",
            "Digestive Tonic: Formulations that promote digestion and relieve bloating."
        ],
        "Respiratory Medicines": [
            "Cough Syrup: Herbal syrup for soothing cough and throat irritation.",
            "Bronchial Support: Ayurvedic products for respiratory health."
        ],
        "Immunity Boosters": [
            "Immunity Booster Capsules: Natural supplements for enhancing immune function.",
            "Tulsi Drops: Concentrated extract for respiratory and immune support."
        ],
        "Stress Relief": [
            "Ashwagandha Capsules: Herbal capsules for stress relief and mental clarity.",
            "Brahmi Capsules: Supplements that promote cognitive function and reduce anxiety."
        ],
        "Joint and Muscle Support": [
            "Joint Support Tablets: Ayurvedic formulations for joint health and mobility.",
            "Pain Relief Balm: Topical ointment for muscle pain relief."
        ],
        "Skin Care Medicines": [
            "Herbal Face Wash: Natural cleanser for acne-prone skin.",
            "Herbal Ointment: For the treatment of minor skin irritations and wounds."
        ],
        "Women’s Health": [
            "Menstrual Support Tablets: Herbal formulations for menstrual health.",
            "Menopause Support: Supplements for managing menopause symptoms."
        ],
        "Children’s Health": [
            "Immunity Syrup for Kids: Herbal syrup to boost immunity in children.",
            "Digestive Support: Formulations for improving digestion in children."
        ],
        "Diabetes Management": [
            "Blood Sugar Support Capsules: Ayurvedic formulations to help manage blood sugar levels."
        ],
        "Cardiovascular Health": [
            "Heart Health Tablets: Herbal supplements supporting cardiovascular function."
        ],
        "Cold and Flu Remedies": [
            "Cold Relief Capsules: Natural remedies for cold and flu symptoms."
        ]
    }

    for category, items in medicines.items():
        st.markdown(f"<h4 style='color: #FF5733;'>{category}</h4>", unsafe_allow_html=True)
        for item in items:
            st.write(f"- {item}")

# Input box for user questions
user_input = st.text_input("Ask me about our products, medicines, company information, or any health-related queries:")

if user_input:
    user_input_lower = user_input.lower()

    if "products" in user_input_lower or "catalog" in user_input_lower:
        st.write("Here are our products:")
        display_products()
    elif "medicines" in user_input_lower:
        st.write("Here is the list of medicines offered by Vasu Organics:")
        display_products()
    elif "company" in user_input_lower or "information" in user_input_lower:
        st.write("Here is some information about Vasu Organics:")
        display_company_info()
    else:
        st.write("I'm sorry, I can only provide information about our products, medicines, and company details. Please ask about our offerings.")

# Footer with contact information
st.write("---")
st.subheader("Contact Us")
st.markdown(
    "<p style='color: #333;'>For more information, reach out to us at:</p>",
    unsafe_allow_html=True
)
st.write("Email: info@vasuorganics.com")




