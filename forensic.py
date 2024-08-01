import io


def write_output(output, content):
    if isinstance(output, io.StringIO):
        output.write(content)
    elif output:
        with open(output, 'w') as f:
            f.write(content)
    else:
        print(content)


def extract_strings(file_path, output=None):
    try:
        content = f"Extracting strings from {file_path}"
        write_output(output, content)
    except Exception as e:
        write_output(output, f"An error occurred: {e}")


def extract_metadata(file_path, output=None):
    try:
        content = f"Extracting metadata from {file_path}"
        write_output(output, content)
    except Exception as e:
        write_output(output, f"An error occurred: {e}")
