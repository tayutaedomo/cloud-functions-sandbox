import os
import tempfile
from werkzeug.utils import secure_filename


#
# Refer
#   - https://cloud.google.com/functions/docs/tutorials/http?hl=ja
#   - https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/functions/helloworld/main.py
#
def hello_get(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    return 'Hello World!'


#
# Refer:
#   - https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/functions/http/main.py#L68
#
def parse_multipart(request):
    """ Parses a 'multipart/form-data' upload request
    Args:
        request (flask.Request): The request object.
    Returns:
        The response text, or any set of values that can be turned into a
         Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """

    # This code will process each non-file field in the form
    fields = {}
    data = request.form.to_dict()
    for field in data:
        fields[field] = data[field]
        print('Processed field: %s' % field)

    # This code will process each file uploaded
    size = 0
    files = request.files.to_dict()
    for file_name, file in files.items():
        # Note: GCF may not keep files saved locally between invocations.
        # If you want to preserve the uploaded files, you should save them
        # to another location (such as a Cloud Storage bucket).
        #file.save(get_file_path(file_name))
        #print('Processed file: %s' % file_name)
        size = len(file.read())
        print('Processed file size: %s' % size)

    # Clear temporary directory
    #for file_name in files:
    #    file_path = get_file_path(file_name)
    #    os.remove(file_path)

    #return "Done!"
    return "Done! size:%s" % size

# Helper function that computes the filepath to save files to
def get_file_path(filename):
    # Note: tempfile.gettempdir() points to an in-memory file system
    # on GCF. Thus, any files in it must fit in the instance's memory.
    file_name = secure_filename(filename)
    return os.path.join(tempfile.gettempdir(), file_name)

