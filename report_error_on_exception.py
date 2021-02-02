from google.cloud import error_reporting

def simulate_error():
    client = error_reporting.Client()
    try:
        # simulate calling a method that's not defined
        raise NameError
    except Exception:
        client.report_exception()
