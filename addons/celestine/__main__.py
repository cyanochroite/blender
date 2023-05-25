""""""
import os
import sys

sys.path[0] = os.path.dirname(sys.path[0])

celestine = __import__("celestine")
celestine.main(sys.argv[1:], True)



def logo():
    base = "/todoapp/content/images"
    img = request.args.get('image_name')
    safepath = os.path.realpath(img)
    prefix = os.path.commonpath(base, safepath)

    if prefix == base:
      return send_file(os.path.join(base, safepath))


  f = request.files['file']
  filename = secure_filename(f.filename)


def allowed_file(filename):
    return os.path.splitext(filename)[1] in app.config["ALLOWED_EXTENSIONS"]
