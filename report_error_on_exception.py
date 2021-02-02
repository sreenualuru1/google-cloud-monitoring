# [START error_reporting]
# [START error_reporting_quickstart]
# [START error_reporting_setup_python]
def simulate_error():
    from google.cloud import error_reporting

    client = error_reporting.Client()
    try:
        # simulate calling a method that's not defined
        raise NameError
    except Exception:
        client.report_exception()
# [END error_reporting_setup_python]
# [END error_reporting_quickstart]
# [END error_reporting]


# [START error_reporting_manual]
# [START error_reporting_setup_python_manual]
def report_manual_error():
    from google.cloud import error_reporting

    client = error_reporting.Client()
    client.report("An error has occurred.")
# [START error_reporting_setup_python_manual]
# [END error_reporting_manual]


if __name__ == '__main__':
    simulate_error()
    report_manual_error()
