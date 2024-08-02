from flask import Flask, request, jsonify
from flask_cors import CORS
import malware
import forensic
import io
import os

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    analysis_type = request.form.get('analysis_type')
    operation = request.form.get('operation')

    # Save the uploaded file temporarily
    temp_path = f"/tmp/{file.filename}"
    file.save(temp_path)

    # Perform the selected analysis
    output = io.StringIO()
    result = {}

    try:
        if analysis_type == 'malware':
            if operation == 'strings':
                malware.extract_strings(temp_path, output)
            elif operation == 'entropy':
                malware.calculate_entropy(temp_path, output)
            elif operation == 'headers':
                malware.enumerate_headers(temp_path, output)
            elif operation == 'language':
                malware.determine_language(temp_path, output)
            elif operation == 'sections':
                malware.analyze_sections(temp_path, output)
            elif operation == 'packer':
                malware.detect_packer(temp_path, output)
            elif operation == 'imports':
                malware.list_imports(temp_path, output)
            elif operation == 'exports':
                malware.list_exports(temp_path, output)
            elif operation == 'yara':
                yara_dir = request.form.get('yara_dir')
                if not yara_dir:
                    return jsonify({'error': 'YARA directory not specified'}), 400
                malware.search_yara_signatures(temp_path, yara_dir, output)
            else:
                return jsonify({'error': 'Invalid operation for malware analysis'}), 400
        elif analysis_type == 'forensic':
            if operation == 'strings':
                forensic.extract_strings(temp_path, output)
            elif operation == 'metadata':
                forensic.extract_metadata(temp_path, output)
            else:
                return jsonify({'error': 'Invalid operation for forensic analysis'}), 400
        else:
            return jsonify({'error': 'Invalid analysis type'}), 400

        result['output'] = output.getvalue()
    except Exception as e:
        result['error'] = str(e)
    finally:
        # Clean up the temporary file
        os.remove(temp_path)

    return jsonify(result)


application = app