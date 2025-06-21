import streamlit as st

def show_flashcards():
    st.subheader("🃏 Flashcards")

    cards = [
        ("Gravity", "Force pulling objects toward each other."),
        ("Photosynthesis", "Process plants use to convert light into energy."),
        ("Mitosis", "Cell division that results in two identical daughter cells."),
        ("Neuron", "Basic working unit of the brain, a nerve cell."),
        ("Algorithm", "A set of rules to solve a problem step-by-step."),
        ("Binary", "A number system using only 0s and 1s."),
        ("CPU", "Central Processing Unit, the brain of a computer."),
        ("Internet", "Global network connecting millions of computers."),
        ("World War II", "A global conflict from 1939 to 1945."),
        ("Mahatma Gandhi", "Leader of India's non-violent independence movement."),
        ("Water Cycle", "Continuous movement of water on, above, and below Earth's surface."),
        ("Ecosystem", "A community of living and non-living things working together."),
        ("Solar System", "Group of planets orbiting the sun."),
        ("Democracy", "Form of government where people elect their leaders."),
        ("Python", "A high-level programming language used in AI, web dev, and more."),
    ]

    for term, definition in cards:
        with st.expander(term):
            st.write(definition)
