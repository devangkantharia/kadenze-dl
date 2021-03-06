import helpers

def test_extract_filename():
    video_url = "https://cdnc-prod-assets-private.kadenze.com/uploads/lecture_medium/4894/file/Reb_L5_720.mp4?Expires" \
                "=1482662443\u0026Signature=QklHU9hV7z2gwVp9yYfN21IITWxPZnPa7c3QOUByerXthMHnGy7-PfWvw~jrk5bE6sNtj2uee" \
                "gCiGNsusW3ummw0zQoNzO4e592eduSgP6SuN0axaqsdqiYGHHDG0dExRD~DepPmG1vSat2lJ3d8SOA0mYOfYMYz5Qk-oJd-wRHsx" \
                "LQPKLhTW5sOD6OjSSajr7Qruu0s5Ej-5WKm4XLdLORz6q~OJEnye~ra~HsXhxqOfEDxoUYojvQZZNVdSRXUSZigEJ7vgYyNop-N7" \
                "~HVRUGjXU~Z~NsB3LtFctaEvoNWd3CMVH~zwHmTKEF1rmDDb2To~ABS6t8sXREUdZ36pQ__\u0026Key-Pair-Id=APKAIPB43QU" \
                "CA2NXZVSQmp4"
    filename = helpers.extract_filename(video_url)
    assert filename == "Reb_L5_720.mp4"


def test_courses_from_json():
    course_json = '{"courses": [{"course_path": "/courses/creative-applications-of-deep-learning-with-tensorflow-i"}]}'
    courses = helpers.get_courses_from_json(course_json)
    assert courses == ["/courses/creative-applications-of-deep-learning-with-tensorflow-i"]


