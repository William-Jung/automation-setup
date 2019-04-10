

def before_all(context):
    # Parse our command line args
    if "url" in context.config.userdata:
        context.url = context.config.userdata['url']