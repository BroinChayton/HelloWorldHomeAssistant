from flask import Flask, render_template_string
app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
  <head>
    <title>Hello World Add-on</title>
    <script>
      function sayHello() {
        alert("Hello World!");
      }
    </script>
  </head>
  <body>
    <h1>Hello from Add-on</h1>
    <button onclick="sayHello()">Hello</button>
  </body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
