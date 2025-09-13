from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend (if served separately) can access

answers = {
    "schedules": """Mallareddy Deemed To Be University Academic Schedules:
- Classes run Monday to Saturday.
- Semester dates and exam schedules are updated regularly on the official website.
- For exact timings and calendars, visit: <a href="https://www.mrec.ac.in/" target="_blank" rel="noopener noreferrer">https://www.mrec.ac.in/</a>""",

    "facilities": """Campus Facilities:
- Residences: On-campus hostels for students.
- Cafeteria: Multiple dining options.
- Sports: Well-maintained grounds and equipment.
- Gymnasium: Fully equipped gym.
- Activities Center: Various extracurricular activities.
- Transport: Reliable transport services.
- 24/7 Wi-Fi across campus.
- Library: Extensive academic resources.
- Auditoriums and Seminar Rooms.
- Center of Excellence for research.
- Yoga and SAAC facilities.
- CCTV Surveillance.
- ATM and Bank facilities within campus.""",

    "dining": """Dining Services:
- Various options catering to diverse tastes.
- Nutritious, affordable meals offered on campus.
- Specific menus can be found at campus cafeterias or on the official website.""",

    "library services": """Library Services:
- Central Library houses approx. 1.4 lakh books and thousands of journals.
- Digital access via Delnet, IEEE, Inflibnet, etc.
- Remote access for students and faculty.
- Library timings: 9 AM to 6 PM on working days.
- Borrowing rules apply; fines for late returns.
- Reference materials and journals non-circulating.
- "No dues" certification on clearance of dues.""",

    "administrative procedures": """Administrative Procedures:
- For admissions, fee payments, and document verification, visit the respective department or admin office.
- Detailed procedures are on the official website.
- Contact admin office for assistance.
- Website: <a href="https://www.mrec.ac.in/" target="_blank" rel="noopener noreferrer">https://www.mrec.ac.in/</a>"""
}

def get_answer(message):
    msg = message.lower()

    if any(keyword in msg for keyword in ["schedule", "timetable", "calendar", "class timing", "exam"]):
        return answers["schedules"]
    if any(keyword in msg for keyword in ["facility", "facilities", "hostel", "sports", "gym", "wifi", "transport", "auditorium", "library resources"]):
        return answers["facilities"]
    if any(keyword in msg for keyword in ["dining", "canteen", "food", "cafeteria", "meal"]):
        return answers["dining"]
    if any(keyword in msg for keyword in ["library", "books", "journals", "digital resources", "library timing", "library rules"]):
        return answers["library services"]
    if any(keyword in msg for keyword in ["administration", "administrative", "procedure", "admission", "fees", "document verification"]):
        return answers["administrative procedures"]
    return """Sorry, I don't have detailed info on that. Please visit the official website for more details:<br><a href="https://www.mrec.ac.in/" target="_blank" rel="noopener noreferrer">https://www.mrec.ac.in/</a>"""

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get("message", "")
    response = get_answer(message)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True)
