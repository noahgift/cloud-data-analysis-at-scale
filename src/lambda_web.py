def lambda_handler(event, context):
    content = """
    <html>
    <p> Hello website Lambda </p>
    </html>
    """
    response = {
        "statusCode": 200,
        "body": content,
        "headers": {"Content-Type": "text/html",},
    }
    return response
