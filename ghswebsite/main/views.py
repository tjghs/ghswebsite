from django.shortcuts import render

from announcements.models import Announcement


def index(request):
    announcements = Announcement.objects.all()
    return render(request, "index.html", {
        'announcements': announcements
    })

# @app.route("/hours/")
# def hours():
#     if "oauth_token" in session:
#         profile_json = session.get("profile")
#         users = User.query.filter_by(username=profile_json['ion_username'])
#         hours = []
#         if users.count() == 0:
#             newUser = User(
#                 profile_json['first_name'],
#                 profile_json['last_name'],
#                 profile_json['ion_username'],
#                 [])
#             db.session.add(newUser)
#             db.session.commit()
#             print("New user " + profile_json['ion_username'] + " created.")
#         else:
#             hours = Hour.query.filter_by(user=users[0].id)
#         return render_template("hours.html", prefix=ROOT_URL, hours=hours)

#     return redirect(url_for("login", next="hours"))


# @app.route("/slideshow/<path:path>")
# def slideshow(path):
#     return send_from_directory("slideshow", path)


# @app.route("/admin/", methods=["GET", "POST"])
# def admin():
#     if request.method == "GET":
#         if "oauth_token" in session:
#             # profile_json = session.get("profile", {})
#             username = session.get("username", {})
#             admins = ["2018wzhang", "2018nzhou"]
#             if username in admins:
#                 announcements = Announcement.query.all()
#                 hours = Hour.query.all()
#                 users = []
#                 for hour in hours:
#                     users.append(
#                         User.query.filter_by(
#                             id=hour.user)[0].username)
#                 return render_template(
#                     "admin.html", prefix=ROOT_URL,
#                     announcements=announcements, users=users,
#                     hours=hours)
#             return "Unauthorized"

#         return redirect(url_for("login", next="admin"))
#     elif request.method == "POST":
