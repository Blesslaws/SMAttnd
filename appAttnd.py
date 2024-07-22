from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from io import BytesIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
db = SQLAlchemy(app)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50), nullable=False)
            location = db.Column(db.String(50), nullable=False)
                department = db.Column(db.String(50), nullable=False)
                    date = db.Column(db.String(50), nullable=False)
                        sign_in = db.Column(db.String(50), nullable=False)
                            sign_off = db.Column(db.String(50), nullable=False)

                            @app.route('/submit', methods=['POST'])
                            def submit():
                                data = request.get_json()
                                    new_entry = Attendance(**data)
                                        db.session.add(new_entry)
                                            db.session.commit()
                                                return jsonify({"message": "Attendance recorded successfully!"}), 201

                                                @app.route('/dashboard', methods=['GET'])
                                                def dashboard():
                                                    records = Attendance.query.all()
                                                        data = pd.DataFrame([{
                                                                    "name": record.name,
                                                                            "location": record.location,
                                                                                    "department": record.department,
                                                                                            "date": record.date,
                                                                                                    "sign_in": record.sign_in,
                                                                                                            "sign_off": record.sign_off
                                                        } for record in records])

                                                            if not data.empty:
                                                                    data['sign_in'] = pd.to_datetime(data['sign_in'])
                                                                            data['sign_off'] = pd.to_datetime(data['sign_off'])
                                                                                    data['working_hours'] = (data['sign_off'] - data['sign_in']).dt.seconds / 3600

                                                                                            avg_hours = data.groupby('department')['working_hours'].mean().tolist()
                                                                                                    labels = data['department'].unique().tolist()

                                                                                                            return jsonify({"avg_hours": avg_hours, "labels": labels})

                                                                                                                return jsonify({"avg_hours": [], "labels": []})

                                                                                                                @app.route('/export', methods=['GET'])
                                                                                                                def export():
                                                                                                                    records = Attendance.query.all()
                                                                                                                        data = pd.DataFrame([{
                                                                                                                                    "Name": record.name,
                                                                                                                                            "Location": record.location,
                                                                                                                                                    "Department": record.department,
                                                                                                                                                            "Date": record.date,
                                                                                                                                                                    "Sign-In Time": record.sign_in,
                                                                                                                                                                            "Sign-Off Time": record.sign_off
                                                                                                                        } for record in records])

                                                                                                                            output = BytesIO()
                                                                                                                                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                                                                                                                                        data.to_excel(writer, index=False, sheet_name='Attendance')
                                                                                                                                            output.seek(0)

                                                                                                                                                return send_file(output, attachment_filename="attendance.xlsx", as_attachment=True)

                                                                                                                                                if __name__ == '__main__':
                                                                                                                                                    db.create_all()
                                                                                                                                                        app.run(debug=True)
                                                                                                                                                        
                                                                                                                        }])
                                                        }])