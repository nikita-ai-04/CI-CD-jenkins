from flask import Flask
app = Flask(_name_)

@app.route(*/*)
def Hello():
  return "Hello World from Jenkins CI/CD!"

if _name_ == "_main_":
  app.run(host="0.0.0.0",port=5000)

